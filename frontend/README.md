# Frontend - Nurtured Heart Compliment Generator

Vue.js 3 frontend application with a beautiful, responsive UI built with PrimeVue.

## 🛠️ Tech Stack

- **Vue.js 3** - Composition API with `<script setup>`
- **PrimeVue** - Enterprise-grade UI component library
- **Vite** - Lightning-fast build tool
- **Vue Router** - Official routing library
- **Axios** - HTTP client

---

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ComplimentForm.vue      # Main form with inputs
│   │   ├── ComplimentDisplay.vue   # Display generated compliment
│   │   ├── NavigationMenu.vue      # Top navigation bar
│   │   └── AppFooter.vue          # Footer with links
│   ├── views/
│   │   ├── GeneratorView.vue      # Main generator page (/)
│   │   ├── AboutView.vue          # About page (/about)
│   │   ├── WhatIsNHA.vue         # NHA information (/what-is-nha)
│   │   └── FAQView.vue           # FAQ page (/faq)
│   ├── router/
│   │   └── index.js              # Vue Router configuration
│   ├── services/
│   │   └── api.js                # Backend API client (Axios)
│   ├── App.vue                   # Root component
│   └── main.js                   # Application entry point
├── cypress/
│   ├── e2e/                      # End-to-end test specs
│   ├── support/                  # Cypress commands & helpers
│   └── fixtures/                 # Test data
├── public/                       # Static assets
├── index.html                    # HTML template
├── package.json                  # Dependencies & scripts
├── vite.config.js               # Vite configuration
└── cypress.config.js            # Cypress configuration
```

---

## 🎨 PrimeVue Components

This application uses PrimeVue for a polished, professional UI.

### Components Used

**Form Elements:**
- `InputText` - Text inputs
- `Dropdown` - Select dropdowns
- `Chip` - Tag/chip display for qualities
- `Textarea` - Multi-line text input
- `Button` - Action buttons

**Layout:**
- `Card` - Content containers
- `Divider` - Visual separators
- `Accordion` / `AccordionTab` - Collapsible content

**Feedback:**
- `Toast` - Notification messages
- `ProgressSpinner` - Loading indicator
- `Message` - Inline messages

**Navigation:**
- Custom navigation using PrimeVue Button components

### Adding More PrimeVue Components

**1. Import globally in `main.js`:**
```javascript
import Dialog from 'primevue/dialog'
app.component('Dialog', Dialog)
```

**2. Or import locally in component:**
```vue
<script setup>
import Dialog from 'primevue/dialog'
</script>

<template>
  <Dialog v-model:visible="showDialog">
    Content here
  </Dialog>
</template>
```

**3. Browse available components:** [PrimeVue Documentation](https://primevue.org/)

---

## 🛠️ Development

### Running Dev Server

```bash
cd frontend
npm run dev
```

Runs at: http://localhost:5173

### Hot Module Replacement

Vite provides instant HMR - edit any `.vue` file and see changes without page refresh!

---

### Component Development

**Create new component in `src/components/`:**

```vue
<template>
  <Card>
    <template #title>{{ title }}</template>
    <template #content>
      <p>{{ content }}</p>
    </template>
  </Card>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: String,
  content: String
})

const emit = defineEmits(['action'])
</script>

<style scoped>
/* Component-specific styles */
</style>
```

**Use Composition API with `<script setup>`:**
- More concise syntax
- Better TypeScript support
- Automatic component registration

---

### Adding Routes

In `src/router/index.js`:

```javascript
{
  path: '/your-route',
  name: 'YourRoute',
  component: () => import('../views/YourView.vue')
}
```

**Lazy loading** with `import()` improves initial load time.

---

### API Integration

The API service is centralized in `src/services/api.js`:

```javascript
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
```

**Usage in components:**
```vue
<script setup>
import api from '@/services/api'

const generateCompliment = async () => {
  try {
    const result = await api.generateCompliment(formData)
    // Handle result
  } catch (error) {
    console.error('Error:', error)
  }
}
</script>
```

---

## 🎨 Customization

### Theme & Colors

PrimeVue theme is configured in `main.js`:

```javascript
import 'primevue/resources/themes/lara-light-blue/theme.css'
```

**Available themes:**
- `lara-light-blue` (current)
- `lara-dark-blue`
- `lara-light-purple`
- `lara-dark-purple`
- Many more at [PrimeVue Themes](https://primevue.org/theming/)

**Custom CSS variables in `App.vue`:**
```css
:root {
  --primary-color: #3b82f6;
  --surface-ground: #f8fafc;
  --text-color: #334155;
}
```

**Use PrimeVue Designer:** [designer.primevue.org](https://designer.primevue.org) to create custom themes.

---

### Customize Relationship Types

Edit `src/components/ComplimentForm.vue`:

```javascript
const relationships = ref([
  { label: 'Student', value: 'student' },
  { label: 'Child', value: 'child' },
  { label: 'Employee', value: 'employee' },
  { label: 'Team Member', value: 'team_member' },
  { label: 'Friend', value: 'friend' },
  // Add more here
])
```

---

### Customize Tone Options

Edit `src/components/ComplimentForm.vue`:

```javascript
const tones = ref([
  { label: 'Warm', value: 'warm' },
  { label: 'Enthusiastic', value: 'enthusiastic' },
  { label: 'Calm', value: 'calm' },
  { label: 'Professional', value: 'professional' },
  // Add more here
])
```

---

## 🧪 Testing

### Cypress E2E Testing

The project includes comprehensive Cypress tests.

[![Cypress Dashboard](https://img.shields.io/endpoint?url=https://cloud.cypress.io/badge/detailed/jkecp8&style=for-the-badge&logo=cypress)](https://cloud.cypress.io/projects/jkecp8/runs)

### Prerequisites

**Start the application:**
```bash
# Option 1: Docker Compose
docker-compose up

# Option 2: Manual
# Terminal 1 - Backend
cd backend && python main.py

# Terminal 2 - Frontend
cd frontend && npm run dev
```

**Verify services:**
```bash
curl http://localhost:5173     # Frontend
curl http://localhost:8000/health  # Backend
```

---

### Running Tests

```bash
cd frontend

# Headless mode (CI/CD)
npm run test

# Interactive Test Runner
npm run test:open

# Headed mode (see browser)
npm run test:headed
```

---

### Test Structure

**Location:** `cypress/e2e/`

**Test files:**
- `compliment.cy.js` - Compliment generation flow
- `navigation.cy.js` - Route navigation
- `api.cy.js` - API health checks
- `external_links.cy.js` - External link validation

**Example test:**
```javascript
describe('Compliment Generator', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('generates a compliment successfully', () => {
    cy.get('input[placeholder*="name"]').type('John')
    cy.get('.p-dropdown').first().click()
    cy.contains('Student').click()
    cy.get('input[placeholder*="quality"]').type('creative{enter}')
    cy.get('textarea').type('completed an art project')
    cy.get('button').contains('Generate').click()
    cy.get('.compliment-display').should('be.visible')
  })
})
```

---

### Custom Commands

Located in `cypress/support/commands.js`:

```javascript
// Example custom command
Cypress.Commands.add('fillComplimentForm', (data) => {
  cy.get('input[placeholder*="name"]').type(data.name)
  cy.get('.p-dropdown').first().click()
  cy.contains(data.relationship).click()
  // ... more form filling
})

// Usage in tests
cy.fillComplimentForm({
  name: 'John',
  relationship: 'Student'
})
```

---

### Test Configuration

**`cypress.config.js`:**
```javascript
{
  e2e: {
    baseUrl: 'http://localhost:5173',
    supportFile: 'cypress/support/e2e.js'
  }
}
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Check what's using port 5173
lsof -i :5173

# Kill it (replace PID)
kill -9 <PID>

# Or use different port
npm run dev -- --port 3000
```

---

### Dependencies Issues

```bash
# Clear and reinstall
rm -rf node_modules package-lock.json
npm install

# Clear npm cache if still having issues
npm cache clean --force
npm install
```

---

### Backend Connection Error

**"Network Error" or CORS errors:**

1. **Verify backend is running:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Check `.env` file:**
   ```bash
   cat .env
   # Should have: VITE_API_URL=http://localhost:8000
   ```

3. **Restart dev server after changing `.env`:**
   ```bash
   npm run dev
   ```

4. **Check browser console (F12)** for detailed errors

---

### Build Errors

```bash
# Clear Vite cache
rm -rf node_modules/.vite

# Rebuild
npm run build

# If still failing, check for:
# - Syntax errors in Vue components
# - Missing imports
# - TypeScript errors (if using TS)
```

---

### Vite Cache Issues

```bash
# Clear Vite cache
rm -rf node_modules/.vite

# Restart dev server
npm run dev
```

---

### PrimeVue Components Not Rendering

**Check component registration in `main.js`:**
```javascript
import Button from 'primevue/button'
app.component('Button', Button)
```

**Verify CSS imports:**
```javascript
import 'primevue/resources/themes/lara-light-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
```

---

### Tests Failing

**"baseUrl not reachable":**
- Ensure frontend is running on http://localhost:5173
- Check `cypress.config.js` baseUrl matches

**Backend not responding:**
- Verify backend is running on http://localhost:8000
- Check backend health: `curl http://localhost:8000/health`

**Timeout errors:**
- Increase timeout in test: `cy.get('.element', { timeout: 10000 })`
- Check if backend/LLM is slow to respond

---

## 🚀 Deployment

For production deployment, see the [DEPLOYMENT.md](../DEPLOYMENT.md) guide which covers:
- Vercel, Netlify, GitHub Pages
- Environment variables for production
- Build optimization
- Static hosting with Nginx/Apache

---

## 📦 Build for Production

```bash
npm run build
```

Built files in `dist/` directory.

**Preview production build:**
```bash
npm run preview
```

---

## 🎯 Performance Tips

1. **Lazy load routes:**
   ```javascript
   component: () => import('../views/YourView.vue')
   ```

2. **Code splitting** - Vite automatically splits code by route

3. **Image optimization:**
   - Use WebP format
   - Compress images before adding

4. **Bundle analysis:**
   ```bash
   npm run build -- --mode analyze
   ```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
