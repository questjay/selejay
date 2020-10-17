from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from mylist import mmy
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import json
from bs4 import BeautifulSoup
import ipaddress
import requests
import random
from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Miny(object):
  def __init__(self):
    self.path1 = r"/usr/bin/chromedriver"
    self.driver = None
    self.server = None
    self.st = False
    self.hen = r'/root/browsermob-proxy-2.1.4/bin/browsermob-proxy'
    self.binary = r'/usr/lib/chromium-browser'
    self.proxy = None
    self.n = mmy
    self.number = 1
  def rad_c(self):
    
    try:
        r = open('UsIP.json', "r" )
        m = json.loads(r.read())
        ip = []
        for n in list(ipaddress.ip_network(m[random.randint(1,len(m))]['network']).hosts()):
            ip.append({'ip': str(n)})
        return str(ip[random.randint(1,len(ip))]['ip']) 
        
    except Exception as e:
        return str(ip[0]['ip'])

  def myip(self):
      try:
        sop =  BeautifulSoup(n,'html.parser')
        x = sop.find_all(class_="rna_ad")
        return "rNA3218_{n}_title".format(n =random.randint(1,4))
      except Exception as e:

        pass 
  def heckProxy(self,nm):
    try:
        url ='https://awebanalysis.com/en/ip-lookup/{n}/'.format(n =nm)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
         'Accept': '*/*',
         'Connection': 'keep-alive',
         'True-Client-IP': '3.6.114.227',
         'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        x = requests.get(url, headers= header)
        x =  BeautifulSoup(x.content,'html.parser')
        pr= x.find_all(id="ipdetails")[1].span.get_text()
        if pr == 'Proxy Detected':
           return True
        else:
            return False
    except Exception:
        print('bad error CheckProxy')
        return True


  def browsSart(self):
      try:
             uio = ['https://www.junno.co/news','https://www.junno.co/famouspeople','https://www.junno.co/lyrics','https://www.junno.co/shows/3',
                 'https://www.junno.co/movies/1']
             
             ip = self.rad_c()
             chrome_options = webdriver.ChromeOptions()
             chrome_options.add_argument("--headless")
             chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
             chrome_options.add_argument("--disable-dev-shm-usage")
             chrome_options.add_argument('window-size=1920,{m}'.format(m =random.randint(708,1080)))
             chrome_options.add_argument("--no-sandbox")
             self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
             ty = self.myip()
             print(ty)
             self.driver._client.set_header_overrides(headers= {'X-Forwarded-For':'{n}'.format(n=ip) ,'Via':'{n}'.format(n=ip),
                                'X-Real-IP':'{n}'.format(n=ip), 'True-Client-IP':'{n}'.format(n=ip), 'Forwarded':"'for={n}:{m}'".format(n=ip,m =random.randint(20000,60000)),
                                                                                                                                      'User-Agent':'{n}'.format(n = random.choice(self.n))})
             self.driver.get(uio[random.randint(1,len(uio)-1)])
             
             element_present = EC.presence_of_element_located((By.XPATH, '//body'))
             WebDriverWait(self.driver, 5).until(element_present)
             self.driver.find_element_by_id( '{n}'.format(n=ty)).click()
             element_present = EC.presence_of_element_located((By.XPATH, '//body'))
             data = WebDriverWait(self.driver, 5).until(element_present)
             time.sleep(1)
             self.driver.delete_all_cookies()
             self.driver.execute_script('window.localStorage.clear();')
             self.driver.execute_script('window.sessionStorage.clear();')
             self.driver.quit()
             print('good')
      
      except Exception:
           print('bad error CheckProxy')
           if self.driver:
               self.driver.quit()
  
if __name__ == '__main__':
    
    miny = Miny()
    while True:
        miny.browsSart()
        time.sleep(1)
