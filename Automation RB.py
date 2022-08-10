from ast import Return 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def war_entry():
    driver.get("https://www.redbubble.com/fr")
    time.sleep(1)
    
def web_entry():
    driver.get("https://www.redbubble.com/fr/auth/login")
    search = driver.find_element_by_id("ReduxFormInput1") 
    search.send_keys("wallgala01@gmail.com")
    search_pwd = driver.find_element_by_id("ReduxFormInput2")
    search_pwd.send_keys("123456789")
    search_pwd.send_keys(Keys.RETURN)

def image_logger():
    driver.get("https://www.redbubble.com/portfolio/images/new?ref=account-nav-dropdown")
    image_input = driver.find_element_by_id("select-image-single")
    image_input.send_keys("D:\\Wallpapers\\16.jpg")
    image_input.send_keys(Keys.RETURN)

def banner_rm():
    time.sleep(11)
    driver.get.window_handles()
    toe = driver.find_element_by_id("sidebar-overlay-lightbox-6d96416b-2d7a-43f0-adc8-433485ead063-1650126366241")
    toe.click()

def design_info() :
    image_title = driver.find_element_by_xpath('//*[@id="work_title_fr"]')
    image_title.click()
    image_title.send_keys("title for the quote")
    image_tags = driver.find_element_by_id("add-work-details__tags")
    image_tags.is_selected()
    image_tags.send_keys("quote,motivation,wise,brand,typography,deep meaning,motivation quotes,")





all_enable = driver.find_element_by_class_name("rb-button enable-all")
all_enable.send_keys(Keys.RETURN)
true_work = driver.find_element_by_id("work_safe_for_work_true")
true_work.send_keys(Keys.RETURN)
select_tee = driver.find_element_by_id("work_defult_product")
select_tee.send_keys("t t t")
