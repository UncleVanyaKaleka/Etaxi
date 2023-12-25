import time
import pytest
import chromedriver_autoinstaller
import Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wdw
chromedriver_autoinstaller.install()


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # Переходим на страницу авторизации
    driver.get('http://185.246.118.41/')

    driver.maximize_window()
    yield driver

    driver.quit()


def test_choosing_a_city(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[1]/figure[2]'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[1]/div[2]/button[2]'))).click()
    driver.find_element(By.XPATH, '//*[@id=\"main-section"]/div[1]/div/div/a[10]').click()
    assert driver.current_url == 'http://185.246.118.41/etaxi/Тюмень'


def test_choosing_a_city_search(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[1]/figure[2]'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[1]/div[2]/button[2]'))).click()
    driver.find_element(By.XPATH, '//*[@id=\"main-section"]/div[1]/div/input').send_keys(Data.YourCity)
    assert driver.current_url == 'http://185.246.118.41/etaxi/Томск'
