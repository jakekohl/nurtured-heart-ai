describe('Navigation', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should display navigation elements', () => {
    cy.contains('Nurtured Heart Compliment Generator').should('be.visible');
    cy.get('nav').should('exist');
  });

  it('should navigate to What is NHA page', () => {
    cy.get('nav').contains(/what is nha/i).click();
    cy.url().should('include', '/what-is-nha');
    cy.contains(/what is nha/i).should('be.visible');
  });

  it('should navigate to About page', () => {
    cy.get('nav').contains(/about/i).click();
    cy.url().should('include', '/about');
    cy.contains(/about/i).should('be.visible');
  });

  it('should navigate to FAQ page', () => {
    cy.get('nav').contains(/faq/i).click();
    cy.url().should('include', '/faq');
    cy.contains(/faq/i).should('be.visible');
  });
});
