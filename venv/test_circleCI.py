from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'D:/Office Works Space/New folder/Driver/chromedriver.exe')
#navigates you to the page.



browser.get("http://qxf2.com/selenium-tutorial-main")

assert "Qxf2 Services: Selenium training main" in browser.title
browser.close()