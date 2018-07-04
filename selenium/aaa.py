import re
from selenium import webdriver

fp = open('company.txt', 'r')
lines = fp.read().split('\n')

for line in lines:
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get('https://robins.jipdec.or.jp/robins/')
    driver.find_element_by_xpath('//*[@id="company"]/div[1]/table/tbody/tr[1]/td/input').send_keys(line)
    driver.find_element_by_xpath('//*[@id="searchExecuteButton"]').click()

    driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[1]/div[1]/div/p[1]/a').click()

    text = driver.find_element_by_xpath('//*[@id="katudouReportTabPanel"]/div[5]/table/tbody/tr/td[1]/p').text

    gyousyu = text.split('\n')[2]
    #gyousyu = text2[2]
    print(gyousyu)

    pattern = "(.*) :(.*)"
    d = re.search(pattern, gyousyu)
    print(d.group(2))
    driver.close()
    driver.quit()
fp.close()








# text = "業種　：不動産・飲食"
#
# pattern = "(.*)：(.*)"
# d = re.search(pattern, text)
# print(d.group(2))
