import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display


class Selenium:
    def __init__(self, headless: bool = True):
        load_dotenv()
        self.headless = headless
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-features=VizDisplayCompositor")
        self.options.add_argument("--window-size=1920,1080")
                
        if sys.platform == "win32":
            google_profile_path = fr"--user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data"
        else:
            google_profile_path = fr"--user-data-dir=/home/{os.getlogin()}/.config/google-chrome"
            
        self.options.add_argument(google_profile_path)

    def get_webdriver(self):
        if self.headless:
            self.display = Display(visible=0, size=(1920, 1080))
            self.display.start()

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        return self.driver
    
    def close_webdriver(self):
        self.driver.quit()
        if self.headless:
            self.display.stop()
        
    
