<template>
  <div class="generator-view">
    <header class="view-header">
      <h1>💙 Nurtured Heart Compliment Generator</h1>
      <p>Create meaningful, heartfelt compliments powered by AI</p>
    </header>

    <Message v-if="healthStatus && !healthStatus.llm.available" severity="warn" :closable="false">
      <strong>LLM Not Ready:</strong> {{ healthStatus.llm.error || 'Model not available' }}
      <br>
      <small>If this is not running locally, this is expected at this time.</small>
    </Message>

    <ComplimentForm 
      v-if="!generatedCompliment"
      ref="formRef"
      @generate="generateCompliment" 
    />

    <ComplimentDisplay 
      v-if="generatedCompliment"
      :compliment="generatedCompliment"
      @reset="resetForm"
      @toast="showToast"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from 'primevue/usetoast'
import ComplimentForm from '../components/ComplimentForm.vue'
import ComplimentDisplay from '../components/ComplimentDisplay.vue'
import api from '../services/api'

const toast = useToast()
const formRef = ref(null)
const generatedCompliment = ref(null)
const healthStatus = ref(null)

onMounted(async() => {
  try {
    healthStatus.value = await api.healthCheck()
  } catch (err) {
    showToast({
      severity: 'error',
      summary: 'Connection Error',
      detail: 'Could not connect to backend API',
      life: 5000
    })
  }
})

const generateCompliment = async(formData) => {
  try {
    const result = await api.generateCompliment(formData)
    
    if (result.success) {
      generatedCompliment.value = result.data
      showToast({
        severity: 'success',
        summary: 'Generated!',
        detail: 'Your compliment is ready',
        life: 3000
      })
    }
  } catch (err) {
    showToast({
      severity: 'error',
      summary: 'Generation Failed',
      detail: err.response?.data?.detail || 'Failed to generate compliment',
      life: 5000
    })
  } finally {
    if (formRef.value) {
      formRef.value.setLoading(false)
    }
  }
}

const resetForm = () => {
  generatedCompliment.value = null
}

const showToast = (options) => {
  toast.add(options)
}
</script>

<style scoped>
.view-header {
  text-align: center;
  margin-bottom: 2rem;
}

.view-header h1 {
  font-size: 2.5rem;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.view-header p {
  color: #64748b;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .view-header h1 {
    font-size: 1.8rem;
  }
}
</style>
