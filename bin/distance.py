# ehaddad@splunk.com ELias Haddad

import os
import splunk.Intersplunk, logging as logger
import math

logger.basicConfig(level=logger.WARN, format='%(asctime)s %(levelname)s %(message)s',
                   filename=os.path.join(os.environ['SPLUNK_HOME'],'var','log','splunk','distance.log'),
                   filemode='a')

def distance(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    
    if ((lat1==lat2) & (long1==long2)):
        return 0
    else:
        degrees_to_radians = math.pi/180.0
            
        # phi = 90 - latitude
        phi1 = (90.0 - lat1)*degrees_to_radians
        phi2 = (90.0 - lat2)*degrees_to_radians
            
        # theta = longitude
        theta1 = long1*degrees_to_radians
        theta2 = long2*degrees_to_radians
            
        # Compute spherical distance from spherical coordinates.
            
        # For two locations in spherical coordinates 
        # (1, theta, phi) and (1, theta, phi)
        # cosine( arc length ) = 
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc length
        
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )

        # Remember to multiply arc by the radius of the earth 
        # in your favorite set of units to get length.
        return arc*3959



def main():
    try:
        messages = {}
        keywords, options = splunk.Intersplunk.getKeywordsAndOptions()
        results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()

        outputField = options.get('outputField', 'distance')
        inputFieldLat1= options.get('inputFieldLat1', None)
        inputFieldLat2= options.get('inputFieldLat2', None)
        inputFieldLon1= options.get('inputFieldLon1', None)
        inputFieldLon2= options.get('inputFieldLon2', None)

        if results:
            for result in results:
                if ((result[inputFieldLat1]!="") & (result[inputFieldLat2]!="") & (result[inputFieldLon1]!="") & (result[inputFieldLon2]!="")): 
            		result[outputField] = distance(float(result[inputFieldLat1]), float(result[inputFieldLon1]), float(result[inputFieldLat2]), float(result[inputFieldLon2]))        
        
            splunk.Intersplunk.outputResults(results)
    
    except Exception as e:
        import traceback
        stack =  traceback.format_exc()
        splunk.Intersplunk.generateErrorResults(str(e))
        logger.error(str(e) + ". Traceback: " + str(stack))

if __name__ == '__main__':
    main()



