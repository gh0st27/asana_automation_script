#!/usr/bin/python -tt
import os
import requests

class Asana_Auto:

	def __init__(self,auth_key,task_id_location,attachment_location):
		self.auth_key = auth_key
		self.task_id_location = task_id_location
		self.attachment_location = attachment_location

	def find_attachment(self):
		if os.path.exists(self.attachment_location) and os.path.isdir(self.attachment_location):
			if not os.listdir(self.attachment_location):
				print("Directory is empty")
				exit(1)
			else:
				print("Directory is not empty")
		else:
			print("Given Directory don't exists")
			exit(0)

	def file_to_dict(self):
		d = {}
                with open(self.task_id_location) as f:
		        for line in f:
	        		(key, val) = line.split(':')
                		d[key] = int(val)
		return d

	def fetch_username(self,dict):
		os.chdir(self.attachment_location)
                print os.getcwd()
                for r, d, f in os.walk(attachment_location):
                	for file in f:
                         	file_name = file
				full_file_path = os.path.join(r, file)
				#print "file to attach:", full_file_path
                                print "fetching username from fileName...."
                                mysplit = file_name.split('.',1)[0]
                                user_name = mysplit.split('_',2)[2]
                                #print "usernaem is:", user_name
				for key, values in dict.items():
					#print key, ":", values
					if user_name.lower() == key.lower():
						print 'match'
						print "sending this attachment to upload fuct", full_file_path
						print "With this task_ID", values
						print "Calling upload fucnt............"
						automation.upload(full_file_path,values,file_name)
					else:
						print "not match"

	def upload(self,full_file_path,values,file_name):
		print " in upload func"
		url = 'https://app.asana.com/api/1.0/tasks/%s/attachments' %values
		print url
		print "full path of file::", full_file_path
		print "file name is", file_name

		with open(full_file_path, 'rb') as f:
			files = {'file': (file_name, f.read())}
    			r = requests.post(url, auth=(self.auth_key, ''), files=files)
		print(r.status_code)
		print(r.json())
		print "successfully uploaded attachement- leaving upload function"

if __name__ =="__main__":
	auth_key = '0/c97afb9791c5b5c72b63fc5a4abceff1'
	task_id_location = r'/home/python/asana_automation/task_id/task_id_dict.txt'
	attachment_location = r'/home/python/asana_automation/attachment'
	automation = Asana_Auto(auth_key,task_id_location,attachment_location)
	automation.find_attachment()
	dict = automation.file_to_dict()
#	print dict
	automation.fetch_username(dict)
	print "done"
