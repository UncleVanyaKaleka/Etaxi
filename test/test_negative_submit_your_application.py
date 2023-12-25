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


def test_submit_your_application_name_number(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameNumbers)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[1]/ul/li')))


def test_submit_your_application_name_special_characters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameSpecialCharacters)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[1]/ul/li')))


def test_submit_your_application_name_simbols_not_entered(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameSymbolsNotEntered)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[1]/ul/li')))


def test_submit_your_application_number_telethon_latin_letters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonLatinLetters)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[2]/ul/li')))


def test_submit_your_application_number_telethon_special_characters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonSpecialCharacters)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[2]/ul/li')))


def test_submit_your_application_number_telethon_lot_of_signs(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonLotOfSigns)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[2]/ul/li')))


def test_submit_your_application_number_telethon_simbols_not_entered(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/button'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"id_name"]'))).click()
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonSymbolsNotEntered)
    driver.find_element(By.XPATH, '//*[@id=\"reg-form"]/button').click()
    wdw(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"reg-form"]/div[2]/ul/li')))