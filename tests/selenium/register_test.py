import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from faker import Faker

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_complete_end_to_end_happy_path(self):
        driver = self.driver
        driver.get('https://soulmate-0737784650f0.herokuapp.com/')


        register_link = driver.find_element(By.LINK_TEXT, 'Register')
        register_link.click()


        fake = Faker()
        email = fake.email()
        password = fake.password(length=12)

        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        password_input_confirm = driver.find_element(
            By.NAME, "passwordConfirmation")
        password_input_confirm.send_keys(password)

        login_button = driver.find_element(
            By.XPATH, '//button[@type="submit"]')
        login_button.click()

        register_link = driver.find_element(By.ID, 'promptbutton')
        register_link.click()

        register_link = driver.find_element(By.ID, 'promptbutton')
        register_link.click()

        expected_title = "Soulmate - Settings"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

    