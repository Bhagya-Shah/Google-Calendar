from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE='credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
# print(dir(service))

calendar = {
    'summary': 'calendarSummary',
}

#InsertCalendar
# created_calendar = service.calendars().insert(body=calendar).execute()
# print(created_calendar)

#DeleteCalendar
service.calendars().delete(calendarId='9uqtoa2ruofsb100ft1nc7i14c@group.calendar.google.com').execute()
