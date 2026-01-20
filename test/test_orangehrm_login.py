import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login import loginpage
from pages.orangehrm_home import homepage


def test_orangehrm_login(page: Page) -> None:
    # Initialize login page object
    login_page = loginpage(page)
    login_page.navigate()

    # Perform login
    login_page.login("Admin", "admin123")

    # Initialize home page object
    home_page = homepage(page)

    # Verify successful login by checking for the presence of the dashboard heading
    expect(home_page.dashboard_heading).to_have_text(re.compile("Dashboard", re.IGNORECASE))