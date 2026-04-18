from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def verify_success(self):
        expect(self.page.get_by_text("You logged into a secure area!")).to_be_visible()

    def verify_failure(self):
        expect(self.page.get_by_text("Your username is invalid!")).to_be_visible()