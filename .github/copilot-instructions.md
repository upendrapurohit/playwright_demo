# Copilot Instructions for Playwright Demo

## Project Overview
This is a **Playwright automation project** for browser testing and web scraping. It uses pytest as the test framework with the `pytest-playwright` plugin for fixture integration.

## Architecture & Key Components

### Core Dependencies
- **Playwright** (1.57.0): Browser automation library with sync and async APIs
- **pytest-playwright** (0.7.2): Pytest integration providing `page`, `browser`, `context` fixtures
- **pytest** (9.0.2): Test framework
- **pytest-base-url** (2.1.0): Base URL management for tests

### Project Structure
- `first_test.py`: Example automation script demonstrating basic Playwright workflow
- `venv1/`: Python virtual environment with all dependencies installed

## Development Workflows

### Running Tests
```bash
# Activate environment
.\venv1\Scripts\Activate.ps1

# Run all tests with pytest
pytest

# Run with verbose output
pytest -v

# Run with headed browser (visible)
pytest --headed

# Run specific file
pytest first_test.py
```

### Running Scripts Directly
```bash
# Activate environment and run Python script
.\venv1\Scripts\python.exe first_test.py
```

## Key Patterns & Conventions

### Playwright Sync API Pattern
All code uses the **sync API** (`sync_playwright` context manager):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # Interact with page
    browser.close()
```

### Browser Interaction Patterns
- **Navigation**: `page.goto(url)` with `page.wait_for_load_state("networkidle")`
- **Selectors**: CSS selectors with `page.click()`, `page.fill()`, `page.query_selector()`
- **Keyboard**: `page.keyboard.press()` for keyboard events
- **Error Handling**: Wrap selectors that may not exist in try/except blocks (see cookies dialog in first_test.py)
- **Waits**: Use `page.wait_for_load_state()` for network stability

### Test Fixture Usage (pytest-playwright)
When writing tests, fixtures provide browser context:
```python
def test_example(page):
    page.goto("https://example.com")
    # Test code
```

## Integration Points

### External Dependencies
- **Browser Engines**: Chromium (default), Firefox, WebKit available via `p.chromium`, `p.firefox`, `p.webkit`
- **Network**: Tests require internet access for external sites
- **OS**: Cross-platform (Windows, macOS, Linux supported)

## Common Tasks

### Adding a New Test
1. Create test file with `test_*.py` naming
2. Define function with `test_` prefix taking `page` fixture
3. Use `page.goto()`, selectors, and assertions
4. Run with `pytest`

### Handling Dynamic Content
- Use `page.wait_for_load_state()` after navigation
- Use `page.wait_for_selector()` before interacting with elements
- Wrap uncertain selectors in error handling (see cookies dialog pattern)

## Debugging Tips
- Set `headless=False` in `launch()` to see browser interaction
- Add `page.screenshot(path="debug.png")` to capture state
- Use `page.pause()` to interactively debug execution
- Check Playwright Inspector: `PWDEBUG=1 pytest`

## Important Notes
- The environment uses Greenlet 3.3.0 for async support in dependencies
- All Playwright interactions are synchronous; async patterns are in dependencies but not used in primary code
