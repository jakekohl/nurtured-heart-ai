<template>
  <div class="about-view">
    <Card>
      <template #title>
        <h1>About This App</h1>
      </template>
      
      <template #content>
        <section class="intro-section">
          <p class="lead">
            The Nurtured Heart AI Compliment Generator is a tool designed to help parents, 
            educators, therapists, and caregivers create meaningful, specific compliments 
            that align with the principles of the Nurtured Heart Approach®.
          </p>
        </section>

        <Divider />

        <section class="purpose-section">
          <h2>Purpose</h2>
          <p>
            This application leverages AI technology to help you craft personalized compliments 
            that recognize and celebrate specific positive qualities and behaviors. By making 
            it easier to provide consistent, meaningful recognition, we hope to support the 
            practice of the Nurtured Heart Approach in daily interactions.
          </p>
        </section>

        <Divider />

        <section class="features-section">
          <h2>Key Features</h2>
          
          <div class="feature-grid">
            <div class="feature-item">
              <i class="pi pi-sparkles"></i>
              <h3>AI-Powered Generation</h3>
              <p>Uses advanced language models to create authentic, specific compliments</p>
            </div>

            <div class="feature-item">
              <i class="pi pi-heart"></i>
              <h3>NHA-Aligned</h3>
              <p>All compliments follow the principles of the Nurtured Heart Approach</p>
            </div>

            <div class="feature-item">
              <i class="pi pi-users"></i>
              <h3>Customizable</h3>
              <p>Tailor compliments to specific relationships, qualities, and contexts</p>
            </div>

            <div class="feature-item">
              <i class="pi pi-shield"></i>
              <h3>Privacy-Focused</h3>
              <p>Runs locally with Ollama - your data stays on your machine</p>
            </div>
          </div>
        </section>

        <Divider />

        <section class="tech-section">
          <h2>Technology Stack</h2>
          <p>This application is built with modern, open-source technologies:</p>
          
          <div class="tech-list">
            <div class="tech-item">
              <strong>Frontend:</strong> Vue.js 3 + PrimeVue UI Components
            </div>
            <div class="tech-item">
              <strong>Backend:</strong> Python FastAPI
            </div>
            <div class="tech-item">
              <strong>AI Model:</strong> Ollama with Llama 3
            </div>
            <div class="tech-item">
              <strong>Deployment:</strong> Docker containers for easy setup
            </div>
          </div>
        </section>

        <Divider />

        <section class="source-section">
          <h2>Open Source</h2>
          <p>
            This project is open source and available on GitHub. We welcome contributions, 
            feedback, and content suggestions.
          </p>
          
          <div class="github-link">
            <Button 
              label="View Source Code on GitHub" 
              icon="pi pi-github" 
              severity="secondary"
              @click="openGithub"
            />
          </div>
        </section>

        <Divider />

        <section class="disclaimer-section">
          <h2>Disclaimer</h2>
          <Message severity="info" :closable="false">
            This tool is designed to support, not replace, genuine human connection and the 
            principles of the Nurtured Heart Approach. Use the generated compliments as 
            inspiration and adapt them to your authentic voice and relationship.
          </Message>
        </section>
      </template>
    </Card>
  </div>
</template>

<script setup>
const openGithub = () => {
  // Update this URL once you've pushed to GitHub
  window.open('https://github.com/YOUR_USERNAME/nurtured-heart-ai', '_blank')
}
</script>

<style scoped>
.about-view {
  max-width: 900px;
  margin: 0 auto;
}

:deep(.p-card-content) {
  padding: 2.5rem !important;
}

h1 {
  color: #1e293b;
  font-size: 2.5rem;
  text-align: center;
  margin-bottom: 2rem;
  padding: 1.5rem 0 1rem 0;
  border-bottom: 1px solid #e2e8f0;
}

h2 {
  color: #1e293b;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
}

.lead {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #475569;
}

section {
  margin: 3rem 0;
}

section p {
  color: #475569;
  line-height: 1.8;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.feature-item {
  background: #f8fafc;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
}

.feature-item i {
  font-size: 2.5rem;
  color: #3b82f6;
  margin-bottom: 1rem;
}

.feature-item h3 {
  color: #1e293b;
  margin-bottom: 0.75rem;
  font-size: 1.2rem;
}

.feature-item p {
  color: #64748b;
  font-size: 0.95rem;
  margin: 0;
}

.tech-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1.5rem;
}

.tech-item {
  background: #f8fafc;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  color: #475569;
}

.tech-item strong {
  color: #1e293b;
}

.github-link {
  margin-top: 1.5rem;
}

@media (max-width: 768px) {
  h1 {
    font-size: 1.8rem;
  }
  
  h2 {
    font-size: 1.4rem;
  }
  
  .feature-grid {
    grid-template-columns: 1fr;
  }
}
</style>

