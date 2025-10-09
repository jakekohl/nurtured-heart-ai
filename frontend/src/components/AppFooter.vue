<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-section">
        <h4>Nurtured Heart AI</h4>
        <p>Generate meaningful compliments using the Nurtured Heart Approach</p>
      </div>
      
      <div class="footer-section">
        <h4>Quick Links</h4>
        <ul>
          <li><router-link to="/">Compliment Generator</router-link></li>
          <li><router-link to="/what-is-nha">What is NHA?</router-link></li>
          <li><router-link to="/about">About This App</router-link></li>
          <li><router-link to="/faq">FAQ</router-link></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h4>Resources</h4>
        <ul>
          <li><a href="https://nurturedheart.com" target="_blank" rel="noopener">Nurtured Heart Approach</a></li>
          <li><a href="#" target="_blank" rel="noopener">GitHub Repository</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h4>Legal</h4>
        <ul>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    
    <Divider />
    
    <div class="footer-bottom">
      <p>&copy; 2025 Nurtured Heart AI. Built with ❤️ using the Nurtured Heart Approach</p>
    </div>
  </footer>
</template>

<script setup>
// No props or logic needed for this component
</script>

<style scoped>
.app-footer {
  background: white;
  margin-top: auto;
  box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.1);
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.footer-section h4 {
  color: #1e293b;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.footer-section p {
  color: #64748b;
  font-size: 0.9rem;
  line-height: 1.5;
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 0.5rem;
}

.footer-section ul li a {
  color: #64748b;
  text-decoration: none;
  transition: color 0.2s;
  font-size: 0.9rem;
}

.footer-section ul li a:hover {
  color: #3b82f6;
}

.footer-bottom {
  text-align: center;
  padding: 1rem 2rem;
  color: #64748b;
  font-size: 0.85rem;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>
