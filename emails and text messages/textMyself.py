"""this allows me import this py file later when I need It and make a program
that sends me a text message when the program is done running.
did not want to enter my critical information just in case bad actors get their
hand on It, but If you are planning to use this, you either have to add some inputs for extra safety
which gonna be quiet annoying, or you can just add your information directly to the code, which is not recommended

the importation process should look something like this:
import textmyself
textmyself.textmyself('The boring task is finished.')


"""

import twilio
Ssid = "twilio_ssid"
token = "twilio_token"
my_number = "my_number"
twilios_number = "twilio_number"
from twilio.rest import Client

def text_myself(message):
    twilio_client = Client(Ssid, token)
    twilio_client.messages.create(body=message, from_=twilios_number, to=my_number)
