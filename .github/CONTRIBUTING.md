# Contributing to Playwright Demo

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions with other contributors and maintainers.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/playwright_demo.git
   cd playwright_demo
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv1
   # On Windows:
   .\venv1\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv1/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Running Tests Locally

```bash
# Run all tests
pytest -v

# Run specific test file
pytest test/test_orangehrm_login.py -v

# Run with headed browser (visible)
pytest --headed -v

# Run with debugging
PWDEBUG=1 pytest
```

### Code Style

This project follows PEP 8 standards. Before committing:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Check with flake8
flake8 .
```

## Making Changes

### File Structure

- `pages/` - Page Object Model (POM) implementations
- `test/` - Test files (use `test_*.py` naming)
- `utils/` - Utility functions and helpers
- `reports/` - Test reports (generated)

### Writing Tests

Follow the Page Object Model pattern:

```python
from playwright.sync_api import Page, expect
from pages.your_page import your_page_object

def test_your_feature(page: Page) -> None:
    # Initialize page object
    page_obj = your_page_object(page)
    page_obj.navigate()
    
    # Perform actions
    page_obj.do_something()
    
    # Assert expectations
    expect(page_obj.element).to_have_text("Expected text")
```

### Creating Page Objects

Create page objects in `pages/` directory:

```python
from playwright.sync_api import Page

class your_page_object:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://example.com"
        # Define locators
        self.element = page.locator("css=.element")
    
    def navigate(self):
        self.page.goto(self.url)
    
    def do_something(self):
        self.element.click()
```

## Committing Changes

- Write clear, descriptive commit messages
- Keep commits focused and atomic
- Reference issues when applicable: `Fixes #123`

Example:
```bash
git commit -m "Add login test for OrangeHRM

- Implements Page Object Model for login page
- Tests successful login with valid credentials
- Verifies dashboard is displayed after login
Fixes #42"
```

## Submitting a Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - Clear title describing the changes
   - Description of what was changed and why
   - Reference to any related issues
   - Confirmation that tests pass locally

3. **Respond to feedback** from reviewers

4. **Merge** after approval

## Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] Tests are passing (`pytest -v`)
- [ ] Code formatted with Black and isort
- [ ] No linting errors (flake8)
- [ ] New tests added for new functionality
- [ ] Documentation updated if needed
- [ ] Commit messages are clear and descriptive

## Reporting Issues

When reporting issues, include:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Test output or error messages

## Questions?

Feel free to open a discussion issue or comment on related issues.

Thank you for contributing! 🎉
