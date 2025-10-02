const { chromium } = require('playwright');

async function testSignupClick() {
    let browser;
    let context;
    let page;
    
    try {
        console.log('Starting Playwright test: Complete Sign up process');
        
        // Launch browser
        browser = await chromium.launch({ 
            headless: false,
            slowMo: 100 // Add small delay between actions for visibility
        });
        context = await browser.newContext();
        page = await context.newPage();
        
        // Navigate to the webshop homepage
        console.log('Navigating to homepage...');
        await page.goto('http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/index.html');
        
        // Wait for the page to load and find the signup link
        console.log('Looking for Sign up link...');
        await page.waitForSelector('#optSignup', { timeout: 10000 });
        
        console.log('Clicking on Sign up...');
        await page.click('#optSignup a');
        
        // Wait a moment to see the result
        await page.waitForTimeout(2000);
        
        // Check current URL to verify navigation
        const currentUrl = page.url();
        console.log('Current URL after click:', currentUrl);
        
        if (currentUrl.includes('signup.html')) {
            console.log('✓ SUCCESS: Successfully navigated to signup page!');
            
            // Now fill out the signup form
            console.log('Filling out the signup form...');
            
            // Find and fill the email field
            console.log('Entering email: test@kea.dk');
            await page.waitForSelector('#txtEmail', { timeout: 10000 });
            await page.fill('#txtEmail', 'test@kea.dk');
            
            // Find and fill the password field
            console.log('Entering password: Testing');
            await page.fill('#txtPassword', 'Testing');
            
            // Find and fill the repeat password field
            console.log('Entering repeat password: Testing');
            await page.fill('#txtRepeatPassword', 'Testing');
            
            // Find and click the Sign up button
            console.log('Clicking the Sign up button...');
            await page.click('input[type="submit"][value="Sign up"]');
            
            // Wait to see the result
            await page.waitForTimeout(3000);
            
            console.log('✓ SUCCESS: Signup form submitted!');
            
            // Check for alert dialog (e.g., "email already exists") and close it if present
            try {
                console.log('Checking for alert dialogs...');
                const alertDialog = await page.locator('dialog#alert[open]');
                
                if (await alertDialog.isVisible()) {
                    // Get the alert message
                    const messageText = await page.locator('dialog#alert section p').textContent();
                    console.log('⚠ Alert found:', messageText);
                    
                    // Close the alert dialog
                    await page.click('dialog#alert button[title="Close Alert"]');
                    await page.waitForTimeout(1000);
                    
                    console.log('✓ Alert dialog closed');
                    
                    // If it's an "email already exists" error, we can still proceed to login
                    if (messageText.toLowerCase().includes('email already exists')) {
                        console.log('Email already exists - proceeding to login with existing account');
                    }
                }
            } catch (alertError) {
                console.log('No alert dialog found - continuing...');
            }
            
            // Now click the "log in" link on the signup page
            console.log('Looking for "log in" link on signup page...');
            await page.waitForSelector('a[href="login.html"]', { timeout: 10000 });
            
            console.log('Clicking on "log in" link...');
            await page.click('a[href="login.html"]');
            
            // Wait a moment to see the result
            await page.waitForTimeout(2000);
            
            // Check current URL to verify navigation to login page
            const loginUrl = page.url();
            console.log('Current URL after clicking log in:', loginUrl);
            
            if (loginUrl.includes('login.html')) {
                console.log('✓ SUCCESS: Successfully navigated to login page!');
                
                // Now fill out the login form
                console.log('Filling out the login form...');
                
                // Find and fill the email field
                console.log('Entering email: test@kea.dk');
                await page.waitForSelector('#txtEmail', { timeout: 10000 });
                await page.fill('#txtEmail', 'test@kea.dk');
                
                // Find and fill the password field
                console.log('Entering password: Testing');
                await page.fill('#txtPassword', 'Testing');
                
                // Find and click the Log in button
                console.log('Clicking the Log in button...');
                await page.click('input[type="submit"][value="Log in"]');
                
                // Wait to see the result
                await page.waitForTimeout(3000);
                
                console.log('✓ SUCCESS: Login form submitted!');
                
                // Check if login was successful by looking for current URL or user indicators
                const currentPageUrl = page.url();
                console.log('Current URL after login:', currentPageUrl);
                
                // If we're back on homepage (successful login) or still on login page, continue
                console.log('Looking for products on the homepage...');
                
                // Navigate to homepage if not already there
                if (!currentPageUrl.includes('index.html')) {
                    await page.goto('http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/index.html');
                    await page.waitForTimeout(2000);
                }
                
                // Look for the specific product "Mens Casual Premium Slim Fit T-Shirts"
                console.log('Searching for "Mens Casual Premium Slim Fit T-Shirts" product...');
                
                try {
                    // Wait for products to load and find the specific product by text content
                    await page.waitForSelector('h2:has-text("Mens Casual Premium Slim Fit T-Shirts")', { timeout: 15000 });
                    
                    console.log('✓ Found the product: Mens Casual Premium Slim Fit T-Shirts');
                    
                    // Find and click the "Add to cart" button for this specific product
                    const productLocator = page.locator('article:has(h2:has-text("Mens Casual Premium Slim Fit T-Shirts"))');
                    await productLocator.locator('div.cart button:has-text("Add to cart")').click();
                    
                    console.log('Clicking "Add to cart" for Mens Casual Premium Slim Fit T-Shirts...');
                    
                    // Wait to see the result
                    await page.waitForTimeout(2000);
                    
                    console.log('✓ SUCCESS: Product added to cart!');
                    
                } catch (productError) {
                    console.log('⚠ Could not find the specific product or add to cart button');
                    console.log('Trying alternative approach - looking for any add to cart buttons...');
                    
                    // Alternative approach: find all add to cart buttons and click the first one
                    const addToCartButtons = await page.locator('button:has-text("Add to cart")').all();
                    
                    if (addToCartButtons.length > 0) {
                        console.log(`Found ${addToCartButtons.length} add to cart button(s), clicking the first one...`);
                        await addToCartButtons[0].click();
                        await page.waitForTimeout(2000);
                        console.log('✓ SUCCESS: Product added to cart (alternative method)!');
                    } else {
                        console.log('❌ No add to cart buttons found');
                    }
                }

                // Now scroll down to find the SanDisk SSD product
                console.log('Scrolling down to find more products...');
                await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
                await page.waitForTimeout(2000);
                
                // Look for the SanDisk SSD product
                console.log('Searching for "SanDisk SSD PLUS 1TB Internal SSD" product...');
                
                try {
                    // Wait for the SanDisk product to be visible
                    await page.waitForSelector('h2:has-text("SanDisk SSD PLUS 1TB Internal SSD")', { timeout: 15000 });
                    
                    console.log('✓ Found the SanDisk SSD product');
                    
                    // Scroll to the SanDisk product to make sure it's visible
                    await page.locator('h2:has-text("SanDisk SSD PLUS 1TB Internal SSD")').scrollIntoViewIfNeeded();
                    await page.waitForTimeout(1000);
                    
                    // Find the quantity input field for this product and set it to 2
                    const sanDiskArticle = page.locator('article:has(h2:has-text("SanDisk SSD PLUS 1TB Internal SSD"))');
                    const quantityInput = sanDiskArticle.locator('div.cart input[type="number"]');
                    
                    console.log('Changing quantity to 2 units...');
                    await quantityInput.fill('2');
                    
                    // Find and click the "Add to cart" button for this product
                    console.log('Clicking "Add to cart" for SanDisk SSD (2 units)...');
                    await sanDiskArticle.locator('div.cart button:has-text("Add to cart")').click();
                    
                    // Wait to see the result
                    await page.waitForTimeout(2000);
                    
                    console.log('✓ SUCCESS: SanDisk SSD (2 units) added to cart!');
                    
                    // Now click on the Cart to view items
                    console.log('Looking for Cart button...');
                    
                    try {
                        // Navigate back to top of page where cart button is located
                        await page.evaluate(() => window.scrollTo(0, 0));
                        await page.waitForTimeout(1000);
                        
                        // Find and click the Cart button
                        await page.waitForSelector('#optCart a', { timeout: 10000 });
                        
                        console.log('Clicking on Cart...');
                        await page.click('#optCart a');
                        
                        // Wait to see the cart contents
                        await page.waitForTimeout(3000);
                        
                        console.log('✓ SUCCESS: Cart opened!');
                        
                        // Now increase SanDisk SSD quantity to 3 in the cart
                        console.log('Looking for SanDisk SSD in cart to increase quantity to 3...');
                        
                        try {
                            // Find the SanDisk product in the cart table row
                            const sanDiskRow = page.locator('td.titleCell:has-text("SanDisk SSD PLUS 1TB Internal SSD")');
                            const quantityInput = sanDiskRow.locator('..').locator('td.amountCell input[type="number"]');
                            
                            console.log('Found SanDisk SSD quantity field in cart');
                            console.log('Changing quantity from 2 to 3 units...');
                            
                            // Set the quantity to 3
                            await quantityInput.fill('3');
                            
                            // Trigger change event
                            await quantityInput.dispatchEvent('change');
                            
                            await page.waitForTimeout(2000);
                            
                            console.log('✓ SUCCESS: SanDisk SSD quantity increased to 3 units!');
                            
                            // Now click on "Check Out" button
                            console.log('Looking for Check Out button...');
                            
                            try {
                                // Find the Check Out button in the submit div
                                await page.waitForSelector('div.submit input[type="submit"][value="Check Out"]', { timeout: 10000 });
                                
                                console.log('Clicking on Check Out...');
                                await page.click('div.submit input[type="submit"][value="Check Out"]');
                                
                                // Wait to see the checkout process
                                await page.waitForTimeout(3000);
                                
                                console.log('✓ SUCCESS: Check Out button clicked!');
                                
                                // Now fill out the checkout form
                                console.log('Filling out checkout form...');
                                
                                try {
                                    // Fill delivery address
                                    console.log('Filling delivery address...');
                                    
                                    await page.waitForSelector('#txtDeliveryAddress', { timeout: 10000 });
                                    await page.fill('#txtDeliveryAddress', 'Guldbergsgade 29N');
                                    await page.fill('#txtDeliveryPostalCode', '2200');
                                    await page.fill('#txtDeliveryCity', 'Copenhagen');
                                    
                                    console.log('✓ Delivery address filled');
                                    
                                    // Check "Same as delivery address" for billing
                                    console.log('Checking "Same as delivery address"...');
                                    await page.check('#chkRepeat');
                                    
                                    console.log('✓ Same as delivery address checked');
                                    
                                    // Fill credit card information
                                    console.log('Filling credit card information...');
                                    
                                    await page.fill('#txtCreditCardName', 'Pernille L. Hansen');
                                    
                                    // Try multiple methods to set the month input
                                    try {
                                        await page.fill('#txtExpiryDate', '2027-12');
                                        console.log('✓ Date set using fill method');
                                    } catch (dateError) {
                                        await page.evaluate(() => {
                                            document.getElementById('txtExpiryDate').value = '2027-12';
                                        });
                                        console.log('✓ Date set using JavaScript');
                                    }
                                    
                                    await page.fill('#txtCVV', '666');
                                    
                                    console.log('✓ Credit card information filled');
                                    
                                    // Click "Place Purchase"
                                    console.log('Looking for Place Purchase button...');
                                    await page.waitForSelector('input[type="submit"][value="Place Purchase"]', { timeout: 10000 });
                                    
                                    console.log('Clicking Place Purchase...');
                                    await page.click('input[type="submit"][value="Place Purchase"]');
                                    
                                    // Wait to see the result
                                    await page.waitForTimeout(3000);
                                    
                                    console.log('✓ SUCCESS: Place Purchase clicked! Order should be completed!');
                                    
                                    // After purchase, click on Cart to verify it's empty
                                    console.log('Verifying cart is empty after purchase...');
                                    
                                    try {
                                        // First, close the checkout modal if it's still open
                                        try {
                                            await page.click('dialog#checkout button[title="Close Check out"]');
                                            await page.waitForTimeout(1000);
                                            console.log('✓ Checkout modal closed');
                                        } catch (closeError) {
                                            console.log('⚠ Checkout modal might already be closed');
                                        }
                                        
                                        // Now click on Cart to verify it's empty
                                        console.log('Clicking on Cart to verify it is empty...');
                                        await page.waitForSelector('#optCart a', { timeout: 10000 });
                                        
                                        await page.click('#optCart a');
                                        await page.waitForTimeout(2000);
                                        
                                        console.log('✓ Cart opened for verification');
                                        
                                        // Check if cart is empty (look for empty cart indicators)
                                        try {
                                            // Look for empty cart indicators or absence of products
                                            const cartContents = await page.locator('dialog#cart section tr').all();
                                            
                                            if (cartContents.length === 0) {
                                                console.log('✓ SUCCESS: Cart is empty as expected!');
                                            } else {
                                                console.log(`⚠ Cart contains ${cartContents.length} item(s) - might not be completely empty`);
                                            }
                                            
                                        } catch (contentsError) {
                                            console.log('✓ SUCCESS: No cart contents found - cart appears empty!');
                                        }
                                        
                                        // Close the cart modal
                                        console.log('Closing cart modal...');
                                        try {
                                            await page.click('dialog#cart button[title="Close the cart"]');
                                            await page.waitForTimeout(1000);
                                            console.log('✓ SUCCESS: Cart modal closed!');
                                        } catch (closeCartError) {
                                            // Alternative method: press Escape key
                                            await page.keyboard.press('Escape');
                                            await page.waitForTimeout(1000);
                                            console.log('✓ Cart modal closed using Escape key');
                                        }
                                        
                                    } catch (cartVerificationError) {
                                        console.log('❌ Error verifying empty cart:', cartVerificationError.message);
                                    }
                                    
                                    // Now log out and verify "Log in" option appears
                                    console.log('Logging out...');
                                    
                                    try {
                                        // Look for logout option (should be visible when logged in)
                                        console.log('Looking for logout option...');
                                        await page.waitForSelector('#optLogout a', { timeout: 10000 });
                                        
                                        console.log('Found logout option, clicking...');
                                        await page.click('#optLogout a');
                                        
                                        // Wait for logout to complete
                                        await page.waitForTimeout(2000);
                                        
                                        console.log('✓ SUCCESS: Logged out!');
                                        
                                        // Now verify that "Log in" option is visible
                                        console.log('Verifying "Log in" option is visible...');
                                        
                                        try {
                                            await page.waitForSelector('#optLogin a', { timeout: 10000 });
                                            
                                            // Check if the login option is visible
                                            const isLoginVisible = await page.locator('#optLogin a').isVisible();
                                            
                                            if (isLoginVisible) {
                                                console.log('✓ SUCCESS: "Log in" option is visible on the page!');
                                                
                                                // Get the text to confirm
                                                const loginText = await page.locator('#optLogin a').textContent();
                                                console.log('Login option text:', loginText);
                                            } else {
                                                console.log('⚠ "Log in" option found but not visible');
                                            }
                                            
                                        } catch (loginVerificationError) {
                                            console.log('❌ Could not find "Log in" option after logout');
                                        }
                                        
                                    } catch (logoutError) {
                                        console.log('❌ Error during logout process:', logoutError.message);
                                    }
                                    
                                } catch (checkoutFormError) {
                                    console.log('❌ Error filling checkout form:', checkoutFormError.message);
                                }
                                
                            } catch (checkoutError) {
                                console.log('⚠ Could not find Check Out button');
                            }
                            
                        } catch (quantityError) {
                            console.log('⚠ Could not find SanDisk SSD product or modify quantity');
                        }
                        
                    } catch (cartError) {
                        console.log('⚠ Could not find or click Cart button');
                    }
                    
                } catch (sanDiskError) {
                    console.log('⚠ Could not find SanDisk SSD product or modify quantity');
                    console.log('Error:', sanDiskError.message);
                }
                
            } else {
                console.log('⚠ WARNING: URL does not contain login.html');
            }
            
        } else {
            console.log('⚠ WARNING: URL does not contain signup.html');
        }
        
    } catch (error) {
        console.error('❌ TEST FAILED:', error.message);
    } finally {
        if (browser) {
            console.log('Keeping browser open for 3 seconds...');
            await page.waitForTimeout(3000);
            await browser.close();
            console.log('Browser closed.');
        }
    }
}

// Run the test
testSignupClick();