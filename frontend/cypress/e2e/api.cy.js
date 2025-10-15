describe('Compliment API', () => {
  const baseUrl = 'http://localhost:8000';

  context('Health Check', () => {
    it('should return a 200 status code', () => {
      cy.request('GET', `${baseUrl}/health`).then((response) => {
        expect(response.status).to.eq(200)
      })
    })
  })

  context('Compliment Generation', () => {
    it('should support generating a compliment with required fields', () => {
      cy.request({
        method: 'POST',
        url: `${baseUrl}/api/generate`,
        body: {
          recipient_name: 'Alice',
          relationship: 'friend',
          context: 'finished a challenging project',
          qualities: ['creative', 'persistent'],
          tone: 'warm'
        },
        }).then((response) => {
        expect(response.status).to.eq(200)
        expect(response.body).to.have.property('success', true)
        expect(response.body).to.have.property('data')
        expect(response.body.data.compliment).to.include('Alice')
      })
    })

    it('should support generating a compliment without context', () => {
      cy.request({
        method: 'POST',
        url: `${baseUrl}/api/generate`,
        body: {
          recipient_name: 'Alice',
          relationship: 'friend',
          qualities: ['kind', 'thoughtful']
        },
      }).then((response) => {
        expect(response.status).to.eq(200)
        expect(response.body).to.have.property('success', true)
        expect(response.body).to.have.property('data')
        expect(response.body.data.compliment).to.include('Alice')
      })
    })
  })
})
