import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    lang_list = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it",
                 "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-cn"]
    if language not in lang_list:
        raise pytest.UsageError("--language should be correct")
    return language


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    browser.quit()
