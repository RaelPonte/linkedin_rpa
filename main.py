from webdriver import Selenium
from connection_deletor import ConnectionDeletor
from auth import Authenticator

class Automation:
    def __init__(self):
        self.selenium = Selenium(headless=True)
        self.driver = self.selenium.get_webdriver()

    def run(self):
        auth = Authenticator(self.driver)
        auth.login()
        print("Login realizado com sucesso!")
        
        connection_deletor = ConnectionDeletor(self.driver)
        connection_deletor.delete_connections()
        
        self.selenium.close_webdriver()
        print("Automação finalizada com sucesso!")
    
if __name__ == "__main__":
    automation = Automation()
    automation.run()
