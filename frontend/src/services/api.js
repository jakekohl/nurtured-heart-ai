import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export default {
  async generateCompliment(data) {
    const response = await apiClient.post('/api/generate', data)
    return response.data
  },

  async sendEmail(data) {
    const response = await apiClient.post('/api/send-email', data)
    return response.data
  },

  async healthCheck() {
    const response = await apiClient.get('/health')
    return response.data
  }
}

