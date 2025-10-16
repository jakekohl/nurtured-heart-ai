describe('Compliment Generator', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should load the compliment generator page', () => {
    cy.contains('Nurtured Heart Compliment Generator').should('be.visible')
    cy.contains('Generate a Nurtured Heart Compliment').should('be.visible')
  })

  it('should fill out the form and generate a compliment', () => {
    cy.intercept('POST', '/api/generate', { fixture: 'compliment.json' }).as('generate')

    // Fill in recipient name
    cy.get('#recipientName').type('John')
    
    // Select relationship
    cy.get('#relationship').click()
    cy.contains('friend').click()
    
    // Add a quality
    cy.get('#quality').type('kind')
    cy.get('.add-btn').click()
    
    // Add context
    cy.get('#context').type('helped me with my project')
    
    // Select tone
    cy.get('#tone').click()
    cy.contains('Warm').click()
    
    // Generate compliment
    cy.get('.generate-btn').click()

    cy.wait('@generate').its('response.body').should('have.property', 'data')

    // Wait for the compliment to be generated
    cy.get('.compliment-text', { timeout: 10000 }).should('be.visible')
  })

  it('should validate required fields', () => {
    // Try to generate without filling required fields
    cy.get('.generate-btn').should('be.disabled')
    
    // Fill only name
    cy.get('#recipientName').type('John')
    cy.get('.generate-btn').should('be.disabled')
    
    // Add relationship
    cy.get('#relationship').click()
    cy.contains('friend').click()
    cy.get('.generate-btn').should('be.disabled')
    
    // Add quality
    cy.get('#quality').type('kind')
    cy.get('.add-btn').click()
    cy.get('.generate-btn').should('not.be.disabled')
  })
})
