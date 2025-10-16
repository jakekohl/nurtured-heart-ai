# 🚀 Deployment Guide

This guide covers deploying the Nurtured Heart Compliment Generator to production environments.

## 📋 Table of Contents

- [Overview](#overview)
- [Backend Deployment](#backend-deployment)
- [Frontend Deployment](#frontend-deployment)
- [Environment Variables](#environment-variables)
- [Platform-Specific Guides](#platform-specific-guides)
- [Testing Deployment](#testing-deployment)
- [Troubleshooting](#troubleshooting)

---

## Overview

### Architecture Options

**Option 1: Cloud API (Recommended for Vercel/Serverless)**
- Backend: Vercel/Railway/Render with Google Gemini API
- Frontend: Vercel/Netlify
- Best for: Easy deployment, no infrastructure management

**Option 2: Self-Hosted with Local Models**
- Backend: Docker + Ollama on VM (AWS/GCP/Azure)
- Frontend: Any static hosting
- Best for: Privacy, offline capability, cost control at scale

---

## Backend Deployment

### Vercel (Recommended - Serverless)

**Prerequisites:**
- Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Vercel account

**Steps:**

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy from backend directory:**
   ```bash
   cd backend
   vercel
   ```

3. **Configure environment variables in Vercel Dashboard:**
   - Go to Settings → Environment Variables
   - Add the following:

   ```
   AI_SERVICE=gemini
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-2.5-flash-lite
   TEMPERATURE=0.7
   CORS_ORIGINS=https://your-frontend-url.vercel.app
   ```

4. **Optional - Email configuration:**
   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   FROM_EMAIL=your-email@gmail.com
   ```

5. **Redeploy after setting environment variables:**
   ```bash
   vercel --prod
   ```

**Note:** The `vercel.json` file in the backend directory is already configured for FastAPI.

---

### Railway

**Steps:**

1. **Create new project on [Railway](https://railway.app/)**

2. **Connect your GitHub repository**

3. **Set root directory to `/backend`**

4. **Add environment variables:**
   ```
   AI_SERVICE=gemini
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-2.5-flash-lite
   TEMPERATURE=0.7
   CORS_ORIGINS=https://your-frontend-url.com
   HOST=0.0.0.0
   PORT=8000
   ```

5. **Deploy** - Railway will automatically detect Python and install dependencies

---

### Render

**Steps:**

1. **Create new Web Service on [Render](https://render.com/)**

2. **Connect repository**

3. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `cd backend && python main.py`
   - **Environment:** Python 3

4. **Add environment variables** (same as Vercel)

---

### Docker + VM (AWS/GCP/Azure)

For self-hosted deployment with Ollama:

**1. Prepare your VM:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose
```

**2. Create production docker-compose.yml:**
```yaml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama-data:/root/.ollama
    ports:
      - "11434:11434"
    restart: unless-stopped

  backend:
    build: ./backend
    environment:
      - AI_SERVICE=ollama
      - OLLAMA_HOST=http://ollama:11434
      - OLLAMA_MODEL=llama3.2:latest
      - TEMPERATURE=0.7
      - CORS_ORIGINS=https://yourdomain.com
      - HOST=0.0.0.0
      - PORT=8000
    ports:
      - "8000:8000"
    depends_on:
      - ollama
    restart: unless-stopped

volumes:
  ollama-data:
```

**3. Deploy:**
```bash
docker-compose up -d
```

**4. Pull Ollama model:**
```bash
docker exec -it <ollama-container> ollama pull llama3.2
```

**5. Configure reverse proxy (Nginx):**
```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Frontend Deployment

### Vercel (Recommended)

**Steps:**

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Build and deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. **Configure environment variable in Vercel Dashboard:**
   ```
   VITE_API_URL=https://your-backend-url.vercel.app
   ```

4. **Redeploy:**
   ```bash
   vercel --prod
   ```

---

### Netlify

**Steps:**

1. **Build the frontend:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy via Netlify CLI:**
   ```bash
   npm i -g netlify-cli
   netlify deploy --prod
   ```

3. **Or use the Netlify Dashboard:**
   - Connect repository
   - Build command: `npm run build`
   - Publish directory: `dist`
   - Environment variables: `VITE_API_URL=https://your-backend-url.com`

---

### GitHub Pages

**Steps:**

1. **Update `vite.config.js`:**
   ```javascript
   export default defineConfig({
     base: '/your-repo-name/',
     plugins: [vue()],
   })
   ```

2. **Build:**
   ```bash
   npm run build
   ```

3. **Deploy to gh-pages branch:**
   ```bash
   npm install -g gh-pages
   gh-pages -d dist
   ```

4. **Configure GitHub Pages** to serve from `gh-pages` branch

---

### Static Hosting (Nginx/Apache)

**Build:**
```bash
cd frontend
npm run build
```

**Nginx configuration:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /var/www/nurtured-heart-ai/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

**Apache configuration (.htaccess):**
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

---

## Environment Variables

### Backend Variables

#### Required (Gemini)
```env
AI_SERVICE=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite
CORS_ORIGINS=https://your-frontend-url.com
```

#### Required (Ollama)
```env
AI_SERVICE=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2:latest
CORS_ORIGINS=https://your-frontend-url.com
```

#### Optional
```env
TEMPERATURE=0.7
HOST=0.0.0.0
PORT=8000
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=your-email@gmail.com
```

### Frontend Variables

```env
VITE_API_URL=https://your-backend-url.com
```

### Getting API Keys

**Google Gemini API Key:**
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with Google account
3. Click "Get API Key"
4. Create API key in new or existing project
5. Copy the key (starts with `AIza...`)

**Gmail App Password (for email):**
1. Enable 2-Factor Authentication on your Google account
2. Go to https://myaccount.google.com/security
3. Security → 2-Step Verification → App passwords
4. Generate password for "Mail"
5. Use the 16-character password in `SMTP_PASSWORD`

---

## Platform-Specific Guides

### Vercel Full Stack Deployment

**Backend:**
1. Deploy backend to Vercel
2. Note the backend URL: `https://your-backend.vercel.app`
3. Configure environment variables in Vercel dashboard

**Frontend:**
1. Deploy frontend to Vercel
2. Set environment variable: `VITE_API_URL=https://your-backend.vercel.app`
3. Note the frontend URL: `https://your-frontend.vercel.app`

**Backend CORS Update:**
- Update backend environment variable: `CORS_ORIGINS=https://your-frontend.vercel.app`
- Redeploy backend

---

### Railway + Netlify

**Backend on Railway:**
1. Create new project, connect repo
2. Set root directory: `/backend`
3. Configure environment variables
4. Deploy and note the URL

**Frontend on Netlify:**
1. Connect repo
2. Build command: `npm run build`
3. Publish directory: `dist`
4. Base directory: `frontend`
5. Environment variable: `VITE_API_URL=<railway-backend-url>`

---

### Docker Compose (Self-Hosted)

**Complete stack with Ollama:**

```yaml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama-data:/root/.ollama
    ports:
      - "11434:11434"

  backend:
    build: ./backend
    environment:
      - AI_SERVICE=ollama
      - OLLAMA_HOST=http://ollama:11434
      - OLLAMA_MODEL=llama3.2:latest
      - CORS_ORIGINS=http://localhost:80
    ports:
      - "8000:8000"
    depends_on:
      - ollama

  frontend:
    build: ./frontend
    environment:
      - VITE_API_URL=http://localhost:8000
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  ollama-data:
```

**Deploy:**
```bash
docker-compose up -d

# Pull model
docker exec -it <ollama-container> ollama pull llama3.2
```

---

## Testing Deployment

### Backend Health Check

```bash
curl https://your-backend-url.com/health
```

**Expected response:**
```json
{
  "api": "healthy",
  "llm": {
    "service": "gemini",
    "available": true,
    "installed_models": ["gemini-1.5-flash", "..."],
    "required_model": "gemini-2.5-flash-lite"
  },
  "email_service": false
}
```

### Test Compliment Generation

```bash
curl -X POST https://your-backend-url.com/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_name": "Test User",
    "relationship": "friend",
    "qualities": ["kind", "thoughtful"],
    "context": "helping me with a project",
    "tone": "warm"
  }'
```

### Frontend Smoke Test

1. Open your deployed frontend URL
2. Fill out the compliment form
3. Generate a compliment
4. Verify the response appears

---

## Troubleshooting

### Backend Issues

**"GEMINI_API_KEY environment variable is required"**
- Ensure the variable is set in your hosting platform
- Redeploy after adding the variable
- Check for typos in the variable name

**"Unknown AI service"**
- Verify `AI_SERVICE` is set to either `ollama` or `gemini`
- Check for case sensitivity

**CORS Errors**
- Update `CORS_ORIGINS` to include your frontend URL
- Include both `http://` and `https://` if needed
- For multiple origins, comma-separate: `https://app.com,https://www.app.com`

**Email Not Sending**
- Verify all SMTP variables are set
- For Gmail, ensure you're using an App Password, not your regular password
- Check firewall rules allow outbound SMTP (port 587)

### Frontend Issues

**"Cannot connect to backend"**
- Verify `VITE_API_URL` points to correct backend URL
- Check backend is running and accessible
- Check browser console for detailed errors

**Blank page after deployment**
- Check browser console for errors
- Verify base path in `vite.config.js` matches deployment
- Clear browser cache

**Routes not working (404)**
- Configure hosting platform for SPA routing
- Ensure all routes redirect to `index.html`
- For Netlify, add `_redirects` file: `/*  /index.html  200`

### Performance Issues

**Slow response times**
- Check Gemini API rate limits in Google AI Studio
- Consider increasing function timeout (Vercel: 60s max on Pro)
- Monitor backend logs for bottlenecks

**Cold starts (serverless)**
- First request may be slow (~1-5 seconds)
- Consider implementing keep-alive pings
- Upgrade to paid hosting for faster cold starts

---

## Security Checklist

- [ ] Environment variables set in hosting platform (not in code)
- [ ] `.env` files are gitignored
- [ ] CORS origins restricted to your domains
- [ ] HTTPS enabled on frontend and backend
- [ ] API keys rotated regularly
- [ ] Gmail using App Passwords (not regular password)
- [ ] Rate limiting configured (if available)
- [ ] Backend logs monitored for suspicious activity

---

## Monitoring & Maintenance

### Recommended Monitoring

**Backend:**
- Function execution time (Vercel/Railway dashboards)
- Error rates and logs
- API usage (Google AI Studio for Gemini)
- Bandwidth and request counts

**Frontend:**
- Page load times
- JavaScript errors (browser console)
- Build sizes

### Cost Monitoring

**Google Gemini:**
- Free tier: 15 requests/minute, 1500 requests/day
- Monitor usage at [Google AI Studio](https://aistudio.google.com/)

**Vercel:**
- Free tier: 100GB bandwidth/month
- Monitor at Vercel dashboard

**Self-hosted:**
- VM costs (compute + storage)
- Bandwidth costs

---

## Next Steps After Deployment

1. **Test thoroughly** in production environment
2. **Set up monitoring** for errors and performance
3. **Monitor API costs** and usage
4. **Configure backups** (if using database in future)
5. **Set up domain** with custom DNS
6. **Enable HTTPS** (automatic on Vercel/Netlify)
7. **Consider CDN** for static assets (if self-hosting)

---

**Your application is now deployed! 🎉**

For local development setup, see the main [README.md](README.md).

