from selenium.webdriver.common.by import By

class Authenticator:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        try:
            self.driver.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in")

            username_field = self.driver.find_elements(By.XPATH, "//input[@id='username']")
            
            if username_field:
                username_field = username_field[0]
                username_field.send_keys("israelponte@icloud.com")

            password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
            password_field.send_keys("c4!ifzRuPNQFLYNn*Ra@7hDLjKytfJq2C")

            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

        except Exception as e:
            pass