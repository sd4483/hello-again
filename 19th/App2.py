from datetime import datetime as dt
import time
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.gsmarena.com", "www.theverge.com"]



while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("1")
    else:
        print("fun hours")
    time.sleep(5)
