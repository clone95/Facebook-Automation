from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://reddit.com")

loginElem = browser.find_element_by_link_text('LOG IN')

loginElem.click()

mailElement = browser.find_element_by_id('loginUsername')
mailElement.send_keys('ciao')

pwdElement = browser.find_element_by_id('loginPassword')

