from selenium import webdriver
import time

# disabling notifications browser-level popUP

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)


def main():

    print(menu)
    your_email = input("Insert e-mail")
    your_pwd = input("Insert password")

    time.sleep(1)
    browser.get('https://facebook.com')

    # finding login input areas

    mail_element= browser.find_element_by_id('email')
    pwd_element = browser.find_element_by_id('pass')

    # filling login form

    mail_element.send_keys(str(your_email))
    pwd_element.send_keys(str(your_pwd))

    # login

    submit_element = browser.find_element_by_id('u_0_2')
    submit_element.click()
    want_notif = input(notifications)

    if want_notif == "yes":
        get_notifications()
    else:
        exit(-1)


def get_notifications():

    notifications_element = browser.find_element_by_id('fbNotificationsJewel')
    notifications_element.click()
    # time to load "see more" button
    time.sleep(2)

    see_more_element = notifications_element.find_element_by_class_name("seeMore")
    see_more_element.click()


menu = "Welcome to Facebook utility\n. Please insert email and password\n"

notifications = "Do you want to open notification?\n" \
                "yes / no\n"

main()


