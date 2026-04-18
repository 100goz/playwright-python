from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_로그인_성공(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("tomsmith", "SuperSecretPassword!")
    login.verify_success()

def test_로그인_실패(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("wronguser", "wrongpassword")
    login.verify_failure()