from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def _get_news_list(self):
    return self.driver.find_elements_by_css_selector(".friendBrowserNameTitle > a")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)


# opening browser

browser.get('https://facebook.com')

# finding login input areas

mailElement = browser.find_element_by_id('email')
pwdElement = browser.find_element_by_id('pass')

# filling login form

mailElement.send_keys("giac290595@gmail.com")
pwdElement.send_keys("Jellyash")

# login

submitElement = browser.find_element_by_id('u_0_2')
submitElement.click()

# open notifications

# browser.forward()

notificationsEl = browser.find_element_by_id('fbNotificationsJewel')
notificationsEl.click()

time.sleep(2)

seeMoreEl = notificationsEl.find_element_by_class_name("seeMore")
seeMoreEl.click()

list = browser.find_element_by_class_name('_44_u')
print(list)



