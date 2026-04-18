from playwright.sync_api import Page, expect

class DropdownPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown")

    def select_option(self, value):
        self.page.locator("#dropdown").select_option(value)

    def verify_selected(self, text):
        expect(self.page.locator("#dropdown")).to_have_value(text)