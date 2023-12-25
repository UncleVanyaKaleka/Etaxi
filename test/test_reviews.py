import time
import pytest
import chromedriver_autoinstaller
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


def test_reviews_text(driver):
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"reviews"]/h2'))).click()
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"review-text__slider-container"]/div[1]')))
    driver.find_element(By.XPATH, '//*[@id=\"review-text__slider-container"]/div[1]/div[3]/div[2]/a').click()
    assert driver.current_url == \
           'https://tomsk.flamp.ru/firm/jo_taksi_taksopark_dlya_voditelya-70000001021276923#reviews'


def test_reviews_video(driver):
    wdw(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=\"reviews"]/div[1]/div[1]')))
    driver.find_element(By.XPATH, '//*[@id=\"reviews"]/div[1]/div[1]/div[3]/video').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id=\"reviews"]/div[1]/div[1]/div[3]/video').click()
    driver.find_element(By.XPATH, '//*[@id=\"reviews"]/div[1]/div[2]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id=\"reviews"]/div[1]/div[1]/div[4]/video').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id=\"reviews"]/div[1]/div[1]/div[4]/video').click()
