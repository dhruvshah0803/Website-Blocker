import platform
import time
from datetime import datetime as dt


current_os = platform.system()                           # getting the platform os
host_path = ""
if(current_os == 'Windows'):
    host_path = r'C:\Windows\System32\drivers\etc\hosts'                # giving host path also r stands passing raw input to avoid problems with /b /n ....
elif(current_os == 'Linux' or current_os == 'Darwin'):
    host_path = r'/etc/hosts'
else:
    print("Please update the file path to get hosts file according to your os")
    

redirect = "127.0.0.1"
    
website_list = ["www.facebook.com" ,
                "www.facebook.com",
                "www.reddit.com",
                "reddit.com" ]

weekno = dt.today().weekday()

while True:
    if(dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 17) and weekno <= 4):
        with open(host_path , 'r+',) as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

        print("Working hours")
        
        print(host_path)
        
    else:
        with open(host_path , 'r+',) as file:
            content = file.readlines()
            file.seek()
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate() 
    time.sleep(5)

