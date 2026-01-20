from playwright.sync_api import Page


class homepage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.user_menu = page.get_by_role("listitem").filter(
            has_text="manda ksdsfkoae;lq"
        )
        self.logout_menuitem = page.get_by_role("menuitem", name="Logout")

    def verify_dashboard_visible(self):
        self.dashboard_heading.wait_for(state="visible")

    def navigate_to_performance(self):
        self.performance_link.click()

    def logout(self):
        self.user_menu.locator("i").click()
        self.logout_menuitem.click()
