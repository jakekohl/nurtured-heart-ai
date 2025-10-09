<template>
  <Card class="compliment-form">
    <template #title>
      <div class="title-container">
        <i class="pi pi-heart-fill" style="color: #ec4899; margin-right: 0.5rem;"></i>
        Generate a Nurtured Heart Compliment
      </div>
    </template>
    
    <template #content>
      <div class="form-grid">
        <!-- Recipient Name -->
        <div class="field">
          <label for="recipientName">Recipient's Name *</label>
          <InputText 
            id="recipientName"
            v-model="formData.recipient_name" 
            placeholder="Enter name"
            class="w-full"
          />
        </div>

        <!-- Relationship -->
        <div class="field">
          <label for="relationship">Relationship *</label>
          <Dropdown
            id="relationship"
            v-model="formData.relationship"
            :options="relationshipOptions"
            placeholder="Select relationship"
            class="w-full"
          />
        </div>

        <!-- Qualities -->
        <div class="field">
          <label for="quality">Positive Qualities *</label>
          <div class="quality-input">
            <InputText 
              id="quality"
              v-model="currentQuality" 
              placeholder="Enter a quality (e.g., creative, kind)"
              @keyup.enter="addQuality"
              class="w-full"
            />
            <Button 
              icon="pi pi-plus" 
              @click="addQuality"
              :disabled="!currentQuality"
              class="add-btn"
            />
          </div>
          <div class="qualities-chips" v-if="formData.qualities.length">
            <Chip 
              v-for="(quality, index) in formData.qualities" 
              :key="index"
              :label="quality"
              removable
              @remove="removeQuality(index)"
            />
          </div>
        </div>

        <!-- Context (Optional) -->
        <div class="field">
          <label for="context">Context or Recent Achievement (Optional)</label>
          <Textarea 
            id="context"
            v-model="formData.context" 
            rows="3"
            placeholder="E.g., finished a challenging project, showed kindness to a peer..."
            class="w-full"
          />
        </div>

        <!-- Tone -->
        <div class="field">
          <label for="tone">Tone</label>
          <Dropdown
            id="tone"
            v-model="formData.tone"
            :options="toneOptions"
            optionLabel="label"
            optionValue="value"
            placeholder="Select tone"
            class="w-full"
          />
        </div>

        <!-- Generate Button -->
        <Button 
          label="Generate Compliment" 
          icon="pi pi-sparkles"
          @click="handleGenerate"
          :loading="loading"
          :disabled="!isFormValid"
          class="generate-btn"
        />
      </div>
    </template>
  </Card>
</template>

<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['generate'])

const formData = ref({
  recipient_name: '',
  relationship: 'student',
  qualities: [],
  context: '',
  tone: 'warm'
})

const currentQuality = ref('')
const loading = ref(false)

const relationshipOptions = [
  'student',
  'child',
  'friend',
  'colleague',
  'family member',
  'partner',
  'teacher',
  'team member'
]

const toneOptions = [
  { label: 'Warm', value: 'warm' },
  { label: 'Encouraging', value: 'encouraging' },
  { label: 'Celebratory', value: 'celebratory' },
  { label: 'Gentle', value: 'gentle' }
]

const isFormValid = computed(() => {
  return formData.value.recipient_name && 
         formData.value.relationship && 
         formData.value.qualities.length > 0
})

const addQuality = () => {
  if (currentQuality.value.trim()) {
    formData.value.qualities.push(currentQuality.value.trim())
    currentQuality.value = ''
  }
}

const removeQuality = (index) => {
  formData.value.qualities.splice(index, 1)
}

const handleGenerate = async () => {
  if (!isFormValid.value) return
  
  loading.value = true
  try {
    await emit('generate', { ...formData.value })
  } finally {
    loading.value = false
  }
}

defineExpose({ setLoading: (val) => loading.value = val })
</script>

<style scoped>
.compliment-form {
  max-width: 600px;
  margin: 0 auto;
}

:deep(.p-card-content) {
  padding: 2.5rem !important;
}

.title-container {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1e293b;
  margin-bottom: 0.5rem;
  gap: 0.75rem;
}

:deep(.p-card-title) {
  margin-bottom: 1.5rem !important;
  padding: 1.5rem 0 1rem 0 !important;
  border-bottom: 1px solid #e2e8f0 !important;
  text-align: center !important;
}

.form-grid {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.field label {
  font-weight: 600;
  color: #475569;
  font-size: 0.95rem;
}

.quality-input {
  display: flex;
  gap: 0.5rem;
}

.qualities-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.generate-btn {
  margin-top: 1rem;
  width: 100%;
  padding: 0.75rem;
  font-size: 1.1rem;
}

.w-full {
  width: 100%;
}
</style>

