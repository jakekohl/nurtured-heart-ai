# Frontend - Nurtured Heart Compliment Generator

Vue.js 3 frontend application for generating Nurtured Heart compliments with a beautiful, responsive UI.

## 🛠️ Tech Stack

- **Vue.js 3** - Progressive JavaScript framework
- **PrimeVue** - UI component library
- **Vite** - Next-generation frontend tooling
- **Vue Router** - Official routing library

## 📋 Requirements

- Node.js 18+ and npm
- Backend API running (default: http://localhost:8000)

## 🚀 Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Create Environment File

Create a `.env` file in the `frontend/` directory:

```bash
cat > .env << 'EOF'
VITE_API_URL=http://localhost:8000
EOF
```

## ⚙️ Configuration Options

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_URL` | `http://localhost:8000` | Backend API base URL |

### Update for Production

```env
VITE_API_URL=https://api.yourdomain.com
```

## 🎮 Running the Application

### Development Mode

```bash
npm run dev
```

Application runs at: **http://localhost:5173**

### Using Helper Script

```bash
cd ..  # Go to project root
./start-frontend.sh
```

### Custom Port

```bash
npm run dev -- --port 3000
```

## 🏗️ Build for Production

### Build

```bash
npm run build
```

Built files will be in `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ComplimentForm.vue      # Main form component
│   │   ├── ComplimentDisplay.vue   # Display generated compliment
│   │   ├── NavigationMenu.vue      # Navigation bar
│   │   └── AppFooter.vue          # Footer component
│   ├── views/
│   │   ├── GeneratorView.vue      # Main generator page
│   │   ├── AboutView.vue          # About page
│   │   ├── WhatIsNHA.vue         # NHA information page
│   │   └── FAQView.vue           # FAQ page
│   ├── router/
│   │   └── index.js              # Vue Router configuration
│   ├── services/
│   │   └── api.js                # API client
│   ├── App.vue                   # Root component
│   └── main.js                   # Application entry point
├── public/                       # Static assets
├── index.html                    # HTML template
├── package.json                  # Dependencies
├── vite.config.js               # Vite configuration
└── .env                         # Environment variables (create this)
```

## 🎨 PrimeVue Components Used

The application leverages PrimeVue components for a polished UI:

- **Form Elements:** InputText, Dropdown, Chips, Textarea, Button
- **Layout:** Card, Divider
- **Feedback:** Toast, ProgressSpinner, Tag
- **Navigation:** Menubar
- **Utilities:** Tooltip

### Adding More PrimeVue Components

1. Import in component:
   ```vue
   import Dialog from 'primevue/dialog';
   ```

2. Use in template:
   ```vue
   <Dialog v-model:visible="display">
     Content here
   </Dialog>
   ```

## 🛠️ Development

### Hot Module Replacement (HMR)

Vite provides instant HMR - edit any `.vue` file and see changes immediately without page refresh.

### Component Development

Create new components in `src/components/`:

```vue
<template>
  <div>
    <!-- Your template -->
  </div>
</template>

<script setup>
// Your logic
</script>

<style scoped>
/* Your styles */
</style>
```

### Add New Routes

In `src/router/index.js`:

```javascript
{
  path: '/your-route',
  name: 'YourRoute',
  component: () => import('../views/YourView.vue')
}
```

### API Integration

The API service is in `src/services/api.js`:

```javascript
export const generateCompliment = async (data) => {
  const response = await fetch(`${API_URL}/api/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
};
```

## 🎨 Customization

### Colors & Theme

PrimeVue theme is configured in `main.js`. To customize:

1. **Use PrimeVue Designer:** https://designer.primevue.org
2. **Or modify CSS variables** in `App.vue`:

```css
:root {
  --primary-color: #3b82f6;
  --surface-ground: #f8fafc;
  --text-color: #334155;
}
```

### Add Relationship Types

Edit `src/components/ComplimentForm.vue`:

```javascript
const relationships = ref([
  { label: 'Student', value: 'student' },
  { label: 'Child', value: 'child' },
  // Add more here
]);
```

### Modify Tone Options

Edit `src/components/ComplimentForm.vue`:

```javascript
const tones = ref([
  { label: 'Warm', value: 'warm' },
  { label: 'Enthusiastic', value: 'enthusiastic' },
  // Add more here
]);
```

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Check what's using port 5173
lsof -i :5173

# Use different port
npm run dev -- --port 3000
```

### Dependencies Issues

```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Backend Connection Error

1. Verify backend is running:
   ```bash
   curl http://localhost:8000/health
   ```

2. Check `.env` file has correct `VITE_API_URL`

3. Check browser console for CORS errors

### Build Errors

```bash
# Clean cache
rm -rf node_modules/.vite

# Rebuild
npm run build
```

### Vite Cache Issues

```bash
# Clear Vite cache
rm -rf node_modules/.vite

# Restart dev server
npm run dev
```

## 🧪 Testing

### Manual Testing Checklist

- [ ] Form validation works
- [ ] Compliment generation succeeds
- [ ] Copy button works
- [ ] Toast notifications appear
- [ ] Responsive on mobile
- [ ] All routes accessible
- [ ] Backend connection working

### Test API Connection

```javascript
// In browser console
fetch('http://localhost:8000/health')
  .then(r => r.json())
  .then(console.log)
```

## 🚀 Deployment

### Vercel

```bash
npm run build
# Then deploy dist/ folder to Vercel
```

Or use Vercel CLI:
```bash
npm i -g vercel
vercel
```

### Netlify

```bash
npm run build
# Then deploy dist/ folder to Netlify
```

Or use Netlify CLI:
```bash
npm i -g netlify-cli
netlify deploy --prod
```

### GitHub Pages

1. Update `vite.config.js`:
   ```javascript
   export default defineConfig({
     base: '/your-repo-name/',
     // ...
   });
   ```

2. Build and deploy:
   ```bash
   npm run build
   # Push dist/ to gh-pages branch
   ```

### Nginx (Self-hosted)

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### Environment Variables for Production

Create `.env.production`:

```env
VITE_API_URL=https://api.yourdomain.com
```

Build with production env:
```bash
npm run build
```

## 📦 Dependencies

### Main Dependencies

```json
{
  "vue": "^3.x",
  "vue-router": "^4.x",
  "primevue": "^3.x",
  "primeicons": "^7.x"
}
```

### Dev Dependencies

```json
{
  "@vitejs/plugin-vue": "^5.x",
  "vite": "^5.x"
}
```

## 🎯 Performance Tips

1. **Lazy Load Routes:**
   ```javascript
   component: () => import('../views/YourView.vue')
   ```

2. **Optimize Images:**
   - Use WebP format
   - Compress images before adding

3. **Code Splitting:**
   - Vite automatically splits code
   - Keep components modular

4. **Production Build:**
   - Minified and tree-shaken
   - Optimized for performance

## 📝 License

MIT

