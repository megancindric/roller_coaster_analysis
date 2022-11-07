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
        "Wood": ".//h4[contains(.,'Wooden')]/following-sibling::table/tbody",
        "Steel": ".//h4[contains(.,'Steel')]/following-sibling::table/tbody"
    },
    2021: {
        "Wood": ".//h3[contains(.,'Wooden')]/following-sibling::figure/table/tbody",
        "Steel": ".//h2[contains(.,'Steel')]/following-sibling::figure/table/tbody"
    },
    2010: {
        "Wood": ".//h4[contains(.,'Wood')]/following-sibling::figure/table/tbody",
        "Steel": ".//h4[contains(.,'Steel')]/following-sibling::figure/table/tbody"
    },
}
years = [2022, 2021, 2019, 2018, 2017, 2016,
         2015, 2014, 2013, 2012, 2011, 2010]
years = [2022]
for year in years:
    # Navigating to the correct page, by year
    page.find_element(By.PARTIAL_LINK_TEXT, f"{year}").click()
    # Establishing XPATH to the Wooden & Steel coasters
    steel_xpath = ".//h4[contains(.,'Steel')]/following-sibling::figure/table/tbody"
    wood_xpath = ".//h4[contains(.,'Wooden')]/following-sibling::figure/table/tbody"
    # If the year is one of our exceptions with a unique XPATH, we will update with correct path
    if year in weird_xpaths.keys():
        steel_xpath = weird_xpaths[year]["Steel"]
        wood_xpath = weird_xpaths[year]["Wood"]

    steel_table = page.find_element(
        By.XPATH, steel_xpath)
    steel_rows = steel_table.find_elements(By.XPATH, './/tr')
    wood_table = page.find_element(
        By.XPATH, wood_xpath)
    print(steel_rows[0].text, "Year of Award")
    print(steel_rows[1].text, year)
    page.back()
page.quit()


def process_table_row(table_row, year):
    pass
    # We will only extract first 5 values (Rank, Name, Park, Location, Supplier, Year_Built)
    # We will also append Year_of_Award using year variable
    # Depending on the year, the structure of the table may be slightly different!
    # 2010 - Rank, Name, Park, Location, Year_Built, Supplier, Votes
# 2011 - Rank, Name, Park, Location, Year_Built, Supplier, Points
# 2012 - Rank, Name, Park, Location, Year_Built, Supplier, Points
# 2018 - Rank, Name, Park, Location, Supplier, Year_Built, Votes
# 2019 - Rank, Name, Park, Location, Supplier, Year_Built
# 2021 - Rank, Name, Park, Location, Supplier, Year_Built
# 2022 - Rank, Name, Park, Location, Supplier, Year_Built
