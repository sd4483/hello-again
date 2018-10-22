from datetime import datetime as dt
import time

hosts_temp = "C:\Users\sudhe\OneDrive\GitHub\hello again\21st\hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.gsmarena.com", "www.theverge.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print('working hours...')
        with open(hosts_path, 'r+') as host:
            content = host.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    host.write(redirect +" "+ website + "\n")

    else:
        with open(hosts_path, 'r+') as host:
            content = host.readlines()
            host.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    host.write(line)
            host.truncate()

        print('fun hours')
    time.sleep(5)
