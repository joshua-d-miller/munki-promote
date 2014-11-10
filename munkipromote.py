#!/usr/bin/python
# This script will take items in the Munki testing catalog
# and place them in the the chosen catalog(s) from
# munkipromote.conf
# Joshua D. Miller - josh@psu.edu - Nov 7, 2014
# The Pennsylvania State University

import os, subprocess, plistlib, time, ast
from ConfigParser import SafeConfigParser

# Read Config File
CONFPARSER = SafeConfigParser({'VERBOSE': 'True'})
CONFPARSER.read('munkipromote.conf')

# Read Munki Repo location
MUNKI_REPO = CONFPARSER.get('munki', 'MUNKI_REPO')
# Read applications to move to specified catalog
MUNKI_APPS = ast.literal_eval(CONFPARSER.get('munki', 'MUNKI_APPS'))
# Read last modified time limit (Days)
MUNKI_TIME = CONFPARSER.getint('munki', 'MUNKI_TIME')
# Read catalogs to move the applications to
MUNKI_CATALOGS = ast.literal_eval(CONFPARSER.get('munki', 'MUNKI_CATALOGS'))

# Set applist to auto updated apps list from config
applist = MUNKI_APPS
# Create list to append updated pkginfo/plist apps
updated_apps = []

# Check pkginfo and plist files in Munki Repo and change their catalog
# based of modification time and catalog selected.
for dirname, dirnames, filenames in os.walk(MUNKI_REPO):
	for filename in filenames:
		currentfile = os.path.join(dirname, filename)
		try:
			plist = plistlib.readPlist(currentfile)
			if plist['name'] in applist:
				try:
					modifytime = os.path.getmtime(currentfile)
					now = time.time()
					if 'testing' in plist['catalogs'] and modifytime < now - MUNKI_TIME * 86400:
						try:
							plist['catalogs'] = MUNKI_CATALOGS
							updated_apps.append(list([plist['name'], plist['version'], plist['catalogs']]))
							plistlib.writePlist(plist, (currentfile))
						except:
							print "Could not update pkginfo for " + currentfile
							continue
				except:
					print "Could not read modify time of file " + currentfile
		except:
			print "Could not read plist information from file " + currentfile
# Print output of changes made
if not updated_apps:
	print "No files were changed...."
else:
	try:
		print "Updating catalogs...."
		subprocess.check_call(["makecatalogs"])
	except:
		print "Could not perform the catalog update.  Please run makecatalogs"
	print "%-20s %-20s %-20s" % ("Name", "Version", "Catalogs")
	print "%-20s %-20s %-20s" % ("----", "-------", "--------")
	for name,version,catalogs in updated_apps:
		print "%-20s %-20s" % (name, version),
		print "%-20s".join(catalogs)
		