# The purpose of this script is to scrape the Golden Ticket Awards website for award winning coasters
# From 2010 to 2022.  We will scrape for the following attributes:
# Ranking
# Name
# Park **May need to be cleaned**
# Supplier
# Year of Award
# Year Built
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

driver = Service("./chromedriver.exe")
page = webdriver.Chrome(service=driver)
page.get("https://goldenticketawards.com/past-gta-winners/")
weird_xpaths = {
    2022: {
        "Wood": ".//h4[contains(.,'Wooden')]/following-sibling::table",
        "Steel": ".//h4[contains(.,'Steel')]/following-sibling::table"
    },
    2021: {
        "Wood": ".//h3[contains(.,'Wooden')]/following-sibling::figure/table",
        "Steel": ".//h2[contains(.,'Steel')]/following-sibling::figure/table"
    },
    2010: {
        "Wood": ".//h4[contains(.,'Wood')]/following-sibling::figure/table",
        "Steel": ".//h4[contains(.,'Steel')]/following-sibling::figure/table"
    },
}
# All links will contain the text "/YYYY-gta-winners/" - we'll use a partial link query
years = [2022, 2021, 2019, 2018, 2017, 2016,
         2015, 2014, 2013, 2012, 2011, 2010]
for year in years:
    # This will also allow us to set Year value for each page's entries
    steel_xpath = ".//h4[contains(.,'Steel')]/following-sibling::figure/table"
    wood_xpath = ".//h4[contains(.,'Wooden')]/following-sibling::figure/table"

    page.find_element(By.PARTIAL_LINK_TEXT, f"{year}").click()
    time.sleep(2)
    if year in weird_xpaths.keys():
        steel_xpath = weird_xpaths[year]["Steel"]
        wood_xpath = weird_xpaths[year]["Wood"]
    # 2022 h4/strong /following-sibling::table
    # 2021 h3/strong /following-sibling::figure/table
    # 2019 h4/strong /following-sibling::figure/table
    # 2018 h4/strong /following-sibling::figure/table
    # 2017 h4 /following-sibling::figure/table
    # 2016 h4 /following-sibling::figure/table
    # 2015 h4 /following-sibling::figure/table
    # 2014 h4 /following-sibling::figure/table
    # 2013 h4 /following-sibling::figure/table
    # 2012 h4 /following-sibling::figure/table
    # 2011 h4 /following-sibling::figure/table
    # 2010 h4 /following-sibling::figure/table

    steel_table = page.find_element(
        By.XPATH, steel_xpath)
    wood_table = page.find_element(
        By.XPATH, wood_xpath)
    print(year, steel_table, wood_table)
    page.back()
page.quit()
