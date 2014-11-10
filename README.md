Munki Promote
=========

This Python script will allow the user to set it up to automatically check their Munki Repository and change the catalog based off the last modified time and currently if the appliation is in the testing catalog.  Currently the Munki team is discussing a way to incorporate this into the pkginfo files via an autopromote argument to the makecatalogs function.  You can join in the conversation [here](https://groups.google.com/forum/#!topic/munki-dev/FKWmj4i-VEU/discussion)

Requirements
------------

**munki**

**python**

**access to your repo**

Setup
-----

Copy the munkipromotetemplate.conf as munkipromote.conf and configure the variables:

    MUNKI_REPO = Your Repo Here
    MUNKI_APPS = ['Enter Apps Names used in Munki Here', 'Another Here']
    MUNKI_TIME = Enter your Days here just the name ex... 7
    MUNKI_CATALOGS = ['Catalogs Here', 'testing' 'production']

Notes
-----

Please keep in mind that this is a proof of concept and may not work in your environment.  I am currently looking for a way to allow users to plug in more variables for (ex.. Google Chrome to testing, FireFox to production) but I know this is already in development with the Munki project.  Feel free to post your suggestions here or contact me in the ##OSX-Server chatroom on freenode.
