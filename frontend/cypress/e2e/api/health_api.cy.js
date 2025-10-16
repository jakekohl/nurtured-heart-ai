describe('Health API', () => {
  const baseUrl = 'http://localhost:8000';

  it('should return a 200 status code', () => {
    cy.request('GET', `${baseUrl}/health`).then((response) => {
      expect(response.status).to.eq(200)
    })
  })
  it('should return a version in the response', () => {
    cy.request('GET', `${baseUrl}/health`).then((response) => {
      expect(response.body).to.have.property('version')
      expect(response.body.version).to.be.a('string')
      expect(response.body.version).to.match(/^\d+\.\d+\.\d+$/)
    })
  })
  it('should return details about the configured llm service', () => {
    cy.request('GET', `${baseUrl}/health`).then((response) => {
      expect(response.body).to.have.property('llm').and.to.be.an('object')
      expect(response.body.llm).to.have.property('service')
      expect(response.body.llm.service).to.be.a('string')
      expect(response.body.llm.service).to.match(/^ollama|gemini$/)
      expect(response.body.llm).to.have.property('available')
      expect(response.body.llm.available).to.be.a('boolean')
      expect(response.body.llm).to.have.property('installed_models')
      expect(response.body.llm.installed_models).to.be.an('array')
      expect(response.body.llm.installed_models).to.have.length.greaterThan(0)
      expect(response.body.llm).to.have.property('required_model')
      expect(response.body.llm.required_model).to.be.a('string')
    })
  })
  it('should return details about the configured email service', () => {
    cy.request('GET', `${baseUrl}/health`).then((response) => {
      expect(response.body).to.have.property('email_service').and.to.be.an('object')
      expect(response.body.email_service).to.have.property('enabled')
      expect(response.body.email_service.enabled).to.be.a('boolean')
      expect(response.body.email_service).to.have.property('configured').to.be.a('boolean')
      expect(response.body.email_service).to.have.property('smtp_host').to.be.a('string')
      expect(response.body.email_service).to.have.property('smtp_port').to.be.a('number')
      expect(response.body.email_service).to.not.have.property('smtp_user')
      expect(response.body.email_service).to.not.have.property('smtp_password')
      expect(response.body.email_service).to.have.property('from_email').to.be.a('string')
    })
  })
})