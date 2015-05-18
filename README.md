Munki Promote
=========

This Python script will allow the user to set it up to automatically (with Jenkins) check their Munki Repository and change the catalog based off the last modified time.  As of the latest update, multiple catalogs can be defined.  Each section is treated as a catalog and you define what you want to promote and from what catalog.  Currently the Munki team is discussing a way to incorporate this into the pkginfo files via an autopromote argument to the makecatalogs function.  You can join in the conversation [here](https://groups.google.com/forum/#!topic/munki-dev/FKWmj4i-VEU/discussion)

Requirements
------------

**munki**

**python**

**access to your repo**

Setup
-----

Copy the munkipromotetemplate.conf as munkipromote.conf and configure the variables:

[main]

REPO = Your Repo Here (ex. /Volumes/Munki/repo [/pkgsinfo is added automatically])

[critical]    

APPS = ['Enter Apps Names used in Munki Here', 'Another Here']

TIME = Enter your Days here just the name ex... 7

PROMOTE_FROM = catalog you are promoting from here

PROMOTE_TO = catalog you are promoting to here

[normal] or whatever name you'd like

APPS = ['Enter Apps Names used in Munki Here', 'Another Here']

TIME = Enter your Days here just the name ex... 7

PROMOTE_FROM = catalog you are promoting from here

PROMOTE_TO = catalog you are promoting to here

Jenkins Config
--------------

What I like to do is configure this to automatically work with Jenkins.  This file is now an executable so you can actually just export the path of where you synced the repository (ex. /Users/macadmin/Documents/munki-promote) by using this command:

**export PATH=$PATH:/Users/macadmin/Documents/munki-promote**

Put this at the beginning of your job script and you won't have to worry about adding it permanently.

Notes
-----

Please keep in mind that this is a proof of concept and may not work in your environment. Feel free to post your suggestions here or contact me in the ##OSX-Server chatroom on freenode.
