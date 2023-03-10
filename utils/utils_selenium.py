import os
from selenium import webdriver
import json
import time

chrome_options = webdriver.ChromeOptions()

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

chrome_driver_path = os.path.join(os.path.expanduser('~'), "chromedriver.exe")


def flatten_with_chrome(file, folder):
    profile = {
        'printing.print_preview_sticky_settings.appState': json.dumps(appState),
        'savefile.default_directory': folder,
    }
    chrome_options.add_experimental_option('prefs', profile)
    chrome_options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    driver.get(f'file://{file}')
    driver.execute_script('window.print();')
    time.sleep(5)
    driver.close()
