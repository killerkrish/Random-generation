import time
import os
import requests
import random
import calendar
from datetime import datetime
int='0123456789'
char='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
#tokenDateTime= 0000000000


						# KEYWORD in API list		
						
keyword=['api','api.connect-dev.bretford.io','mfg','private','locker','deviceconfig','producttype','listFirmwareApplications',
'getFirmwareApplication','versions','orgs','tenant','device','updatefirmware','bay','accesslog','producttype',
'baystack','lockerstackbay','unassigned','assignbayuser','lockeruser','import','parentOrgs','iotupdate','org','bulk','iot',
'baytags','metrics','locker','avgdailyusage','bayopensbyhour','availablebays','assignedusers','orgunit','hierarchy','tenantlist','orgsetup',
'orglist','orgsetup','rootadmin','sso','webuser','attachorg','tenanttype','ssoconnection','role','menu','resource',
'userconfig','isValidUser','attachrole','orgunit','updateWebUserID','tenants','subscription','update','usage','bretford','cusage','v1']

						# Single API

lstApi = ['api.connect-dev.bretford.io/org/api/private/orgs/1546/tenant/GExPU9SLEJ/orgsetup',
'api.connect-dev.bretford.io/mfg/api/private/deviceconfig','api.connect-dev.bretford.io/mfg/api/private/locker/listFirmwareApplications',
'api.connect-dev.bretford.io/iot/api/private/producttype','api.connect-dev.bretford.io/iot/api/private/locker/tenant/baystack/GExPU9SLEJ/1546',
'api.connect-dev.bretford.io/iot/api/private/locker/tenant/assignbayuser','api.connect-dev.bretford.io/orgs/api/private/orgs/role'
'api.connect-dev.bretford.io/iot/api/private/tenant/1546/GExPU9SLEJ/lockeruser/import','api.connect-dev.bretford.io/iot/api/private/lockeruser/GExPU9SLEJ/1546',
'api.connect-dev.bretford.io/iot/api/private/parentOrgs/GExPU9SLEJ/1546','api.connect-dev.bretford.io/iot/api/private/tenant/locker/1546',
'api.connect-dev.bretford.io/iotupdate/api/private/tenant/GExPU9SLEJ/lockeruser','api.connect-dev.bretford.io/iotupdate/api/private/tenant/GExPU9SLEJ/org/1546/lockeruser',
'api.connect-dev.bretford.io/iotupdate/api/private/tenant/GExPU9SLEJ/org/1546/lockeruser/bulk','api.connect-dev.bretford.io/iotupdate/api/private/locker/tenant/baytags',
'api.connect-dev.bretford.io/metrics/api/private/avgdailyusage','api.connect-dev.bretford.io/metrics/api/private/bayopensbyhour',
'api.connect-dev.bretford.io/orgs/api/private/orgs/orgunit','api.connect-dev.bretford.io/orgs/api/private/orgs/1546/tenant/GExPU9SLEJ/hierarchy',
'api.connect-dev.bretford.io/orgs/api/private/orgs/tenantlist','api.connect-dev.bretford.io/orgs/api/private/orgs/1546/tenant/GExPU9SLEJ/orglist',
'api.connect-dev.bretford.io/orgs/api/private/orgs/1546/tenant/GExPU9SLEJ/orgsetup','api.connect-dev.bretford.io/orgs/api/private/orgs/1546/rootadmin',
'api.connect-dev.bretford.io/orgs/api/private/orgs/1546/tenant/GExPU9SLEJ/sso','api.connect-dev.bretford.io/orgs/api/private/tenant/webuser/attachorg',
'api.connect-dev.bretford.io/orgs/api/private/orgs/ssoconnection','api.connect-dev.bretford.io/orgs/api/private/orgs/1546/tenant/GExPU9SLEJ/role',
'api.connect-dev.bretford.io/orgs/api/private/orgs/{orgid}/role/{roleid}/menu']

						# Generate Random values function					

def num(data):
def num(data):
	randa=""
	for c in range(len(data[i])):
		randa +=random.choice(int)
	#print randa	
	return randa
def alphanum(data):
	rand=""
	for c in range(len(data[i])):
		rand +=random.choice(char)
	#print rand
	return rand


						
def change( cmd ):
	returned_value= os.system(cmd)
	cmd ="webdriver-manager start";
	return	

def generateToken():
 cmd="protractor conf.js";
 change(cmd);
 in_file = open("token.txt", "rt") 
 token = in_file.read()         
 in_file.close()                   
 in_file = open("tenantid.txt", "rt") 
 tenantid = in_file.read()         
 in_file.close()                   
 in_file = open("resourse.txt", "rt") 
 resourse = in_file.read()         
 in_file.close()                   
 t=token
 te=tenantid
 r=resourse
 #print('Bearer '+token+'###'+tenantid+'###'+resourse)
 auth_token='Bearer '+token+'###'+tenantid+'###'+resourse
 return auth_token
	
												# API split	
def main():												
	fstApi= True
	#tokenDateTime= 0000000000
	for api in lstApi:
		param=api.split('/')
		#print param
		data=[]
						
									# Save Parameters into data							

		nCnt=0
		posArray=[]
		for para in param:
			if para not in keyword :
				#print ( str(nCnt))
				posArray.append(nCnt)
				data.append(param[nCnt])
			nCnt = nCnt +1
								
								# Parameters Type and Replace values to params
		global i	
		
		for i in range (len(data)):	
			if data[i].isdigit():
				param[posArray[i]] = num(data)
			else:
				param[posArray[i]] = alphanum(data)
		#print data	
		data=[]
		#print param
									
									# Merging the Parameters	
									
		j="/"	
		newurl='https://'+	j.join(param)	
		print newurl
		#print data
		Diff = 0		
		if not fstApi:
			#Check token is valid?
			syscurrentDateTime = datetime.now()
			currentTimeDiff = syscurrentDateTime -tokenDateTime
			Diff =currentTimeDiff.seconds
			print Diff
				
		if(fstApi or Diff>840):
			if  os.path.isfile('token.txt'):
				os.remove("token.txt")
				os.remove("tenantid.txt")
				os.remove("resourse.txt")
			print Diff
			#print fstApi
			fstApi= False
			#Generate new token
			auth_token = generateToken()
			tokenDateTime= datetime.now()
			print(tokenDateTime)	
		
		
	
		
		headers = {'Authorization': auth_token}	
		#print headers
		response = requests.get(newurl, headers=headers)
		print response
	

if __name__== "__main__":
	main()				