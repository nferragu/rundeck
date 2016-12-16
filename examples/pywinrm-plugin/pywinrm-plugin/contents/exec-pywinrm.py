#!/usr/bin/env python
import sys
import os
import pywinrm
import pprint

pprint.pprint (os.environ)

if len(sys.argv)==4:
	(a,host,user,pass,command)=sys.argv
else:
	print ('Args : hostname username password command')
	exit(1)

try:
	s=winrm.Session(host,auth=(user,pass))
	r=s.run_cmd(command)
	print (r.std_out)
except:
	print ('Erreur de connexion winrm')
	exit(1)
