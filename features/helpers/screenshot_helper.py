import os
from datetime import datetime

def take_screenshot(driver, directory, step_name):
    """Tira screenshot e salva em arquivo"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{step_name}_{timestamp}.png".replace(" ", "_")
    filepath = os.path.join(directory, filename)
    driver.save_screenshot(filepath)
    print(f"Screenshot salvo em: {filepath}")