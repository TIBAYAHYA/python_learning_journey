"""this program is supposed,to run in the morning just before the user wakes up,  scrap data froma weather site, analyse the data, 
find out If Its gonna be a rainy day or not, and If Its a rainy day, send you an sms reminding you to take an umbrella just in case!
in this program we gonna need quite some modules, twilio for sms stuff, request and bs4 to scrap data, and mybe more
"""
import requests
import bs4
import twilio.rest

def web_data():
    
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = requests.get("https://www.accuweather.com/en/ma/fes/243090/weather-forecast/243090",headers=headers) 
    #using different agent, because original does not get through the site security
    soup = bs4.BeautifulSoup(req.text,"html.parser")
    rain_data = {}
        ### scraping stuff!
    for item in soup.select('.hourly-list__list__item'):
        time = item.select_one('.hourly-list__list__item-time')
        precip = item.select_one('.hourly-list__list__item-precip span')
        ### scraping stuff!
        if precip and time:
            rain_data[time.text.strip()] = precip.text.strip()  # making a dict off the scraped data
    rain_data_interpreter(rain_data) #interpreting the dict data
    
    



def rain_data_interpreter(rain_data):
    raining_hours_dict = {}
    for key, value in rain_data.items():
        percentage = int(value.strip("%"))  # making the % format readable for program's comparison
        if percentage > 49:                 # 50, why?, because AI told me so
            raining_hours_dict[key] = value # adding the values above number in the form of ANOTHER dictionary
            
    rain_data_string = "\n".join([f"At {time} the Chance of rain is {percenta}"for time,percenta in raining_hours_dict.items()])
    rain_data_string = "Weather reminder!!!\n"+ rain_data_string

    #the above variable, we make the message that is gonna get sent to the number, very cool!
####checking If the data is worthy to be sent, dont wanna waste twilio credits sending "OH TODAY IS A GOOD DAY!"
    if rain_data_string:
        message_sending(rain_data_string)
    else:
        print("No need to send!")
        time.sleep(60) #sleeping for a minute, so the program does not send the same message twice
        before_waking_timer()
####
    



### twilio part!, made sure not to include any sensitive information this time, this way I dont have to force git commit deleting
import twilio
ssid = input("Enter your twilio ssid: ")
token = input("Enter your twilio password: ")
my_number = input("Enter your number: ")
twilios_number = input("Enter twilio number: ")
###
import time

def message_sending(rain_data_string):
    
    twilio_client = twilio.rest.Client(ssid,token)  #LOGGING IN TO TWILIO
    twilio_client.messages.create(body=rain_data_string, from_=twilios_number, to=my_number)  #look above If you want what rain_data_string is
    print("Message sent!")
    time.sleep(60) #sleeping for a minute, so the program does not send the same message twice
    before_waking_timer()


import datetime

def before_waking_timer():
    while True:
        now = datetime.datetime.now()  #refreshing the time
        if now.hour == 6 and now.minute == 30:    # make sure to add your own time, so the program does not wake you up at 3 am or smth
            web_data()
        else:
            print("Not yet!")
            time.sleep(60)




before_waking_timer()