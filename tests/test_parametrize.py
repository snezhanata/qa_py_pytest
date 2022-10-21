
"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import have
from selene.support.shared import browser

mobile = (500, 650)
desktop = (1044, 785)


@pytest.fixture(params=[desktop])
def browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com')
    yield


def test_github_desktop(browser_management):
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize(
    'browser_management',
    [mobile],
    indirect=True,
    ids=['Changed to mobile browser window size'],
)
def test_github_mobile(browser_management):
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
