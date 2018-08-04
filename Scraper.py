from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://facebook.com")

# loginElem = browser.find_element_by_link_text('LOG IN')

# loginElem.click()

mailElement = browser.find_element_by_id('email')
pwdElement = browser.find_element_by_id('pass')
# mailElement.send_keys('ciao')
mailElement.send_keys("giac290595@gmail.com")
pwdElement.send_keys("Jellyash")
# pwdElement = browser.find_element_by_id('loginPassword')
submitElement = browser.find_element_by_id('u_0_2')
submitElement.click()

