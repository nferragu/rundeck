#!/usr/bin/python
import sys
import os
import winrm
import pprint

if os.environ['RD_JOB_LOGLEVEL']=='DEBUG':
	for i in os.environ.keys():
		print (i+" : "+os.environ[i])

if len(sys.argv)==4:
	(a,host,user,command)=sys.argv
else:
	print ('Args : hostname username password command')
	exit(1)

try:
	passwd=os.environ['RD_CONFIG_PASSWORD']
	if os.environ['RD_JOB_LOGLEVEL']=='DEBUG':
		print ("Host :"+host)
		print ("user :"+user)
		print ("pass :"+passwd)
		print ("cmnd :"+command)
	s=winrm.Session(host,auth=(user,passwd))
	r=s.run_cmd(command)
	print (r.std_out)
except:
	print ('Erreur de connexion winrm')
	exit(1)
