from selenium import webdriver
import platform
from distutils.spawn import find_executable

def run(browser: str="") -> webdriver:
    # Search for browsers
    system = platform.system()
    browsers = {
        "firefox": 0,
        "chrome": 0,
        "edge": 0,
    }
    if system == "Linux":
        if find_executable("firefox"):
            browsers["firefox"] = 1
        if find_executable("chromium"):
            browsers["chrome"] = 1
    elif system == "Windows":
        if find_executable("firefox"):
            browsers["firefox"] = 1
        if find_executable("chrome"):
            browsers["chrome"] = 1
    
    if browsers["chrome"] == 1:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
        return webdriver.Chrome()
    elif browsers["firefox"] == 1:
        import geckodriver_autoinstaller
        geckodriver_autoinstaller.install()
        return webdriver.Firefox()