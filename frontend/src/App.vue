<template>
  <div id="app">
    <Toast />
    
    <NavigationMenu />

    <!-- Main Content Area -->
    <main class="app-main">
      <router-view />
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import NavigationMenu from './components/NavigationMenu.vue'
import AppFooter from './components/AppFooter.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-main {
  flex: 1;
  padding: 3rem 2rem;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .app-main {
    padding: 2rem 1rem;
  }
}
</style>

