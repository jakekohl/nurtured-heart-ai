describe('Email API', () => {
  const baseUrl = 'http://localhost:8000';

  it('should support sending an email', () => {
    cy.request({
      method: 'POST',
      url: `${baseUrl}/api/send-email`,
      body: {
        recipient_email: 'test@example.com',
        recipient_name: 'Test',
        sender_name: 'Test',
        compliment: 'Test compliment'
      },
    }).then((response) => {
      expect(response.status).to.eq(200)
      expect(response.body).to.have.property('success')
      expect(response.body.success).to.be.a('boolean')
      expect(response.body).to.have.property('message')
      expect(response.body.message).to.be.a('string')
    });
  })
})