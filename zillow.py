from selenium import webdriver
from time import sleep

#Enter
url="https://www.zillow.com/"
acity="San Jose, CA /r"

class OpenSite:
    def __init__(self, city):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder= \"Enter an address, neighborhood, city, or ZIP code\"]")\
            .send_keys(city)
        self.driver.find_element_by_xpath("//input[@placeholder= \"Enter an address, neighborhood, city, or ZIP code\"]")\
            .sendKeys(Keys.RETURN)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div/div[2]/div/div/form/div/div[1]/label").click()
        sleep(2)
        self.driver.find_element_by_xpath("//h3[contains(text(), 'What type of listings')]")\
            .click()
        sleep(2)

        # self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
        #     .send_keys(username)
        # self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
        #     .send_keys(pw)
        # self.driver.find_element_by_xpath('//button[@type="submit"]')\
        #     .click()
        # sleep(4)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        #     .click()
        # sleep(2)

OpenSite(acity)
