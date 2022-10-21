"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture()
def browser_management_desktop():
    browser.config.window_width = 1044
    browser.config.window_height = 785
    browser.open('https://github.com')
    yield


@pytest.fixture()
def browser_management_mobile():
    browser.config.window_width = 500
    browser.config.window_height = 650
    browser.open('https://github.com')
    yield


def test_github_desktop(browser_management_desktop):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_management_mobile):
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
