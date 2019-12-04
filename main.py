# Script for booking a student meeting rooms 7 days in adv 
# Currently books room E311 from 2-4
import requests 
from bs4 import BeautifulSoup
import datetime

with requests.session() as s:

      page = s.get('https://webapps-5.okanagan.bc.ca/ok/StudentRoomBookings/Booking')
      soup = BeautifulSoup(page.text)
      
      sessionKey = soup.find("input",{"name":"sessionDataKey"})['value']
      headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
      }
      payload = {
            'username': '<studentNumber>@stu.oc', #replace with student number
            'password': '<password>', #replace with password
            'sessionDataKey': sessionKey
      }

      login_url = 'https://auth.okanagan.bc.ca/commonauth/'
      r = s.post(login_url, data=payload,headers=headers)
      print(r)

      #Currently set to 230-430 in room E409
      #Books 7 days in advance 
      #Suggestion is running at 12 AM every day
      booking_date = datetime.datetime.now()
      booking_date += datetime.timedelta(days=7)
      booking_date = booking_date.replace(hour=22,minute=30,second=00,microsecond=000)#Replace hour/min with time you want
      end_time = booking_date.replace(year=1900,day=1,month=1,hour=00) #change to 2 hours past or how ever long you want the room for
      start_time = booking_date.replace(year=1900,day=1,month=1) 

      booking_date = booking_date.isoformat()
      start_time = start_time.isoformat()
      end_time = end_time.isoformat()
      PARAMS = { 
            'bookingDate':"{}.000Z".format(booking_date),
            'endTime':"{}.000Z".format(end_time),
            'resourceId':'9', #Find resouceID for rooms below
            'startTime':"{}.000Z".format(start_time)
      }
      print(PARAMS)
      r = s.post('https://webapps-5.okanagan.bc.ca/ok/StudentRoomBookings/Booking/Create',params = PARAMS)
      print(r)
      
      
      # How the college deals with time         # Resource ID for each room

      # 4pm = 00:00:00                          E204 = 1
      # 5pm = 01:00:00                          E206 = 2
      # 6pm = 02:00:00                          E307 = 6      
      # 7pm = 03:00:00                          E309A = 7
      # 8pm = 04:00:00                          E311 = 22
      # 9pm = 05:00:00                          E409 = 9
      # 10pm = 06:00:00                         L301 = 10
      # 11pm = 07:00:00                         L302 = 11
      # 12pm = 08:00:00                         L303 = 12
      # 1am = 09:00:00                          L304 = 13
      # 2am = 10:00:00                          L305 = 14
      # 3am = 11:00:00                          L308 = 15
      # 4am = 12:00:00                          L312 = 21
      # 5am = 13:00:00                          L310 = 20
      # 6am = 14:00:00
      # 7am = 15:00:00
      # 8am = 16:00:00
      # 9am = 17:00:00
      # 10am = 18:00:00
      # 11am = 19:00:00
      # 12am = 20:00:00
      # 1pm = 21:00:00
      # 2pm = 22:00:00
      # 3pm = 23:00:00

