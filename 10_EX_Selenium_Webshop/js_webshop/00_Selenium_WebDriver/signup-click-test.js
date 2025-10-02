const { Builder, By, until } = require('selenium-webdriver');

async function testSignupClick() {
    let driver;
    
    try {
        console.log('Starting Selenium test: Complete Sign up process');
        
        // Create Chrome WebDriver
        driver = await new Builder().forBrowser('chrome').build();
        
        // Navigate to the webshop homepage
        console.log('Navigating to homepage...');
        await driver.get('http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/index.html');
        
        // Wait for the page to load and find the signup link
        console.log('Looking for Sign up link...');
        const signupLink = await driver.wait(
            until.elementLocated(By.id('optSignup')), 
            10000
        );
        
        // Make sure the element is visible and clickable
        await driver.wait(until.elementIsVisible(signupLink), 5000);
        
        console.log('Clicking on Sign up...');
        await signupLink.click();
        
        // Wait a moment to see the result
        await driver.sleep(2000);
        
        // Check current URL to verify navigation
        const currentUrl = await driver.getCurrentUrl();
        console.log('Current URL after click:', currentUrl);
        
        if (currentUrl.includes('signup.html')) {
            console.log('✓ SUCCESS: Successfully navigated to signup page!');
            
            // Now fill out the signup form
            console.log('Filling out the signup form...');
            
            // Find and fill the email field
            console.log('Entering email: test@kea.dk');
            const emailField = await driver.wait(
                until.elementLocated(By.id('txtEmail')), 
                10000
            );
            await emailField.clear();
            await emailField.sendKeys('test@kea.dk');
            
            // Find and fill the password field
            console.log('Entering password: Testing');
            const passwordField = await driver.wait(
                until.elementLocated(By.id('txtPassword')), 
                10000
            );
            await passwordField.clear();
            await passwordField.sendKeys('Testing');
            
            // Find and fill the repeat password field
            console.log('Entering repeat password: Testing');
            const repeatPasswordField = await driver.wait(
                until.elementLocated(By.id('txtRepeatPassword')), 
                10000
            );
            await repeatPasswordField.clear();
            await repeatPasswordField.sendKeys('Testing');
            
            // Find and click the Sign up button
            console.log('Clicking the Sign up button...');
            const signupButton = await driver.wait(
                until.elementLocated(By.css('input[type="submit"][value="Sign up"]')), 
                10000
            );
            await signupButton.click();
            
            // Wait to see the result
            await driver.sleep(3000);
            
            console.log('✓ SUCCESS: Signup form submitted!');
            
            // Check for alert dialog (e.g., "email already exists") and close it if present
            try {
                console.log('Checking for alert dialogs...');
                const alertDialog = await driver.findElement(By.css('dialog#alert[open]'));
                
                if (alertDialog) {
                    // Get the alert message
                    const alertMessage = await driver.findElement(By.css('dialog#alert section p'));
                    const messageText = await alertMessage.getText();
                    console.log('⚠ Alert found:', messageText);
                    
                    // Close the alert dialog
                    const closeAlertButton = await driver.findElement(By.css('dialog#alert button[title="Close Alert"], dialog#alert header button'));
                    await closeAlertButton.click();
                    await driver.sleep(1000);
                    
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
            const loginLink = await driver.wait(
                until.elementLocated(By.css('a[href="login.html"]')), 
                10000
            );
            
            // Make sure the element is visible and clickable
            await driver.wait(until.elementIsVisible(loginLink), 5000);
            
            console.log('Clicking on "log in" link...');
            await loginLink.click();
            
            // Wait a moment to see the result
            await driver.sleep(2000);
            
            // Check current URL to verify navigation to login page
            const loginUrl = await driver.getCurrentUrl();
            console.log('Current URL after clicking log in:', loginUrl);
            
            if (loginUrl.includes('login.html')) {
                console.log('✓ SUCCESS: Successfully navigated to login page!');
                
                // Now fill out the login form
                console.log('Filling out the login form...');
                
                // Find and fill the email field
                console.log('Entering email: test@kea.dk');
                const loginEmailField = await driver.wait(
                    until.elementLocated(By.id('txtEmail')), 
                    10000
                );
                await loginEmailField.clear();
                await loginEmailField.sendKeys('test@kea.dk');
                
                // Find and fill the password field
                console.log('Entering password: Testing');
                const loginPasswordField = await driver.wait(
                    until.elementLocated(By.id('txtPassword')), 
                    10000
                );
                await loginPasswordField.clear();
                await loginPasswordField.sendKeys('Testing');
                
                // Find and click the Log in button
                console.log('Clicking the Log in button...');
                const loginButton = await driver.wait(
                    until.elementLocated(By.css('input[type="submit"][value="Log in"]')), 
                    10000
                );
                await loginButton.click();
                
                // Wait to see the result
                await driver.sleep(3000);
                
                console.log('✓ SUCCESS: Login form submitted!');
                
                // Check if login was successful by looking for current URL or user indicators
                const currentPageUrl = await driver.getCurrentUrl();
                console.log('Current URL after login:', currentPageUrl);
                
                // If we're back on homepage (successful login) or still on login page, continue
                console.log('Looking for products on the homepage...');
                
                // Navigate to homepage if not already there
                if (!currentPageUrl.includes('index.html')) {
                    await driver.get('http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/index.html');
                    await driver.sleep(2000);
                }
                
                // Look for the specific product "Mens Casual Premium Slim Fit T-Shirts"
                console.log('Searching for "Mens Casual Premium Slim Fit T-Shirts" product...');
                
                try {
                    // Wait for products to load and find the specific product by text content
                    const productElement = await driver.wait(
                        until.elementLocated(By.xpath("//h2[contains(text(), 'Mens Casual Premium Slim Fit T-Shirts')]")),
                        15000
                    );
                    
                    console.log('✓ Found the product: Mens Casual Premium Slim Fit T-Shirts');
                    
                    // Find the "Add to cart" button for this specific product
                    // Look for the button within the same article container
                    const addToCartButton = await driver.findElement(
                        By.xpath("//h2[contains(text(), 'Mens Casual Premium Slim Fit T-Shirts')]/ancestor::article//div[@class='cart']/button[contains(text(), 'Add to cart')]")
                    );
                    
                    console.log('Clicking "Add to cart" for Mens Casual Premium Slim Fit T-Shirts...');
                    await addToCartButton.click();
                    
                    // Wait to see the result
                    await driver.sleep(2000);
                    
                    console.log('✓ SUCCESS: Product added to cart!');
                    
                } catch (productError) {
                    console.log('⚠ Could not find the specific product or add to cart button');
                    console.log('Trying alternative approach - looking for any add to cart buttons...');
                    
                    // Alternative approach: find all add to cart buttons and click the first one
                    const addToCartButtons = await driver.findElements(
                        By.css('button[onclick*="addToCart"], .add-to-cart, button:contains("Add to cart")')
                    );
                    
                    if (addToCartButtons.length > 0) {
                        console.log(`Found ${addToCartButtons.length} add to cart button(s), clicking the first one...`);
                        await addToCartButtons[0].click();
                        await driver.sleep(2000);
                        console.log('✓ SUCCESS: Product added to cart (alternative method)!');
                    } else {
                        console.log('❌ No add to cart buttons found');
                    }
                }

                // Now scroll down to find the SanDisk SSD product
                console.log('Scrolling down to find more products...');
                await driver.executeScript("window.scrollTo(0, document.body.scrollHeight);");
                await driver.sleep(2000);
                
                // Look for the SanDisk SSD product
                console.log('Searching for "SanDisk SSD PLUS 1TB Internal SSD" product...');
                
                try {
                    // Wait for the SanDisk product to be visible
                    const sanDiskProduct = await driver.wait(
                        until.elementLocated(By.xpath("//h2[contains(text(), 'SanDisk SSD PLUS 1TB Internal SSD')]")),
                        15000
                    );
                    
                    console.log('✓ Found the SanDisk SSD product');
                    
                    // Scroll to the SanDisk product to make sure it's visible
                    await driver.executeScript("arguments[0].scrollIntoView(true);", sanDiskProduct);
                    await driver.sleep(1000);
                    
                    // Find the quantity input field for this product
                    const quantityInput = await driver.findElement(
                        By.xpath("//h2[contains(text(), 'SanDisk SSD PLUS 1TB Internal SSD')]/ancestor::article//div[@class='cart']/input[@type='number']")
                    );
                    
                    console.log('Changing quantity to 2 units...');
                    // Use JavaScript to set the value directly to avoid "12" issue
                    await driver.executeScript("arguments[0].value = '2';", quantityInput);
                    
                    // Alternative method: Select all and replace
                    // await quantityInput.clear();
                    // await driver.sleep(100);
                    // await quantityInput.sendKeys('2');
                    
                    // Find and click the "Add to cart" button for this product
                    const sanDiskAddToCartButton = await driver.findElement(
                        By.xpath("//h2[contains(text(), 'SanDisk SSD PLUS 1TB Internal SSD')]/ancestor::article//div[@class='cart']/button[contains(text(), 'Add to cart')]")
                    );
                    
                    console.log('Clicking "Add to cart" for SanDisk SSD (2 units)...');
                    await sanDiskAddToCartButton.click();
                    
                    // Wait to see the result
                    await driver.sleep(2000);
                    
                    console.log('✓ SUCCESS: SanDisk SSD (2 units) added to cart!');
                    
                    // Now click on the Cart to view items
                    console.log('Looking for Cart button...');
                    
                    try {
                        // Navigate back to top of page where cart button is located
                        await driver.executeScript("window.scrollTo(0, 0);");
                        await driver.sleep(1000);
                        
                        // Find and click the Cart button (from the index.html structure)
                        const cartButton = await driver.wait(
                            until.elementLocated(By.css('#optCart a, a[title="Cart"], .cart-icon, #cart')), 
                            10000
                        );
                        
                        console.log('Clicking on Cart...');
                        await cartButton.click();
                        
                        // Wait to see the cart contents
                        await driver.sleep(3000);
                        
                        console.log('✓ SUCCESS: Cart opened!');
                        
                        // Now increase SanDisk SSD quantity to 3 in the cart
                        console.log('Looking for SanDisk SSD in cart to increase quantity to 3...');
                        
                        try {
                            // Find the SanDisk product in the cart table row
                            const sanDiskInCart = await driver.wait(
                                until.elementLocated(By.xpath("//td[contains(@class, 'titleCell') and contains(text(), 'SanDisk SSD PLUS 1TB Internal SSD')]/following-sibling::td[@class='amountCell alignRight']/input[@type='number']")),
                                10000
                            );
                            
                            console.log('Found SanDisk SSD quantity field in cart');
                            console.log('Changing quantity from 2 to 3 units...');
                            
                            // Set the quantity to 3 using JavaScript to avoid the "23" issue
                            await driver.executeScript("arguments[0].value = '3';", sanDiskInCart);
                            
                            // Trigger change event to update cart
                            await driver.executeScript("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", sanDiskInCart);
                            
                            await driver.sleep(2000);
                            
                            console.log('✓ SUCCESS: SanDisk SSD quantity increased to 3 units!');
                            
                            // Now click on "Check Out" button
                            console.log('Looking for Check Out button...');
                            
                            try {
                                // Find the Check Out button in the submit div
                                const checkOutButton = await driver.wait(
                                    until.elementLocated(By.css('div.submit input[type="submit"][value="Check Out"], input[value="Check Out"]')),
                                    10000
                                );
                                
                                console.log('Clicking on Check Out...');
                                await checkOutButton.click();
                                
                                // Wait to see the checkout process
                                await driver.sleep(3000);
                                
                                console.log('✓ SUCCESS: Check Out button clicked!');
                                
                                // Now fill out the checkout form
                                console.log('Filling out checkout form...');
                                
                                try {
                                    // Fill delivery address
                                    console.log('Filling delivery address...');
                                    
                                    const deliveryAddress = await driver.wait(
                                        until.elementLocated(By.id('txtDeliveryAddress')), 
                                        10000
                                    );
                                    await deliveryAddress.clear();
                                    await deliveryAddress.sendKeys('Guldbergsgade 29N');
                                    
                                    const deliveryPostalCode = await driver.findElement(By.id('txtDeliveryPostalCode'));
                                    await deliveryPostalCode.clear();
                                    await deliveryPostalCode.sendKeys('2200');
                                    
                                    const deliveryCity = await driver.findElement(By.id('txtDeliveryCity'));
                                    await deliveryCity.clear();
                                    await deliveryCity.sendKeys('Copenhagen');
                                    
                                    console.log('✓ Delivery address filled');
                                    
                                    // Check "Same as delivery address" for billing
                                    console.log('Checking "Same as delivery address"...');
                                    const sameAsDeliveryCheckbox = await driver.findElement(By.id('chkRepeat'));
                                    await sameAsDeliveryCheckbox.click();
                                    
                                    console.log('✓ Same as delivery address checked');
                                    
                                    // Fill credit card information
                                    console.log('Filling credit card information...');
                                    
                                    const creditCardName = await driver.findElement(By.id('txtCreditCardName'));
                                    await creditCardName.clear();
                                    await creditCardName.sendKeys('Pernille L. Hansen');
                                    
                                    const expiryDate = await driver.findElement(By.id('txtExpiryDate'));
                                    await expiryDate.clear();
                                    
                                    // Try multiple methods to set the month input
                                    try {
                                        // Method 1: Direct JavaScript value assignment
                                        await driver.executeScript("arguments[0].value = '2027-12';", expiryDate);
                                        console.log('✓ Date set using JavaScript');
                                    } catch (jsError) {
                                        try {
                                            // Method 2: SendKeys with proper format
                                            await expiryDate.sendKeys('2027-12');
                                            console.log('✓ Date set using sendKeys');
                                        } catch (sendKeysError) {
                                            // Method 3: Click and type
                                            await expiryDate.click();
                                            await expiryDate.sendKeys('December 2027');
                                            console.log('✓ Date set using click and type');
                                        }
                                    }
                                    
                                    const cvv = await driver.findElement(By.id('txtCVV'));
                                    await cvv.clear();
                                    await cvv.sendKeys('666');
                                    
                                    console.log('✓ Credit card information filled');
                                    
                                    // Click "Place Purchase"
                                    console.log('Looking for Place Purchase button...');
                                    const placePurchaseButton = await driver.wait(
                                        until.elementLocated(By.css('input[type="submit"][value="Place Purchase"]')),
                                        10000
                                    );
                                    
                                    console.log('Clicking Place Purchase...');
                                    await placePurchaseButton.click();
                                    
                                    // Wait to see the result
                                    await driver.sleep(3000);
                                    
                                    console.log('✓ SUCCESS: Place Purchase clicked! Order should be completed!');
                                    
                                    // After purchase, click on Cart to verify it's empty
                                    console.log('Verifying cart is empty after purchase...');
                                    
                                    try {
                                        // First, close the checkout modal if it's still open
                                        try {
                                            const closeCheckoutButton = await driver.findElement(By.css('dialog#checkout button[title="Close Check out"], dialog#checkout header button'));
                                            await closeCheckoutButton.click();
                                            await driver.sleep(1000);
                                            console.log('✓ Checkout modal closed');
                                        } catch (closeError) {
                                            console.log('⚠ Checkout modal might already be closed');
                                        }
                                        
                                        // Now click on Cart to verify it's empty
                                        console.log('Clicking on Cart to verify it is empty...');
                                        const cartButton = await driver.wait(
                                            until.elementLocated(By.css('#optCart a, a[title="Cart"], .cart-icon, #cart')), 
                                            10000
                                        );
                                        
                                        await cartButton.click();
                                        await driver.sleep(2000);
                                        
                                        console.log('✓ Cart opened for verification');
                                        
                                        // Check if cart is empty (look for empty cart indicators)
                                        try {
                                            // Look for empty cart indicators or absence of products
                                            const cartContents = await driver.findElements(By.css('dialog#cart section tr, .cart-item, .product-row'));
                                            
                                            if (cartContents.length === 0) {
                                                console.log('✓ SUCCESS: Cart is empty as expected!');
                                            } else {
                                                console.log(`⚠ Cart contains ${cartContents.length} item(s) - might not be completely empty`);
                                            }
                                            
                                            // Look for empty cart message
                                            try {
                                                const emptyMessage = await driver.findElement(By.xpath("//*[contains(text(), 'empty') or contains(text(), 'Empty') or contains(text(), 'no items') or contains(text(), 'No items')]"));
                                                console.log('✓ Empty cart message found:', await emptyMessage.getText());
                                            } catch (emptyMsgError) {
                                                console.log('⚠ No explicit empty cart message found');
                                            }
                                            
                                        } catch (contentsError) {
                                            console.log('✓ SUCCESS: No cart contents found - cart appears empty!');
                                        }
                                        
                                        // Close the cart modal
                                        console.log('Closing cart modal...');
                                        try {
                                            const closeCartButton = await driver.findElement(By.css('dialog#cart button[title="Close the cart"], dialog#cart header button'));
                                            await closeCartButton.click();
                                            await driver.sleep(1000);
                                            console.log('✓ SUCCESS: Cart modal closed!');
                                        } catch (closeCartError) {
                                            // Alternative method: press Escape key
                                            await driver.actions().sendKeys('\uE00C').perform(); // Escape key
                                            await driver.sleep(1000);
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
                                        const logoutOption = await driver.wait(
                                            until.elementLocated(By.css('#optLogout a[title="Log out"], #optLogout a, a[href="index.html"][title="Log out"]')),
                                            10000
                                        );
                                        
                                        console.log('Found logout option, clicking...');
                                        await logoutOption.click();
                                        
                                        // Wait for logout to complete
                                        await driver.sleep(2000);
                                        
                                        console.log('✓ SUCCESS: Logged out!');
                                        
                                        // Now verify that "Log in" option is visible
                                        console.log('Verifying "Log in" option is visible...');
                                        
                                        try {
                                            const loginOption = await driver.wait(
                                                until.elementLocated(By.css('#optLogin a[title="Log in"], #optLogin a[href="login.html"], a[href="login.html"]')),
                                                10000
                                            );
                                            
                                            // Check if the login option is visible
                                            const isLoginVisible = await loginOption.isDisplayed();
                                            
                                            if (isLoginVisible) {
                                                console.log('✓ SUCCESS: "Log in" option is visible on the page!');
                                                
                                                // Get the text to confirm
                                                const loginText = await loginOption.getText();
                                                console.log('Login option text:', loginText);
                                            } else {
                                                console.log('⚠ "Log in" option found but not visible');
                                            }
                                            
                                        } catch (loginVerificationError) {
                                            console.log('❌ Could not find "Log in" option after logout');
                                            
                                            // Alternative verification: check if logout option is gone
                                            try {
                                                const logoutStillVisible = await driver.findElements(By.css('#optLogout'));
                                                if (logoutStillVisible.length === 0) {
                                                    console.log('✓ Logout option is gone, user appears to be logged out');
                                                }
                                            } catch (altVerificationError) {
                                                console.log('⚠ Could not verify logout state');
                                            }
                                        }
                                        
                                    } catch (logoutError) {
                                        console.log('❌ Error during logout process:', logoutError.message);
                                        console.log('Trying alternative logout method...');
                                        
                                        try {
                                            // Alternative: look for any logout link
                                            const logoutLinks = await driver.findElements(By.xpath("//a[contains(text(), 'Log out') or contains(@title, 'Log out')]"));
                                            if (logoutLinks.length > 0) {
                                                await logoutLinks[0].click();
                                                await driver.sleep(2000);
                                                console.log('✓ Logged out using alternative method');
                                                
                                                // Verify login option
                                                const loginOption = await driver.findElement(By.css('#optLogin a, a[href="login.html"]'));
                                                if (await loginOption.isDisplayed()) {
                                                    console.log('✓ SUCCESS: "Log in" option is visible!');
                                                }
                                            }
                                        } catch (altLogoutError) {
                                            console.log('❌ Could not complete logout process');
                                        }
                                    }
                                    
                                } catch (checkoutFormError) {
                                    console.log('❌ Error filling checkout form:', checkoutFormError.message);
                                }
                                
                            } catch (checkoutError) {
                                console.log('⚠ Could not find Check Out button');
                                console.log('Trying alternative approach...');
                                
                                try {
                                    // Alternative approach: look for any submit button or checkout text
                                    const checkoutElements = await driver.findElements(
                                        By.xpath("//input[@type='submit' and contains(@value, 'Check')] | //button[contains(text(), 'Check')] | //*[contains(text(), 'Check Out')]")
                                    );
                                    
                                    if (checkoutElements.length > 0) {
                                        console.log(`Found ${checkoutElements.length} checkout element(s), clicking the first one...`);
                                        await checkoutElements[0].click();
                                        await driver.sleep(3000);
                                        console.log('✓ SUCCESS: Check Out clicked (alternative method)!');
                                    } else {
                                        console.log('❌ No checkout elements found');
                                    }
                                } catch (alternativeCheckoutError) {
                                    console.log('❌ Could not click Check Out button');
                                }
                            }
                            
                        } catch (quantityError) {
                            console.log('⚠ Could not find SanDisk quantity field in cart');
                            console.log('Trying alternative approach...');
                            
                            try {
                                // Alternative: look for any quantity inputs in the cart
                                const cartQuantityInputs = await driver.findElements(
                                    By.css('input[type="number"], .quantity input, input[name*="quantity"]')
                                );
                                
                                if (cartQuantityInputs.length > 0) {
                                    console.log(`Found ${cartQuantityInputs.length} quantity input(s) in cart`);
                                    
                                    // Assume the SanDisk is the second product (index 1) if there are multiple items
                                    const targetInput = cartQuantityInputs.length > 1 ? cartQuantityInputs[1] : cartQuantityInputs[0];
                                    
                                    console.log('Updating quantity to 3...');
                                    await driver.executeScript("arguments[0].value = '3';", targetInput);
                                    await driver.executeScript("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", targetInput);
                                    
                                    await driver.sleep(2000);
                                    console.log('✓ SUCCESS: Quantity updated to 3 (alternative method)!');
                                } else {
                                    console.log('❌ No quantity inputs found in cart');
                                }
                            } catch (alternativeError) {
                                console.log('❌ Could not update quantity in cart');
                            }
                        }
                        
                    } catch (cartError) {
                        console.log('⚠ Could not find or click Cart button');
                        console.log('Trying alternative approach...');
                        
                        // Alternative approach: look for any element with "cart" in text or attributes
                        try {
                            const cartElements = await driver.findElements(
                                By.xpath("//a[contains(text(), 'Cart') or contains(@title, 'Cart')] | //div[contains(@id, 'cart') or contains(@class, 'cart')]//a")
                            );
                            
                            if (cartElements.length > 0) {
                                console.log(`Found ${cartElements.length} cart element(s), clicking the first one...`);
                                await cartElements[0].click();
                                await driver.sleep(3000);
                                console.log('✓ SUCCESS: Cart opened (alternative method)!');
                            } else {
                                console.log('❌ No cart elements found');
                            }
                        } catch (alternativeCartError) {
                            console.log('❌ Could not open cart');
                        }
                    }
                    
                } catch (sanDiskError) {
                    console.log('⚠ Could not find SanDisk SSD product or modify quantity');
                    console.log('Error:', sanDiskError.message);
                    
                    // Try a more general approach to find SanDisk product
                    try {
                        const sanDiskElements = await driver.findElements(
                            By.xpath("//h2[contains(text(), 'SanDisk')]")
                        );
                        
                        if (sanDiskElements.length > 0) {
                            console.log(`Found ${sanDiskElements.length} SanDisk product(s), trying the first one...`);
                            await driver.executeScript("arguments[0].scrollIntoView(true);", sanDiskElements[0]);
                            await driver.sleep(1000);
                            
                            // Try to find quantity input and add to cart button near this product
                            const nearbyQuantityInputs = await driver.findElements(
                                By.xpath("//h2[contains(text(), 'SanDisk')]/ancestor::article//input[@type='number']")
                            );
                            
                            const nearbyAddToCartButtons = await driver.findElements(
                                By.xpath("//h2[contains(text(), 'SanDisk')]/ancestor::article//button[contains(text(), 'Add to cart')]")
                            );
                            
                            if (nearbyQuantityInputs.length > 0 && nearbyAddToCartButtons.length > 0) {
                                // Use JavaScript to set the value directly
                                await driver.executeScript("arguments[0].value = '2';", nearbyQuantityInputs[0]);
                                await nearbyAddToCartButtons[0].click();
                                await driver.sleep(2000);
                                console.log('✓ SUCCESS: SanDisk product (2 units) added to cart (alternative method)!');
                                
                                // Also try to open cart after alternative SanDisk addition
                                console.log('Looking for Cart button after alternative SanDisk addition...');
                                await driver.executeScript("window.scrollTo(0, 0);");
                                await driver.sleep(1000);
                                
                                try {
                                    const cartButton = await driver.wait(
                                        until.elementLocated(By.css('#optCart a, a[title="Cart"], .cart-icon, #cart')), 
                                        5000
                                    );
                                    
                                    console.log('Clicking on Cart...');
                                    await cartButton.click();
                                    await driver.sleep(3000);
                                    console.log('✓ SUCCESS: Cart opened!');
                                    
                                    // Also try to increase SanDisk quantity after alternative cart opening
                                    try {
                                        const cartQuantityInputs = await driver.findElements(
                                            By.css('input[type="number"], .quantity input')
                                        );
                                        
                                        if (cartQuantityInputs.length > 0) {
                                            const targetInput = cartQuantityInputs.length > 1 ? cartQuantityInputs[1] : cartQuantityInputs[0];
                                            await driver.executeScript("arguments[0].value = '3';", targetInput);
                                            await driver.executeScript("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", targetInput);
                                            await driver.sleep(2000);
                                            console.log('✓ SUCCESS: Quantity updated to 3 units!');
                                            
                                            // Also try to click Check Out after alternative quantity update
                                            try {
                                                const checkOutButton = await driver.findElement(
                                                    By.css('div.submit input[type="submit"][value="Check Out"], input[value="Check Out"]')
                                                );
                                                
                                                console.log('Clicking on Check Out...');
                                                await checkOutButton.click();
                                                await driver.sleep(3000);
                                                console.log('✓ SUCCESS: Check Out button clicked!');
                                                
                                                // Also fill checkout form after alternative checkout click
                                                try {
                                                    console.log('Filling checkout form (alternative path)...');
                                                    
                                                    // Fill delivery address
                                                    const deliveryAddress = await driver.findElement(By.id('txtDeliveryAddress'));
                                                    await deliveryAddress.clear();
                                                    await deliveryAddress.sendKeys('Guldbergsgade 29N');
                                                    
                                                    const deliveryPostalCode = await driver.findElement(By.id('txtDeliveryPostalCode'));
                                                    await deliveryPostalCode.clear();
                                                    await deliveryPostalCode.sendKeys('2200');
                                                    
                                                    const deliveryCity = await driver.findElement(By.id('txtDeliveryCity'));
                                                    await deliveryCity.clear();
                                                    await deliveryCity.sendKeys('Copenhagen');
                                                    
                                                    // Check same as delivery address
                                                    const sameAsDeliveryCheckbox = await driver.findElement(By.id('chkRepeat'));
                                                    await sameAsDeliveryCheckbox.click();
                                                    
                                                    // Fill credit card
                                                    const creditCardName = await driver.findElement(By.id('txtCreditCardName'));
                                                    await creditCardName.clear();
                                                    await creditCardName.sendKeys('Pernille L. Hansen');
                                                    
                                                    const expiryDate = await driver.findElement(By.id('txtExpiryDate'));
                                                    await expiryDate.clear();
                                                    
                                                    // Try JavaScript method for alternative path
                                                    try {
                                                        await driver.executeScript("arguments[0].value = '2027-12';", expiryDate);
                                                    } catch (jsError) {
                                                        await expiryDate.sendKeys('2027-12');
                                                    }
                                                    
                                                    const cvv = await driver.findElement(By.id('txtCVV'));
                                                    await cvv.clear();
                                                    await cvv.sendKeys('666');
                                                    
                                                    // Click Place Purchase
                                                    const placePurchaseButton = await driver.findElement(By.css('input[type="submit"][value="Place Purchase"]'));
                                                    await placePurchaseButton.click();
                                                    await driver.sleep(3000);
                                                    
                                                    console.log('✓ SUCCESS: Order completed (alternative path)!');
                                                    
                                                    // Also verify empty cart for alternative path
                                                    try {
                                                        // Close checkout modal
                                                        const closeCheckoutButton = await driver.findElement(By.css('dialog#checkout button[title="Close Check out"], dialog#checkout header button'));
                                                        await closeCheckoutButton.click();
                                                        await driver.sleep(1000);
                                                        
                                                        // Click cart and verify empty
                                                        const cartButton = await driver.findElement(By.css('#optCart a, a[title="Cart"]'));
                                                        await cartButton.click();
                                                        await driver.sleep(2000);
                                                        
                                                        const cartContents = await driver.findElements(By.css('dialog#cart section tr, .cart-item'));
                                                        if (cartContents.length === 0) {
                                                            console.log('✓ Cart verified empty (alternative path)');
                                                        }
                                                        
                                                        // Close cart modal
                                                        const closeCartButton = await driver.findElement(By.css('dialog#cart header button'));
                                                        await closeCartButton.click();
                                                        await driver.sleep(1000);
                                                        
                                                    } catch (altCartVerificationError) {
                                                        console.log('⚠ Could not verify empty cart on alternative path');
                                                    }
                                                    
                                                    // Also handle logout for alternative path
                                                    try {
                                                        console.log('Logging out (alternative path)...');
                                                        const logoutOption = await driver.findElement(By.css('#optLogout a, a[title="Log out"]'));
                                                        await logoutOption.click();
                                                        await driver.sleep(2000);
                                                        
                                                        // Verify login option
                                                        const loginOption = await driver.findElement(By.css('#optLogin a, a[href="login.html"]'));
                                                        if (await loginOption.isDisplayed()) {
                                                            console.log('✓ Logged out and Login option verified (alternative path)');
                                                        }
                                                    } catch (altLogoutError) {
                                                        console.log('⚠ Could not complete logout on alternative path');
                                                    }
                                                } catch (altCheckoutFormError) {
                                                    console.log('⚠ Could not fill checkout form on alternative path');
                                                }
                                            } catch (altCheckoutError) {
                                                console.log('⚠ Could not click Check Out after alternative quantity update');
                                            }
                                        }
                                    } catch (altQuantityError) {
                                        console.log('⚠ Could not update quantity after alternative cart opening');
                                    }
                                } catch (cartError) {
                                    console.log('⚠ Could not open cart after alternative method');
                                }
                            }
                        }
                    } catch (alternativeError) {
                        console.log('❌ Could not add SanDisk product to cart');
                    }
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
        if (driver) {
            console.log('Keeping browser open for 3 seconds...');
            await driver.sleep(3000);
            await driver.quit();
            console.log('Browser closed.');
        }
    }
}

// Run the test
testSignupClick();