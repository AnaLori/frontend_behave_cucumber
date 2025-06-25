from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless")  # Executar sem interface gráfica
    options.add_argument("--no-sandbox") # Necessário em alguns ambientes Linux restritos
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas de espaço compartilhado
    options.add_argument("--disable-gpu")  # Evita problemas com aceleração gráfica

    # Remover mensagens de erro do console
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

    # Configuração de timeouts
    context.driver.set_page_load_timeout(30)
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()

