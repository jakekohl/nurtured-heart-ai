describe('LLM API', () => {
  const baseUrl = 'http://localhost:8000';

  it('should list available models', () => {
    cy.request({
      method: 'GET',
      url: `${baseUrl}/api/models`,
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('available')
      expect(response.body.available).to.be.a('boolean');
      expect(response.body).to.have.property('installed_models');
      expect(response.body.installed_models).to.be.an('array').and.to.have.length.greaterThan(0);
      expect(response.body).to.have.property('required_model');
      expect(response.body.required_model).to.be.a('string').to.match(/^llama|gemini$/);
      expect(response.body).to.have.property('service');
      expect(response.body.service).to.be.a('string').to.match(/^ollama|gemini$/);
    });
  });
});