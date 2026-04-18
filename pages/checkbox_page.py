from playwright.sync_api import Page, expect

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def get_checkbox(self, index):
        return self.page.locator("input[type='checkbox']").nth(index)

    def click_checkbox(self, index):
        self.get_checkbox(index).click()

    def verify_checked(self, index):
        expect(self.get_checkbox(index)).to_be_checked()

    def verify_unchecked(self, index):
        expect(self.get_checkbox(index)).not_to_be_checked()