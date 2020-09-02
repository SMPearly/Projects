import time;
from selenium import webdriver;

#time to refresh page (in seconds)
Timer = 120

#youtube link (change link to make it the video you woul like views on)
link = 'https://www.youtube.com/watch?v=hW_WFUs3hfQ'

#number of views
views = 20

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
