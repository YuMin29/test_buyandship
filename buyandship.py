import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BuyAndShip:

    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)
        self.driver = driver

    def click_region_element(self):
        region_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "bs-header-top-bar__content__country")
            )
        )

        if region_element is None:
            print("not find region element")
        else:
            region_element.click()

    def switch_region(self, target_region):
        print("Start to switch region => ", target_region)

        region_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "bs-language-list__item")
            )
        )

        if region_list is None:
            print("not find region_list")
        else:
            print("region list leh => ", len(region_list))

        for region_item in region_list:
            region_name = region_item.find_element(
                By.CLASS_NAME, "bs-language-list__item__name"
            )
            print("item name => ", region_name.text.strip())

            if region_item.is_displayed() and region_item.is_enabled():
                if region_item.text in target_region:
                    region_item.click()
                    new_region = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, "bs-header-top-bar__content__country__text")
                        )
                    )
                    print("new region => ", new_region.text)
                    return new_region

    def quit_chrome(self):
        self.driver.quit()
