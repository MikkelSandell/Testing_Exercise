const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:5500/10_EX_Selenium_Webshop/js_webshop/',
    viewportWidth: 1280,
    viewportHeight: 720,
    video: false,
    screenshotOnRunFailure: true,
    defaultCommandTimeout: 10000,
    requestTimeout: 10000,
    responseTimeout: 10000,
    pageLoadTimeout: 10000,
    watchForFileChanges: false,
    
    setupNodeEvents(on, config) {
      // implement node event listeners here
      
      // Handle console logs from the app
      on('task', {
        log(message) {
          console.log(message)
          return null
        }
      })
      
      return config
    },
    
    // Specify the spec patterns
    specPattern: [
      '00_Cypress/**/*.cy.{js,jsx,ts,tsx}',
      '00_Cypress/**/*.spec.{js,jsx,ts,tsx}'
    ],
    
    // Support file
    supportFile: false, // Disable default support file for this simple setup
    
    // Experimental features
    experimentalStudio: true,
    experimentalWebKitSupport: false
  },
  
  component: {
    devServer: {
      framework: 'create-react-app',
      bundler: 'webpack'
    }
  }
})