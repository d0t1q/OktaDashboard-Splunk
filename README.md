Original Application: https://splunkbase.splunk.com/app/2821/

# OktaDashboard-Splunk
Updating the outdated Okta Dashboard to work with the new API

Caveats:
*	A lot of the implimentaitons I've setup still rely on the legacy API call
     `legacyEventType=`
	Once Okta sunsets this Legacy result the dashboard will stop working. 
* 	Version 1.0 and version 1.1 on Splunkbase does not include a bruteforce page 
	even though it is refereced in the documentation and other nav pages. 
	Unsure why this page is referecned at all, I've removed all refeference to
	this page. 
*	The page application_analytics uses a regex to filter out emails from the 
	application lists. If your organization uses email addresses that do not end in
	 `ca | com | net | org` 
	you will need to update this regex to include the extra domain extensions.
*	The page application_analytics  has a drop down multiselect box that should
	fill with a list of applications, I am unable to get this working. Someone
	better than me can most likely fix it. That being said, the page works without
	the filter. 
