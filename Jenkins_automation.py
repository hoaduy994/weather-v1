import jenkins
import json
import os

host = "https://3a2e-2a09-bac1-7aa0-50-00-17-206.ap.ngrok.io"
username = "hoaduy994"
password = "116cf1b01b16e684582f9f62788bb84fcc"
server = jenkins.Jenkins(host, username=username, password=password)

user = server.get_whoami()
version = server.get_version()
print('hello %s from Jenkins %s' % (user['fullName'], version))