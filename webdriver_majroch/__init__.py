from selenium import webdriver
import platform

def run(browser: str="", mute_browser: bool=True, headless: bool=True) -> webdriver:
    # Search for browsers
    system = platform.system()
    browsers = {
        "firefox": 0,
        "chrome": 0,
        "edge": 0,
    }
    if browser == "firefox":
        browsers['firefox'] = 1
    elif browser == "chrome":
        browsers["chrome"] = 1
    else:
        if system == "Linux":
            from distutils.spawn import find_executable
            if find_executable("firefox"):
                browsers["firefox"] = 1
            if find_executable("chromium"):
                browsers["chrome"] = 1
        elif system == "Windows":
            import os
            if os.path.isdir("C:\\Program Files\\Google\\Chrome"):
                browsers["chrome"] = 1
            if os.path.isdir("C:\\Program Files (x86)\\Google\\Chrome"):
                browsers["chrome"] = 1
            if os.path.isdir("C:\\Program Files\\Mozilla Firefox"):
                browsers["firefox"] = 1
            if os.path.isdir("C:\\Program Files (x86)\\Mozilla Firefox"):
                browsers["firefox"] = 1
        
    
    if browsers["chrome"] == 1:
        import chromedriver_autoinstaller
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        if mute_browser:
            options.add_argument("--mute-audio")
        return webdriver.Chrome(chrome_options=options)
    elif browsers["firefox"] == 1:
        import geckodriver_autoinstaller
        geckodriver_autoinstaller.install()
        options = webdriver.FirefoxProfile()
        if headless:
            options.headless = True
        if mute_browser:
            options.set_preference("media.volume_scale", "0.0")
        return webdriver.Firefox(firefox_profile=options)