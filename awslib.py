import boto

from os import path
from boto.s3.key import Key

class AwsHelper:

	def __init__(self,bucket, aws_key, aws_secret):
		self.bucket_name = bucket
		self.conn = boto.connect_s3(aws_key,aws_secret)
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

	aws = AwsHelper(key,secret)
	aws.upload(fn)

