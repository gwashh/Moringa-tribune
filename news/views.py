from calendar import week
from django.shortcuts import HttpResponse, render
import datetime as dt

def welcome(request):
    return render (request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
             <body>
                  <h1> {date.day}--{date.month}--{date.year}</h1>
              </body>
        </html>
             '''
    return HttpResponse(html)

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thusday','Friday','Saturday','Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day

def news_of_day(request):
    date =dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND THE EXACT DAY
    day = convert_dates(date)
    html = f'''
         <html>
              <body>
                   <h1>News for {day} {date.day}--{date.month}--{date.year}</h1>
               </body>
         </html>
            '''
    return HttpResponse(html)