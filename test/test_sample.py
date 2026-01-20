import re
from playwright.sync_api import expect

def test_google_title(page):
    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle")
    
    # Accept cookies if present
    try:
        page.get_by_role("button", name="Accept all").click(timeout=2000)
    except Exception:
        pass  # Consent button not present
    
    # Search using textarea selector (more reliable than role-based)
    page.fill("textarea[name='q']", "Playwright python")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))