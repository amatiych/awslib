import boto

import json
from os import path
from boto.s3.key import Key

class AwsHelper:
	"""
		wrappe around aws python lib
	"""

	def __init__(self,config_file):
		with open(config_file,'r') as f:
			json_config = json.load(f)
			self.bucket_name = json_config['bucket']
			self.conn = boto.connect_s3(json_config['aws_key'],json_config['aws_secret'])
			self.bucket = self.conn.get_bucket(self.bucket_name)


	def upload(self,file):
    		_,filename = path.split(file)
    		k = Key(self.bucket)
    		k.key = filename
    		return k.set_contents_from_filename(file)

if __name__ == '__main__':
	fn = "/home/pi/Documents/videos/20160415_16131460736808.h264"
	print("uploading file " + fn)
	key = ""
	secret=""

	aws = AwsHelper('awskeys.json')
	aws.upload(fn)

