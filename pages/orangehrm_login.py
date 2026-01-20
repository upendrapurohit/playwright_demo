from playwright.sync_api import Page


class loginpage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state("networkidle")
