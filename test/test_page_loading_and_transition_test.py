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


def test_loading_page_main(driver):
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"main-section"]/div[2]/div/section/div[2]/div[1]/button')))
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"main-section"]/div[3]/section[1]/h2')))
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '///*[@id=\"catalog"]/h2')))
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"reviews"]/h2')))
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/footer/div/div/div[1]/div[2]/a')))


def test_loading_page_contacts(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[4]/a'))).click()
    assert driver.current_url == 'http://185.246.118.41/etaxi/Екатеринбург/contacts/'
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"contacts"]/div[2]')))


def test_loading_page_about(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    assert driver.current_url == 'http://185.246.118.41/etaxi/Екатеринбург/about/'
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[1]')))
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[//*[@id=\"main-section"]/div[2]/section[2]')))
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[//*[@id=\"main-section"]/div[2]/section[4]/div')))


