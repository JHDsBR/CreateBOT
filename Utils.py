from time import sleep
import warnings
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SECRET



def WaitLogin(driver):
    while(driver.current_url != SECRET.E):
        sleep(0.5)

def GetAccID(driver):
    try:
        elems = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.v-navigation-drawer__content > div > a")))
        for elem in elems:
            if("my channel" in elem.text.lower()):
                return elem.get_attribute("href")
        return None
    except:
        return None


def GetUserName(driver):
    try:
        elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mt-4 > h2.text-h5")))
        return elem.text.strip()
    except:
        return None


def CreateDriver(visible:bool=False):
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('lang=en')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-in-process-stack-traces")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--output=/dev/null")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if(not visible):
        chrome_options.add_argument("--headless")

    return selenium.webdriver.Chrome(options=chrome_options)


