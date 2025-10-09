<template>
  <nav class="app-navbar">
    <div class="nav-container">
      <div class="nav-logo">
        <span class="app-logo">💙 Nurtured Heart AI</span>
      </div>
      <div class="nav-menu">
        <router-link 
          v-for="item in menuItems" 
          :key="item.label"
          :to="item.route" 
          class="nav-item"
          :class="{ 'active': $route.path === item.route }"
        >
          <i :class="item.icon"></i>
          {{ item.label }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const menuItems = ref([
  {
    label: 'Compliment Generator',
    icon: 'pi pi-heart-fill',
    route: '/'
  },
  {
    label: 'What is NHA?',
    icon: 'pi pi-question-circle',
    route: '/what-is-nha'
  },
  {
    label: 'About',
    icon: 'pi pi-info-circle',
    route: '/about'
  },
  {
    label: 'FAQ',
    icon: 'pi pi-comments',
    route: '/faq'
  }
])
</script>

<style scoped>
/* Custom Navigation */
.app-navbar {
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-logo {
  flex-shrink: 0;
}

.nav-menu {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  color: #64748b;
  font-weight: 500;
  transition: all 0.2s ease;
  border: 2px solid transparent;
  white-space: nowrap;
}

.nav-item:hover {
  background-color: #e0f2fe;
  border-color: #3b82f6;
  color: #1e293b;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(59, 130, 246, 0.15);
}

.nav-item.active {
  background-color: #3b82f6;
  color: white;
  border-color: #2563eb;
}

.nav-item.active:hover {
  background-color: #2563eb;
  color: white;
  transform: translateY(-1px);
}

.app-logo {
  font-size: 1.3rem;
  font-weight: 600;
  color: #1e293b;
}

@media (max-width: 768px) {
  .app-logo {
    font-size: 1.1rem;
  }
  
  .nav-container {
    padding: 0 1rem;
  }
  
  .nav-menu {
    gap: 1.5rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}
</style>
