# Playwright Demo - Browser Automation Testing

A comprehensive Playwright automation project demonstrating browser testing with Page Object Model (POM) pattern using pytest.

## Features

- **Playwright 1.57.0**: Browser automation library for Chromium, Firefox, and WebKit
- **pytest Integration**: Using `pytest-playwright` plugin for fixture management
- **Page Object Model**: Organized page objects for maintainable test code
- **Cross-platform**: Runs on Windows, macOS, and Linux
- **CI/CD Ready**: GitHub Actions workflows for automated testing

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/playwright_demo.git
   cd playwright_demo
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Windows
   python -m venv venv1
   .\venv1\Scripts\Activate.ps1

   # macOS/Linux
   python -m venv venv1
   source venv1/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test/test_orangehrm_login.py -v

# Run with headed browser (visible)
pytest --headed

# Run with debugging
PWDEBUG=1 pytest
```

## Project Structure

```
playwright_demo/
├── pages/                    # Page Object Models
│   ├── __init__.py
│   ├── orangehrm_home.py
│   └── orangehrm_login.py
├── test/                     # Test files
│   ├── __init__.py
│   ├── test_orangehrm_login.py
│   └── test_sample.py
├── utils/                    # Utility functions
├── reports/                  # Test reports (generated)
├── .github/
│   ├── workflows/            # CI/CD workflows
│   │   ├── tests.yml
│   │   └── lint.yml
│   ├── ISSUE_TEMPLATE/       # Issue templates
│   └── CONTRIBUTING.md       # Contributing guidelines
├── first_test.py            # Example automation script
├── requirements.txt         # Python dependencies
├── pytest.ini              # pytest configuration
└── README.md               # This file
```

## Key Components

### Page Object Model

Page objects encapsulate web element locators and actions:

```python
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button:has-text('Login')")
    
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

### Test Example

```python
def test_orangehrm_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")
    
    # Assertions
    expect(page.locator(".dashboard")).to_be_visible()
```

## CI/CD Workflows

This project includes automated testing:

- **Tests workflow** (`.github/workflows/tests.yml`):
  - Runs on Python 3.10, 3.11, 3.12
  - Tests on Windows, macOS, and Linux
  - Uploads test results as artifacts

- **Lint workflow** (`.github/workflows/lint.yml`):
  - Code formatting checks (Black)
  - Import sorting (isort)
  - Linting (flake8, pylint)

## Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines.

### Quick Contributing Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and commit: `git commit -m "Add your feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Create a Pull Request

## Development

### Code Quality

Format and lint your code before committing:

```bash
# Format with Black
black .

# Sort imports with isort
isort .

# Check with flake8
flake8 .
```

### Debugging Tests

```bash
# Interactive debugging with Playwright Inspector
PWDEBUG=1 pytest test/test_orangehrm_login.py

# With headed browser
pytest --headed -v

# Generate detailed HTML report
pytest --html=report.html --self-contained-html
```

## Configuration

### pytest.ini

Configure pytest behavior, timeouts, and markers in `pytest.ini`.

### Playwright Options

Tests use pytest-playwright fixtures for automatic browser lifecycle management:

```python
def test_example(page, browser, context):
    # page: Browser tab/page
    # browser: Browser instance
    # context: Browser context (isolated)
    pass
```

## Browser Support

- Chromium (default)
- Firefox
- WebKit

Install a specific browser:
```bash
playwright install firefox
```

## Troubleshooting

### Browser Installation Issues

```bash
# Reinstall all browsers
playwright install

# Install specific browser
playwright install chromium
```

### Permission Errors (Linux/macOS)

```bash
# Install system dependencies
playwright install-deps
```

### Virtual Environment Issues

```bash
# Recreate virtual environment
deactivate
rm -rf venv1  # or rmdir venv1 on Windows
python -m venv venv1
# Activate and reinstall
```

## Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Open a [GitHub Issue](../../issues)
- Check [Contributing Guidelines](.github/CONTRIBUTING.md)
- Review [FAQ](#faq)

## FAQ

**Q: How do I run tests in headless mode?**
A: Tests run in headless mode by default. Use `pytest --headed` to see the browser.

**Q: Can I run tests on multiple browsers?**
A: Yes, modify test fixtures to specify browser type or use parameterization.

**Q: How do I take screenshots in tests?**
A: Use `page.screenshot(path="screenshot.png")` in your test code.

---

**Happy Testing! 🎭**
