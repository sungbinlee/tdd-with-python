from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:8000/")

assert 'successfully' in browser.title