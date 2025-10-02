# Cypress E2E Tests

This folder contains Cypress end-to-end tests for the JS Webshop application.

## Setup

1. Make sure you have Node.js installed
2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Tests

### Prerequisites
Before running any tests, make sure you have:

1. **JSON Server running** (for user data):
   ```bash
   npm run start:json-server
   ```
   Or manually:
   ```bash
   npx json-server --watch data/users.json --port 3000
   ```

2. **Web server running** on `http://127.0.0.1:5500` (using Live Server extension in VS Code or similar)

### Test Execution Options

#### Option 1: Run tests in headless mode (CI/CD friendly)
```bash
npm run test:cypress
```

#### Option 2: Open Cypress Test Runner (interactive)
```bash
npm run cy:open
```

#### Option 3: Run all Cypress tests headlessly
```bash
npm run cy:run
```

#### Option 4: Run specific test file
```bash
npx cypress run --spec "00_Cypress/signup-click-test.cy.js"
```

## Test Coverage

The main test file `signup-click-test.cy.js` covers:

### Main User Journey Test
1. **Signup Process**: Navigate to signup page and create account
2. **Alert Handling**: Handle "email already exists" alerts gracefully  
3. **Login Process**: Navigate to login page and authenticate
4. **Product Shopping**: Add multiple products to cart with different quantities
5. **Cart Management**: View cart, modify quantities, and verify contents
6. **Checkout Process**: Complete purchase with delivery and payment info
7. **Order Verification**: Confirm cart is empty after successful purchase
8. **Logout Process**: Sign out and verify login option appears

### Additional Test Scenarios
- **Error Handling**: Test various error conditions gracefully
- **Performance Testing**: Rapid interactions and reliability testing
- **Navigation Testing**: Page-to-page navigation verification

## Custom Commands

The test file includes several custom Cypress commands:

- `cy.loginUser(email, password)` - Quick login helper
- `cy.addProductToCart(productName, quantity)` - Add products easily
- `cy.openCart()` - Open shopping cart modal  
- `cy.closeCart()` - Close shopping cart modal

## Test Structure

The tests use Cypress's modern API features including:
- `cy.contains()` for text-based element selection
- `cy.within()` for scoped element queries
- `cy.should()` for assertions and waiting
- `cy.get().then()` for conditional logic
- `cy.scrollIntoView()` for element visibility
- `cy.trigger()` for event handling

## Debugging

If tests fail:

1. **Check Prerequisites**: Ensure both JSON server and web server are running
2. **Browser Console**: Check for JavaScript errors in the application
3. **Cypress Videos**: Review videos in `cypress/videos/` (if enabled)
4. **Screenshots**: Check failure screenshots in `cypress/screenshots/`
5. **Cypress Debug Mode**: Use `cy.debug()` or `cy.pause()` in tests

## Configuration

The test configuration is defined in `cypress.config.js`:
- Base URL: `http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/`
- Viewport: 1280x720
- Timeouts: 10 seconds default
- Video recording: Disabled (can be enabled)
- Screenshots on failure: Enabled

## Comparison with Other Testing Frameworks

This Cypress implementation provides the same functionality as:
- **Selenium WebDriver**: `00_Selenium WebDriver/signup-click-test.js`
- **Playwright**: `00_Playwright/signup-click-test.js`

All three implementations test the identical user journey but with different APIs and capabilities.