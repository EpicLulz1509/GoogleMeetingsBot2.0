from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# assign email id and password
mail_address = '21051549@kiit.ac.in'
password = ''

# create chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument('--log-level=3')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 2,
	"profile.default_content_setting_values.media_stream_camera": 2,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", options=opt)




def login(mail_address, password):
	# Login Page
	driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def login2(mail_address, password):
    # Login again

    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
    # input Password
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
    print("Enter something for classes to begin")
    ans = (input())




def turnoff():
	# turn off Microphone
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/span/span/div/div[1]/span[2]/svg').click()
	driver.implicitly_wait(3000)

	# turn off camera
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div[1]/div[4]/div[2]/div/div[1]').click()
	driver.implicitly_wait(3000)


def joinNow():
	# Join meet
	print(1)
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button').click()
	print(1)


def meet(day):
    count = True
    for i in day:
        if count == False:
            print("Enter something to move to the next meeting")
            confirm = input()
        # if count == False:
        #     driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
        driver.get(i)
        if count == True:
            login2(mail_address, password)
            count = False
        joinNow()





# login to Google account
login(mail_address, password)

monday = ["https://meet.google.com/brh-rbsf-siz", "https://meet.google.com/pnm-jtex-ymn", "https://meet.google.com/quy-gjic-yxf"]
tuesday = ["https://meet.google.com/pnm-jtex-ymn", "https://meet.google.com/khh-akcm-adv", "https://meet.google.com/brh-rbsf-siz", "https://meet.google.com/kox-ocvc-mbq"]
wednesday = ["https://meet.google.com/khh-akcm-adv", "https://meet.google.com/qhe-vsqh-dck", "https://meet.google.com/pnm-jtex-ymn", "https://meet.google.com/brh-rbsf-siz"]
thursday = ["https://meet.google.com/brh-rbsf-siz", "https://meet.google.com/kox-ocvc-mbq", "https://meet.google.com/qhe-vsqh-dck"]
friday = ["https://meet.google.com/kox-ocvc-mbq", "https://meet.google.com/quy-gjic-yxf", "https://meet.google.com/qhe-vsqh-dck", "https://meet.google.com/khh-akcm-adv", "https://meet.google.com/brh-rbsf-siz"]


meet(monday)

# # go to google meet
# driver.get('https://meet.google.com/brh-rbsf-siz')
# login2(mail_address, password)
# #turnoff()
# joinNow()
