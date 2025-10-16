<template>
  <Card v-if="compliment" class="compliment-display">
    <template #title>
      <div class="display-title">
        <i class="pi pi-star-fill" style="color: #fbbf24;" />
        Your Nurtured Heart Compliment
      </div>
    </template>
    
    <template #content>
      <div class="compliment-content">
        <p class="compliment-text">
          {{ compliment.compliment }}
        </p>
        
        <div class="actions">
          <Button 
            label="Copy" 
            icon="pi pi-copy"
            class="action-btn copy-btn"
            @click="copyToClipboard"
          />
          <Button 
            v-tooltip.top="!emailServiceAvailable ? 'Email service is not configured or disabled' : ''" 
            label="Email"
            icon="pi pi-envelope"
            class="action-btn email-btn"
            :disabled="!emailServiceAvailable"
            @click="showEmailDialog = true"
          />
          <Button 
            v-if="canShare"
            label="Share" 
            icon="pi pi-share-alt"
            class="action-btn share-btn"
            @click="shareCompliment"
          />
          <Button 
            label="Generate Another" 
            icon="pi pi-refresh"
            class="action-btn generate-btn"
            @click="$emit('reset')"
          />
        </div>
        
        <div class="promo-text">
          <p>
            Powered by 
            <a
              href="https://nurtured-heart-ai.vercel.app/"
              target="_blank"
              rel="noopener noreferrer"
              class="promo-link"
            >
              Nurtured Heart AI
            </a>
            - Creating meaningful connections through personalized compliments
          </p>
        </div>
      </div>

      <!-- Simple Email Form -->
      <div v-if="showEmailDialog" class="email-form">
        <h3>Send Compliment via Email</h3>
        <div class="field">
          <label>Recipient Email</label>
          <InputText 
            v-model="emailData.recipient_email" 
            type="email"
            placeholder="recipient@example.com"
            class="w-full"
          />
        </div>
        <div class="field">
          <label>Your Name</label>
          <InputText 
            v-model="emailData.sender_name" 
            placeholder="Your name"
            class="w-full"
          />
        </div>
        <div class="email-actions">
          <Button 
            label="Cancel" 
            text
            @click="showEmailDialog = false"
          />
          <Button 
            label="Send" 
            icon="pi pi-send"
            :loading="sendingEmail"
            @click="sendEmail"
          />
        </div>
      </div>
    </template>
  </Card>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'

const props = defineProps({
  compliment: Object
})

const emit = defineEmits(['reset', 'toast'])

const showEmailDialog = ref(false)
const sendingEmail = ref(false)
const canShare = ref(false)
const emailServiceAvailable = ref(false)
const emailData = ref({
  recipient_email: '',
  sender_name: '',
  recipient_name: '',
  compliment: ''
})

// Check if Web Share API is supported
const checkShareSupport = () => {
  canShare.value = navigator.share && navigator.canShare
}

// Check email service availability
const checkEmailService = async() => {
  try {
    const health = await api.healthCheck()
    emailServiceAvailable.value = health.email_service?.enabled || false
  } catch (err) {
    console.error('Failed to check email service availability:', err)
    emailServiceAvailable.value = false
  }
}

const copyToClipboard = async() => {
  try {
    await navigator.clipboard.writeText(props.compliment.compliment)
    emit('toast', { 
      severity: 'success', 
      summary: 'Copied!', 
      detail: 'Compliment copied to clipboard',
      life: 3000
    })
  } catch (err) {
    emit('toast', { 
      severity: 'error', 
      summary: 'Error', 
      detail: 'Failed to copy to clipboard',
      life: 3000
    })
  }
}

const shareCompliment = async() => {
  try {
    const shareText = `${props.compliment.compliment}\n\nYour greatness has inspired me to compliment you with Nurtured-heart-ai. If you want to compliment someone else's greatness, head to https://nurtured-heart-ai.vercel.app`
    
    // Try sharing with just text first (some platforms prefer this)
    if (navigator.canShare && navigator.canShare({ text: shareText })) {
      await navigator.share({ text: shareText })
      emit('toast', { 
        severity: 'success', 
        summary: 'Shared!', 
        detail: 'Compliment shared successfully',
        life: 3000
      })
    } else if (navigator.canShare && navigator.canShare({ text: shareText, url: 'https://nurtured-heart-ai.vercel.app' })) {
      // Fallback to sharing with both text and URL
      await navigator.share({ 
        text: shareText, 
        url: 'https://nurtured-heart-ai.vercel.app' 
      })
      emit('toast', { 
        severity: 'success', 
        summary: 'Shared!', 
        detail: 'Compliment shared successfully',
        life: 3000
      })
    } else {
      // Fallback to copy to clipboard if sharing is not available
      await navigator.clipboard.writeText(shareText)
      emit('toast', { 
        severity: 'info', 
        summary: 'Copied!', 
        detail: 'Compliment copied to clipboard with promo text',
        life: 3000
      })
    }
  } catch (err) {
    if (err.name !== 'AbortError') {
      // Fallback to copy to clipboard if sharing fails
      try {
        const fallbackText = `"${props.compliment.compliment}"\n\nYour greatness has inspired me to compliment you with Nurtured-heart-ai. If you want to compliment someone else's greatness, head to https://nurtured-heart-ai.vercel.app`
        await navigator.clipboard.writeText(fallbackText)
        emit('toast', { 
          severity: 'info', 
          summary: 'Copied!', 
          detail: 'Compliment copied to clipboard with promo text',
          life: 3000
        })
      } catch (clipboardErr) {
        emit('toast', { 
          severity: 'error', 
          summary: 'Error', 
          detail: 'Failed to share or copy compliment',
          life: 3000
        })
      }
    }
  }
}

const sendEmail = async() => {
  if (!emailData.value.recipient_email) {
    emit('toast', { 
      severity: 'warn', 
      summary: 'Required', 
      detail: 'Please enter recipient email',
      life: 3000
    })
    return
  }

  sendingEmail.value = true
  try {
    const result = await api.sendEmail({
      ...emailData.value,
      compliment: props.compliment.compliment
    })
    
    if (result.success) {
      emit('toast', { 
        severity: 'success', 
        summary: 'Sent!', 
        detail: result.message,
        life: 3000
      })
      showEmailDialog.value = false
      emailData.value = { recipient_email: '', sender_name: '', recipient_name: '', compliment: '' }
    } else {
      throw new Error(result.message)
    }
  } catch (err) {
    emit('toast', { 
      severity: 'error', 
      summary: 'Error', 
      detail: err.message || 'Failed to send email',
      life: 5000
    })
  } finally {
    sendingEmail.value = false
  }
}

// Initialize share support and email service check on component mount
onMounted(() => {
  checkShareSupport()
  checkEmailService()
})
</script>

<style scoped>
.compliment-display {
  max-width: 700px;
  margin: 2rem auto;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.display-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
}

.compliment-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.compliment-text {
  font-size: 1.3rem;
  line-height: 1.8;
  font-style: italic;
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #fbbf24;
}

.actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.action-btn {
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s ease;
  min-height: 44px;
  padding: 0.75rem 1.25rem;
}

.copy-btn {
  background: rgba(255, 255, 255, 0.95);
  color: #1e293b;
  border: 2px solid rgba(255, 255, 255, 0.8);
}

.copy-btn:hover {
  background: #ffffff;
  color: #1e293b;
  border-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.email-btn {
  background: rgba(59, 130, 246, 0.95);
  color: #ffffff;
  border: 2px solid rgba(59, 130, 246, 0.8);
}

.email-btn:hover:not(:disabled) {
  background: #3b82f6;
  color: #ffffff;
  border-color: #3b82f6;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.email-btn:disabled {
  background: rgba(100, 116, 139, 0.5);
  color: rgba(255, 255, 255, 0.6);
  border-color: rgba(100, 116, 139, 0.5);
  cursor: not-allowed;
  opacity: 0.6;
}

.generate-btn {
  background: #10b981;
  color: #ffffff;
  border: 2px solid #10b981;
}

.generate-btn:hover {
  background: #059669;
  color: #ffffff;
  border-color: #059669;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.share-btn {
  background: rgba(168, 85, 247, 0.95);
  color: #ffffff;
  border: 2px solid rgba(168, 85, 247, 0.8);
}

.share-btn:hover {
  background: #a855f7;
  color: #ffffff;
  border-color: #a855f7;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(168, 85, 247, 0.3);
}

/* Responsive button layout */
@media (max-width: 768px) {
  .actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .action-btn {
    width: 100%;
    justify-content: center;
  }
}

/* Focus states for accessibility */
.action-btn:focus {
  outline: 2px solid #fbbf24;
  outline-offset: 2px;
}

/* Promo text styling */
.promo-text {
  margin-top: 1.5rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.promo-text p {
  margin: 0;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.5;
}

.promo-link {
  color: #fbbf24;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.promo-link:hover {
  color: #ffffff;
  text-decoration: underline;
}

.email-form {
  margin-top: 1.5rem;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  color: #1e293b;
}

.email-form h3 {
  margin: 0 0 1rem 0;
  color: #1e293b;
}

.field {
  margin-bottom: 1rem;
}

.field label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #475569;
}

.email-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 1rem;
}

.w-full {
  width: 100%;
}
</style>
