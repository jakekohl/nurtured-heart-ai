<template>
  <div class="faq-view">
    <div class="faq-header">
      <h1>Frequently Asked Questions</h1>
      <p class="subtitle">We're here to help you understand and use this tool effectively</p>
    </div>

    <div class="faq-sections">
      <section class="faq-section">
        <div class="section-icon">✨</div>
        <h2>What is the Nurtured Heart Approach?</h2>
        <p>
          The Nurtured Heart Approach® (NHA) is a relationship-focused methodology that 
          transforms challenging behaviors by recognizing and celebrating success in the 
          present moment. It was developed by Howard Glasser to help children (and adults) 
          build inner wealth and self-regulation.
        </p>
        <router-link to="/what-is-nha" class="learn-more-link">
          Learn more about NHA →
        </router-link>
      </section>

      <section class="faq-section">
        <div class="section-icon">🤖</div>
        <h2>How does this AI compliment generator work?</h2>
        <p>
          This tool uses an AI language model to generate personalized compliments based on 
          the information you provide: the recipient's name, your relationship, positive 
          qualities you've observed, and any specific context or achievements. The AI is 
          guided by prompts that ensure the compliments align with NHA principles.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">🔒</div>
        <h2>Is my data private and secure?</h2>
        <p>
          Yes! Your privacy is important. This application does not store any of the 
          information you enter or the compliments that are generated. Each session is 
          temporary, and no personal data is saved to databases or shared with third parties. 
          Once you close or refresh the page, all information is cleared.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">🧠</div>
        <h2>What AI model does this use?</h2>
        <p>
          This application uses a large language model specifically prompted to generate 
          compliments that align with the Nurtured Heart Approach principles. The AI is 
          designed to recognize and celebrate positive qualities, strengths, and achievements 
          in an authentic and meaningful way.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">✏️</div>
        <h2>Can I customize the compliments?</h2>
        <p>
          Yes! The generated compliments are meant to be starting points. You should always 
          adapt them to match your authentic voice and the specific nuances of your relationship. 
          The form allows you to specify qualities, context, tone, and relationship type to 
          help personalize the output.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">💙</div>
        <h2>Who can benefit from using this tool?</h2>
        <p>
          This tool is designed for anyone who wants to practice the Nurtured Heart Approach:
        </p>
        <ul>
          <li>Parents and caregivers</li>
          <li>Teachers and educators</li>
          <li>Therapists and counselors</li>
          <li>Coaches and mentors</li>
          <li>Anyone in a supportive relationship role</li>
        </ul>
      </section>

      <section class="faq-section">
        <div class="section-icon">💻</div>
        <h2>What do I need to use this application?</h2>
        <p>
          All you need is a modern web browser! This application is web-based and works on 
          desktop computers, tablets, and mobile devices. For the best experience, we recommend 
          using the latest version of Chrome, Firefox, Safari, or Edge.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">🚀</div>
        <h2>Can I run this application myself?</h2>
        <p>
          Yes! This is an open-source project. If you'd like to run your own instance locally 
          or deploy it yourself, detailed installation instructions are available in the project's 
          GitHub repository. The code includes setup scripts and documentation to help you get 
          started.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">🤝</div>
        <h2>Can I contribute to this project?</h2>
        <p>
          Absolutely! This is an open-source project and we welcome contributions of all kinds:
        </p>
        <ul>
          <li>Code improvements and bug fixes</li>
          <li>Documentation enhancements</li>
          <li>UI/UX suggestions</li>
          <li>New features or prompt improvements</li>
          <li>Translations</li>
        </ul>
        <router-link to="/about" class="learn-more-link">
          View the source code →
        </router-link>
      </section>

      <section class="faq-section">
        <div class="section-icon">ℹ️</div>
        <h2>Is this affiliated with the official Nurtured Heart Approach organization?</h2>
        <p>
          No, this is an independent, open-source project created to support people practicing 
          the Nurtured Heart Approach. It is not officially affiliated with or endorsed by 
          the Nurtured Heart Approach organization, Children's Success Foundation, or Howard Glasser.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">💬</div>
        <h2>What if the generated compliments don't feel authentic?</h2>
        <p>
          AI-generated compliments are meant as inspiration and starting points, not final 
          products. The most important aspect of the Nurtured Heart Approach is authenticity. 
          Always review, modify, and personalize the compliments to match your genuine feelings 
          and natural communication style. If a generated compliment doesn't resonate, use it 
          as a template and adjust it to fit your authentic voice.
        </p>
      </section>

      <section class="faq-section">
        <div class="section-icon">🏥</div>
        <h2>Can I use this for professional/therapeutic purposes?</h2>
        <p>
          This tool can be helpful for professionals working with the Nurtured Heart Approach, 
          but it should be used thoughtfully. Consider it a support tool for brainstorming or 
          learning, not a replacement for professional judgment and authentic human connection. 
          Always prioritize your professional expertise and the unique needs of your clients.
        </p>
      </section>
    </div>

    <section class="contact-section">
      <div class="contact-icon">💌</div>
      <h2>Still have questions?</h2>
      <p>
        If you have additional questions or feedback, please feel free to open an issue 
        on our GitHub repository or reach out to the community.
      </p>
    </section>
  </div>
</template>

<style scoped>
.faq-view {
  max-width: 900px;
  margin: 0 auto;
}

.faq-header {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.faq-header h1 {
  color: #1e293b;
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.faq-header .subtitle {
  color: #64748b;
  font-size: 1.125rem;
  line-height: 1.6;
}

.faq-sections {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.faq-section {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.faq-section:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.section-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: inline-block;
}

.faq-section h2 {
  color: #1e293b;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
  line-height: 1.3;
}

.faq-section p {
  color: #475569;
  line-height: 1.8;
  margin-bottom: 1rem;
  font-size: 1.0625rem;
}

.faq-section p:last-child {
  margin-bottom: 0;
}

.faq-section ul,
.faq-section ol {
  margin-left: 1.5rem;
  margin-top: 0.75rem;
  color: #475569;
}

.faq-section li {
  margin-bottom: 0.625rem;
  line-height: 1.7;
  font-size: 1.0625rem;
}

.learn-more-link {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  display: inline-block;
  margin-top: 0.75rem;
  transition: color 0.2s ease;
}

.learn-more-link:hover {
  color: #2563eb;
  text-decoration: underline;
}

.contact-section {
  margin-top: 3rem;
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  color: white;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
}

.contact-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.contact-section h2 {
  color: white;
  font-size: 1.75rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.contact-section p {
  color: rgba(255, 255, 255, 0.95);
  line-height: 1.8;
  font-size: 1.0625rem;
  max-width: 600px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .faq-header h1 {
    font-size: 1.875rem;
  }

  .faq-header .subtitle {
    font-size: 1rem;
  }

  .faq-section {
    padding: 1.5rem;
  }

  .faq-section h2 {
    font-size: 1.25rem;
  }

  .section-icon {
    font-size: 1.5rem;
  }

  .contact-section {
    padding: 2rem 1.5rem;
  }

  .contact-section h2 {
    font-size: 1.5rem;
  }
}
</style>

