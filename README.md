# Fourball Players Analysis Tool

A professional golf player analysis dashboard featuring performance metrics, head-to-head comparisons, and tournament predictions.

## 🚀 Quick Start

### Local Development

1. **Start the server:**
   ```bash
   python3 server.py
   ```

2. **Open in browser:**
   Navigate to `http://localhost:8000`

3. **Login:**
   - Default username: `cleeksgc` (or set via `DASHBOARD_USERNAME` environment variable)
   - Password: Set via `DASHBOARD_PASSWORD` environment variable

### View the Dashboard

Open `http://localhost:8000/fourball_dashboard.html` in your web browser.

## 📊 Features

- **Player Overview**: Comprehensive player statistics and profiles
- **Leaderboard**: Tournament standings and rankings
- **Position Analysis**: Expected finishing positions with percentile ranges
- **Top Finish Probabilities**: Win probability and top-5/10 finish odds
- **Performance Map**: Visual bubble chart of player performance vs. skill
- **Head-to-Head Comparison**: Direct player comparisons with advantage indicators

## 🎨 Customization

### Quick Theme Changes

Edit `static/theme.css` to customize colors and appearance:

```css
:root {
    --color-primary-bg: #024035;     /* Main background */
    --color-accent: #F6E2AD;          /* Accent color (gold) */
    --color-text: #FFFFFF;            /* Text color */
}
```

See `CUSTOMIZATION_GUIDE.md` for detailed customization instructions.

### Update Player Data

Edit `data/player_summaries.json` to add or modify player information:

```json
{
  "Player Name": {
    "bio": "Career overview and accomplishments",
    "strengths": "Key statistical strengths",
    "weaknesses": "Areas needing improvement",
    "recent_form": "Last 20/50/100 round trends",
    "playing_style": "Approach to the game",
    "key_stat": "F_SG_Total: [value]"
  }
}
```

## 📁 Project Structure

```
Fourball_Players_Analysis_Tool/
├── fourball_dashboard.html    # Main dashboard page
├── server.py                  # HTTP server with authentication
├── data/
│   └── player_summaries.json  # Player profiles and statistics
├── static/
│   ├── theme.css              # Color scheme and branding
│   ├── styles.css             # Component styles
│   ├── *.png                  # Chart images
│   ├── *.html                 # Data tables
│   └── h2h/                   # Head-to-head comparison data
├── railway.json               # Railway deployment config
└── requirements.txt           # Python dependencies (minimal)
```

## 🚂 Railway Deployment

### Prerequisites

1. **Create a GitHub repository** and push this code
2. **Create a Railway account** at https://railway.app

### Deployment Steps

1. **Connect to Railway:**
   - Log into Railway
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Set Environment Variables:**
   ```
   DASHBOARD_USERNAME=your_username
   DASHBOARD_PASSWORD=your_secure_password
   PORT=8000
   ```

3. **Deploy:**
   - Railway will automatically detect `railway.json`
   - Deployment starts automatically
   - Access your dashboard at the provided Railway URL

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DASHBOARD_USERNAME` | Login username | Yes |
| `DASHBOARD_PASSWORD` | Login password | Yes |
| `PORT` | Server port (default: 8000) | No |

## 🔒 Authentication

The dashboard is protected by HTTP Basic Authentication. Set credentials using environment variables:

```bash
export DASHBOARD_USERNAME="your_username"
export DASHBOARD_PASSWORD="your_password"
python3 server.py
```

## 📖 Documentation

- **CUSTOMIZATION_GUIDE.md** - Detailed customization instructions
- **static/theme.css** - Color and theme configuration (with inline comments)
- **static/styles.css** - Component styling documentation

## 🛠 Technology Stack

- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
- **Backend:** Python 3 (built-in HTTP server)
- **Deployment:** Railway (or any Python hosting platform)
- **Data:** JSON-based player profiles

## 📝 License

This project is provided as-is for analysis and visualization purposes.

## 🤝 Support

For customization questions or deployment help, refer to:
1. `CUSTOMIZATION_GUIDE.md` for styling and data updates
2. Railway documentation for deployment issues: https://docs.railway.com

---

**Built for rapid deployment and easy customization**
