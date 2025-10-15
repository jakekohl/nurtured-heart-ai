<template>
  <div class="what-is-nha">
    <Card>
      <template #title>
        <h1>What is the Nurtured Heart Approach?</h1>
      </template>
      
      <template #content>
        <section class="intro-section">
          <p class="lead">
            The Nurtured Heart Approach® (NHA) is a relationship-focused methodology that 
            helps transform challenging behaviors into positive ones by recognizing and 
            celebrating success in the present moment.
          </p>
        </section>

        <Divider />

        <section class="principles-section">
          <h2>Core Principles</h2>
          
          <div class="principle-card">
            <h3>🌟 Recognize Greatness</h3>
            <p>
              Actively notice and energize moments when individuals are being successful, 
              even in small ways. This creates a powerful incentive for positive behavior.
            </p>
          </div>

          <div class="principle-card">
            <h3>💪 Absolute Clarity</h3>
            <p>
              Provide clear, consistent boundaries and consequences that help individuals 
              understand expectations without emotional escalation.
            </p>
          </div>

          <div class="principle-card">
            <h3>❤️ Relentless Positivity</h3>
            <p>
              Create a relationship based on recognizing positive qualities and actions, 
              building inner wealth and self-esteem from the inside out.
            </p>
          </div>
        </section>

        <Divider />

        <section class="benefits-section">
          <h2>Benefits of NHA</h2>
          <ul>
            <li>Reduces challenging behaviors and builds cooperative relationships</li>
            <li>Develops intrinsic motivation and inner strength</li>
            <li>Enhances self-regulation and emotional intelligence</li>
            <li>Creates positive, sustainable transformation in relationships</li>
            <li>Applicable in homes, schools, therapy settings, and organizations</li>
          </ul>
        </section>

        <Divider />

        <section class="learn-more-section">
          <h2>Learn More</h2>
          <p>Explore these official resources to deepen your understanding of the Nurtured Heart Approach:</p>
          
          <div class="resource-links">
            <a
              href="https://www.nurturedheartinstitute.com"
              target="_blank"
              rel="noopener"
              class="resource-link"
            >
              <i class="pi pi-external-link" />
              <div>
                <strong>Nurtured Heart Approach Official Website</strong>
                <p>The primary resource for NHA information, training, and materials</p>
              </div>
            </a>

            <a
              href="https://difficultchild.com"
              target="_blank"
              rel="noopener"
              class="resource-link"
            >
              <i class="pi pi-book" />
              <div>
                <strong>The Nurtured Heart Approach Books</strong>
                <p>Books by Howard Glasser, creator of the approach</p>
              </div>
            </a>

            <a
              href="https://childrenssuccessfoundation.com"
              target="_blank"
              rel="noopener"
              class="resource-link"
            >
              <i class="pi pi-users" />
              <div>
                <strong>Children's Success Foundation</strong>
                <p>Training and certification programs for NHA practitioners</p>
              </div>
            </a>

            <a
              href="https://www.youtube.com/results?search_query=nurtured+heart+approach"
              target="_blank"
              rel="noopener"
              class="resource-link"
            >
              <i class="pi pi-video" />
              <div>
                <strong>Video Resources</strong>
                <p>Watch presentations and tutorials about the Nurtured Heart Approach</p>
              </div>
            </a>
          </div>
        </section>
      </template>
    </Card>
  </div>
</template>

<style scoped>
.what-is-nha {
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

.principles-section,
.benefits-section,
.learn-more-section {
  margin: 2rem 0;
}

.principle-card {
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  border-left: 4px solid #3b82f6;
}

.principle-card h3 {
  color: #1e293b;
  margin-bottom: 0.75rem;
  font-size: 1.3rem;
}

.principle-card p {
  color: #64748b;
  line-height: 1.6;
}

.benefits-section ul {
  list-style-position: inside;
  color: #475569;
  line-height: 2;
}

.benefits-section li {
  margin-bottom: 0.5rem;
}

.resource-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1.5rem;
}

.resource-link {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  padding: 1.5rem;
  background: #f8fafc;
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.2s;
  border: 1px solid #e2e8f0;
}

.resource-link:hover {
  background: #e0f2fe;
  border-color: #3b82f6;
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.resource-link i {
  font-size: 2rem;
  color: #3b82f6;
  margin-top: 0.25rem;
}

.resource-link strong {
  color: #1e293b;
  font-size: 1.1rem;
  display: block;
  margin-bottom: 0.5rem;
}

.resource-link p {
  color: #64748b;
  margin: 0;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  h1 {
    font-size: 1.8rem;
  }
  
  h2 {
    font-size: 1.4rem;
  }
}
</style>
