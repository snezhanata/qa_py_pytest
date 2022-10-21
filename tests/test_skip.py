"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_management():
    browser.config.window_width = 1011
    browser.config.window_height = 785
    browser.open('https://github.com')
    yield


def test_github_desktop(browser_management):
    if browser.config.window_width <= 1011:
        pytest.skip(reason='Browser window size is for mobile')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.config.hold_browser_open = True


def test_github_mobile(browser_management):
    if browser.config.window_width > 1011:
        pytest.skip(reason='Browser window size is for desktop')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
