import yagmail
import time
from datetime import datetime as dt

#using this info above so that you can uses your computers date and time and save it as dt
sender = 'exampleemail@gmail.com' #name of reciver goes here (does not work with hotmail emails)
receiver = 'reciver@10mail.org' #the name of the reciver goes here
subject = 'example text' #Pplace the subject of the email here
content = '''
the time you have gotten this email it will be 24 hours from now 
''' #Content of the email goes here

while True:
    now= dt.now()
    #NB that the  clock only works in 24 hour clock
    #Edit now.hour to adjust the  hours and now.minute to adjust the mins
    if now.hour == 16  and now.minute ==00:
        yag=yagmail.SMTP(user=sender, password='AppPassword_Here')
        yag.send(to=receiver, subject=subject, contents=subject)
        print('passed test')
        time.sleep(10)