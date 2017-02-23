import requests
#import suds
from suds.client import Client


url = 'http://218.58.226.142:9999/axis2/services/SmartService'
# r = requests.post(url)
# print r.text

c = Client(url)