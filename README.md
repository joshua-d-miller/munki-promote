Munki Promote
=========

This Python script will allow the user to set it up to automatically (with Jenkins or a launch daemon) check their Munki Repository and change the catalog based off the last modified time.  As of the latest update, multiple catalogs can be defined.  Each section is treated as a catalog and you define what you want to promote and from what catalog.  The munki team has indicated that this will most likely never be incorporated but you can use this script at your own discretion.

Requirements
------------

**munki** - Obviously

**Python 3** - Tested with Python 3.8.0

**Your Repo accessible via SMB mount or other means**

Setup
-----

Copy the munkipromotetemplate.json as munkipromote.json and configure the variables:
```
{
  "main": {
    "REPO" : "/Volumes/munki/repo", <-- Your Munki Repo Location Here
    "MAKECATALOGS" : "" <-- Your Makecatalogs location if not using the default
    "TEAMS_WEBHOOK": "" <-- Enter your incoming WebHook here if you'd like the output to be sent to Teams
  },
  "promotions": [
    {
      "TITLE" : "Critical", <-- Title of your promotion group
      "APPS" : ["Google Chrome, Firefox"], <-- Apps you want to promote in quotes and separated by commas
      "TIME" : 2, <-- The amount of days the file has not been modified to signal promotion
      "PROMOTE_FROM" : "testing", <-- Catalog to Promote from
      "PROMOTE_TO" : "production" <-- Catalog to Promote to
    }
  ]
}
```

Jenkins Config
--------------

What you can do is configure this to automatically work with Jenkins.  This file is now an executable so you can actually just export the path of where you synced the repository (ex. /Users/macadmin/Documents/munki-promote) by using this command:

**export PATH=$PATH:/Users/macadmin/Documents/munki-promote**

Put this at the beginning of your job script and you won't have to worry about adding it permanently.

Notes
-----

Please keep in mind that this is a proof of concept and may not work in your environment. Feel free to contact me on [MacAdmins Slack](https://macadmins.org)
