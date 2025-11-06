# Railway Deployment Guide

Quick guide to deploy Fourball Players Analysis Tool to Railway.

## Prerequisites

- GitHub account with your code pushed (✅ Done: https://github.com/PiinkovaIiro/fourball-players-dashboard)
- Railway account (sign up at https://railway.app if needed)

## Step-by-Step Deployment

### 1. Create New Railway Project

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose **`fourball-players-dashboard`** from your repositories
5. Railway will auto-detect the configuration from `railway.json`

### 2. Set Environment Variables

In your Railway project settings, add these variables:

```
DASHBOARD_USERNAME=your_username
DASHBOARD_PASSWORD=your_secure_password
PORT=8000
```

**To set variables:**
1. Click on your service in Railway
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add each variable above

### 3. Deploy

Railway will automatically:
- Detect `railway.json` configuration
- Run `python3 server.py` as the start command
- Deploy on port 8000
- Set up health checks via `/health` endpoint

### 4. Access Your Dashboard

1. Railway will provide a public URL (e.g., `https://fourball-players-dashboard-production.up.railway.app`)
2. Navigate to: `https://[your-url]/fourball_dashboard.html`
3. Login with the credentials you set in environment variables

## Configuration Files

- **`railway.json`**: Defines the build and start commands
- **`server.py`**: HTTP server with authentication
- **`.railwayignore`**: Files excluded from deployment

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DASHBOARD_USERNAME` | Login username | `fourball` |
| `DASHBOARD_PASSWORD` | Login password | `SecurePass123!` |
| `PORT` | Server port | `8000` (default) |

## Troubleshooting

### Deployment Fails

- Check Railway build logs for errors
- Verify `railway.json` exists in root directory
- Ensure `server.py` is executable

### Can't Access Dashboard

- Verify environment variables are set correctly
- Check the Railway URL is correct
- Ensure you're navigating to `/fourball_dashboard.html`

### Authentication Not Working

- Double-check `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` variables
- Try redeploying after setting variables
- Check browser isn't caching old credentials

## Auto-Deployment

Railway automatically redeploys when you push to the `main` branch on GitHub:

```bash
git add .
git commit -m "Update dashboard"
git push origin main
```

Railway will detect the push and redeploy automatically.

## Health Check

Railway monitors your app via the `/health` endpoint (unauthenticated).

Test locally:
```bash
curl http://localhost:8000/health
```

Expected response: `OK`

## Custom Domain (Optional)

1. In Railway project settings, go to **"Settings"**
2. Click **"Generate Domain"** or add your custom domain
3. Follow Railway's instructions for DNS configuration

## Support

- Railway Docs: https://docs.railway.com
- Project Issues: https://github.com/PiinkovaIiro/fourball-players-dashboard/issues

---

**Your dashboard is now live and ready to use!** 🚀
