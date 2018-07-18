from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

def initCalendarAPI():
	# Setup the Calendar API
	SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
	store = file.Storage('credentials.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('calendar', 'v3', http=creds.authorize(Http()))

def getCalenderEvents():
	# Call the Calendar API
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
	                                      maxResults=10, singleEvents=True,
	                                      orderBy='startTime').execute()
	events = events_result.get('items', [])
	return events #Probably in form of jabqnchvht5r2pjv0haqlg1j8s%40group.calendar.google.com

def addCalendarsToHTML(userCalendars):
	startOfCalendarIFrame = '''<iframe src="https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=dbough%40salesforce.com&amp;color=%231B887A&amp;'''
	endOfCalendarIFrame = '''ctz=America%2FNew_York" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'''
	
	html = startOfCalendarIFrame
	for calendar in userCalendars:
		html += "src=" + calendar + "&amp;color=%23691426&amp;"
	html += endOfCalendarIFrame
	print('Calendar HTML: ', html)
	return html

def main():
	initCalendarAPI()
	events = getCalenderEvents()
	if not events:
	    print('No upcoming events found.')
	for event in events:
	    start = event['start'].get('dateTime', event['start'].get('date'))
	    print(start, event['summary'])
	addCalendarsToHTML(events)

main()