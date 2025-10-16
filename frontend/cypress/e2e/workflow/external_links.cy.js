describe('External Links', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should open the NHA Institute official website link in a new tab', () => {
    cy.get('footer').find('a').contains(/Nurtured Heart Approach/i)
      .should('have.attr', 'href')
      .then((href) => {
        expect(href).to.match(/^https?:\/\/.*nurturedheartinstitute\.com/i);
      });
      cy.get('footer').find('a').contains(/Nurtured Heart Approach/i)
      .should('have.attr', 'target', '_blank');
  });

  it('should open the GitHub Repository link in a new tab', () => {
    cy.get('footer').find('a').contains(/GitHub Repository/i)
      .should('have.attr', 'href')
      .then((href) => {
        expect(href).to.eq('https://github.com/jakekohl/nurtured-heart-ai');
      });
    cy.get('footer').find('a').contains(/GitHub Repository/i)
      .should('have.attr', 'target', '_blank');
  });

  it('should open the API Documentation link in a new tab', () => {
    cy.get('footer').find('a').contains(/API Documentation/i)
      .should('have.attr', 'href')
      .then((href) => {
        expect(href).to.eq('http://localhost:8000/docs');
      });
    cy.get('footer').find('a').contains(/API Documentation/i)
      .should('have.attr', 'target', '_blank');
  });
});
