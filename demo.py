from django.http import HttpResponse
import sys, os
import gflags
import httplib2
import time

from googleapiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow,argparser
from rfc3339 import rfc3339

FLAGS = gflags.FLAGS

FLOW = OAuth2WebServerFlow(
client_id='200891717746-emprjdnsl4duha6b0dtrmp6rga5f0r4l.apps.googleusercontent.com',
client_secret='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',
scope='https://www.googleapis.com/auth/calendar',
user_agent='calTest')
#redirect_uri = 'http://127.0.0.1:8000/result/')

storage = Storage('.git/calendar.dat')
flags = argparser.parse_args(args=[])
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run_flow(FLOW, storage,flags)
  
http = httplib2.Http()
cred = credentials.authorize(http)

service = build(serviceName='calendar', version='v3', http=cred,
      developerKey='AIzaSyDVDzxEhXLeC-pJgTR02tLuIxz-sENf3ys')

description = "%s\n" % os.popen("git whatchanged -1 --pretty=format:\"commiter: %cn <%ae>%ndate    : %cd%n%s%n--------------------%n%b%n\"").read()
summary = "[commit] %s" % os.popen("git log -1 --oneline").read()

startTime = time.time() - 60 * 60
endTime = time.time() 


event = {
  'summary': summary,
  'description': description,
  'start' : { 'dateTime' : rfc3339(startTime) },
  'end' : { 'dateTime' : rfc3339(endTime) }
}
created_event = service.events().insert(calendarId='mmandali@codal.com', body=event).execute()
print("Created Event: %s" % created_event['id'])
 







#git log --oneline ->	Fits each commit on a single line which is useful for an overview of the project history.
