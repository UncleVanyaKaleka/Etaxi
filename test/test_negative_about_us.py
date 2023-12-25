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


def test_about_us_ask_a_question_name_number(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameNumbers)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_name_special_characters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameSpecialCharacters)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_name_simbols_not_entered(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.NegativeNameSymbolsNotEntered)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NumberTelethon)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_number_telethon_latin_letters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonLatinLetters)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_number_telethon_special_characters(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonSpecialCharacters)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_number_telethon_lot_of_signs(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonLotOfSigns)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()


def test_about_us_ask_a_question_number_telethon_simbols_not_entered(driver):
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"header-section"]/div/div[2]/div[2]/div[2]/nav/ul/li[5]/a'))).click()
    wdw(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id=\"main-section"]/div[2]/section[5]')))
    driver.find_element(By.ID, 'id_name').send_keys(Data.Name)
    driver.find_element(By.ID, 'id_phone_number').send_keys(Data.NegativeNumberTelethonSymbolsNotEntered)
    driver.find_element(By.ID, 'id_question').send_keys(Data.Question)
    driver.find_element(By.XPATH, '//*[@id="main-section"]/div[2]/section[5]/div/div/form/button').click()
