import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class automation:
    def __init__(self):
        self.get_spot()

    def run_in_day(self):
        print('Timer started')
        time.sleep(3600 * 24)
        print('Time is up, getting next day spot :)')
        get_spot()

    def get_spot(self):
        now = datetime.now()
        date_select = str(now.day + 1)
        driver = webdriver.Firefox()
        driver.get("https://mypass.sixflags.com/reservations.aspx?rt=PARKING")
        elem = driver.find_element_by_id("ctl00_BodyContent_fldLoginEmail")
        elem.send_keys("kylerkibler182@gmail.com")
        elem = driver.find_element_by_id("ctl00_BodyContent_fldLoginPassword")
        elem.send_keys("4Mysixflags182", Keys.ENTER)
        time.sleep(4)
        button = driver.find_element_by_id("BodyContent_cmdSelectAPark")
        button.click()
        time.sleep(2)
        button = driver.find_element_by_link_text(date_select)
        button.click()
        button = driver.find_element_by_id("BodyContent_cmdSelectDate")
        #button.click()
        driver.close()
        self.run_in_day()

automation()
