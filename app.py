from flask import Flask
import pytz 
import datetime as dt

def tz_string(tz_obj):
    return tz_obj.tzinfo.tzname(tz_obj)



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!  Welcome to S14a2023</p>"

@app.route("/datetime")
# show the current date time in the server's timezone and another datetime in the UTC timezone
def datetime():
    time_now= dt.datetime.now() # creating current time 
    sys_time = time_now.astimezone() # creating system time 
    sys_tz = tz_string(sys_time)
    
    utc_time = dt.datetime.now(dt.timezone.utc) # creating utc time now

    if sys_time == 'PDT':
        my_time = sys_time
    else:
        my_time = dt.datetime.now(dt.timezone(dt.timedelta(hours=-7), 'PDT'))
 
    # Display the timezones
    return f""" <p>
                System Timezone: {sys_tz} --- System Time: {sys_time}
                UTC Timezone: {tz_string(utc_time)} --- UTC Time: {utc_time}
                My Timezone: {tz_string(my_time)} --- My Time: {my_time}
                </p>
                """
    
  
