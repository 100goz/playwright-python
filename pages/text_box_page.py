from playwright.sync_api import Page, expect

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://demoqa.com/checkbox")

    def expand_all(self):
        self.page.locator("button[title='Expand all']").click()

    def check_item(self, name):
        self.page.get_by_text(name).click()

    def verify_checked(self):
        expect(self.page.locator(".text-success")).to_be_visible()