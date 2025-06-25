from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

def before_scenario(context, scenario):
    # Configuração robusta do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Remover mensagens de erro do console
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configuração de tempoouts
    context.driver.set_page_load_timeout(30)
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
