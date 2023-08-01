from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

class ConnectionDeletor:
    def __init__(self, webdriver: webdriver) -> None:
        self.driver = webdriver

    def delete_connections(self):
        base_url = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22100364837%22%5D&network=%5B%22F%22%5D&origin=FACETED_SEARCH&"
        self.driver.get(base_url)

        total_pages = self._get_total_pages()

        for page in range(1, total_pages + 1):
            print(f"Deletando conexões da página {page} de {total_pages}.")
            self._delete_connections_on_page(page, base_url)
        
        print("Conexões deletadas com sucesso!")

    def _delete_connections_on_page(self, page: int, base_url: str):
        self.driver.get(base_url + f"page={page}")

        profiles_list = self.driver.find_elements(By.XPATH, "//div[@class='display-flex']//a")

        for profile in profiles_list:
            print(f"Deletando conexão - {profile.text.splitlines()[0]}")
            profile_link = profile.get_attribute("href")
            self._delete_connection(profile_link)
            time.sleep(randint(4, 10))

    def _delete_connection(self, profile_link):
        self.driver.execute_script(f"window.open('{profile_link}', '_blank')")
        self.driver.switch_to.window(self.driver.window_handles[1])

        self._click_more_button()
        self._unfollow()

        self._click_more_button()
        self._click_remove_connection_button()

        self.driver.switch_to.window(self.driver.window_handles[0])

    def _click_more_button(self):
        
        more_button = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[@class='pv-top-card-v2-ctas ']//button//span[text()='More']")))
        more_button.click()

    def _unfollow(self):
        try:
            unfollow_button = WebDriverWait(self.driver, 2.5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Following ')]")))
            unfollow_button.click()

            unfollow_button = WebDriverWait(self.driver, 2.5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Unfollow']")))
            unfollow_button.click()
        except:
            pass

    def _click_remove_connection_button(self):
        try:
            remove_connection_button = WebDriverWait(self.driver, 2.5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@aria-label, 'Remove your connection ')]")))[-1]
            remove_connection_button.click()
        except:
            pass

    def _get_total_pages(self):
        pages_container = self.driver.find_elements(By.XPATH, "//div[@class='search-marvel-srp']/div//ul")[-1]
        total_pages = int(pages_container.find_elements(By.XPATH, "//li")[-1].text)
        print(f"Total de páginas: {total_pages}")
        return total_pages