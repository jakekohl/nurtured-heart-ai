# Vercel Deployment Guide

## Overview

Your application is now configured to use:
- **Local Development**: Ollama (via Docker Compose)
- **Production**: Google Gemini AI (via Vercel)

## Prerequisites

1. **Google AI Studio Account**: You need a Google account to access the Gemini API
2. **Vercel Account**: Your application is already deployed on Vercel
3. **Environment Variables**: You'll need to configure them in Vercel

## Step 1: Get Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API Key"** in the top right
4. Click **"Create API Key"**
5. Choose **"Create API key in new project"** or select an existing project
6. Copy the generated API key (starts with `AIza...`)

## Step 2: Configure Vercel Environment Variables

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Find your project and click on it
3. Go to **Settings** → **Environment Variables**
4. Add the following environment variables:

### Required Variables:
```
AI_SERVICE = gemini
GEMINI_API_KEY = your_actual_api_key_from_step_1
GEMINI_MODEL = gemini-1.5-flash
CORS_ORIGINS = your_frontend_vercel_url
```

### Optional Variables:
```
TEMPERATURE = 0.7
```

## Step 3: Deploy Backend Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feature: add dual AI service support for Ollama and Gemini"
   git push origin main
   ```

2. **Vercel will automatically deploy** when you push to main branch

## Step 4: Deploy Frontend Changes

If you need to update the frontend to point to the new backend URL:

1. Go to your frontend Vercel project settings
2. Add environment variable:
   ```
   VITE_API_URL = your_backend_vercel_url
   ```
3. Redeploy the frontend

## Step 5: Test the Deployment

1. **Test the health endpoint**:
   ```bash
   curl https://your-backend-url.vercel.app/health
   ```

   Expected response:
   ```json
   {
     "api": "healthy",
     "llm": {
       "service": "gemini",
       "available": true,
       "installed_models": ["gemini-1.5-flash", ...],
       "required_model": "gemini-1.5-flash"
     },
     "email_service": false
   }
   ```

2. **Test compliment generation**:
   ```bash
   curl -X POST https://your-backend-url.vercel.app/api/generate \
     -H "Content-Type: application/json" \
     -d '{
       "recipient_name": "Test User",
       "relationship": "friend",
       "qualities": ["kind", "thoughtful"],
       "context": "helping me move",
       "tone": "warm"
     }'
   ```

## Local Development

To run locally with Ollama:

1. **Start the services**:
   ```bash
   docker-compose up
   ```

2. **The system will automatically use Ollama** since `AI_SERVICE=ollama` is set in docker-compose.yml

3. **Test locally**:
   ```bash
   curl http://localhost:8000/health
   ```

## Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY environment variable is required"**
   - Make sure you've added the `GEMINI_API_KEY` to Vercel environment variables
   - Redeploy after adding the variable

2. **"Unknown AI service"**
   - Ensure `AI_SERVICE=gemini` is set in Vercel environment variables

3. **CORS errors**
   - Update `CORS_ORIGINS` in Vercel to include your frontend URL
   - Make sure frontend `VITE_API_URL` points to your backend URL

4. **API rate limits**
   - Google Gemini has rate limits. Check your usage in Google AI Studio
   - Consider implementing retry logic if needed

### Environment Variable Checklist:

✅ `AI_SERVICE` = `gemini`  
✅ `GEMINI_API_KEY` = `your_api_key`  
✅ `GEMINI_MODEL` = `gemini-1.5-flash`  
✅ `CORS_ORIGINS` = `your_frontend_url`  

## Monitoring

1. **Check Vercel Function Logs**:
   - Go to your project → Functions tab
   - Monitor for any errors or timeouts

2. **Monitor API Usage**:
   - Check Google AI Studio for API usage and limits
   - Monitor Vercel bandwidth and function execution time

## Next Steps

1. **Test thoroughly** in both local and production environments
2. **Monitor performance** and adjust temperature/model settings as needed
3. **Set up monitoring** for API usage and costs
4. **Consider implementing** caching for frequently requested compliments

Your dual AI service setup is now complete! 🎉
