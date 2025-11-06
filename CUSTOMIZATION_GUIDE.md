# Fourball Players Analysis Tool - Customization Guide

This guide will help you quickly customize the dashboard's appearance and player data without touching the core functionality.

## Table of Contents

1. [Changing Colors and Theme](#changing-colors-and-theme)
2. [Updating Player Data](#updating-player-data)
3. [Modifying Component Styles](#modifying-component-styles)
4. [Adding Custom Fonts](#adding-custom-fonts)
5. [Updating Charts and Images](#updating-charts-and-images)
6. [Advanced Customization](#advanced-customization)

---

## Changing Colors and Theme

All color and branding configuration is in **`static/theme.css`**.

### Quick Color Changes

Open `static/theme.css` and modify these CSS variables:

```css
:root {
    /* Primary Brand Colors */
    --color-primary-bg: #024035;           /* Main background */
    --color-primary-dark: #012A22;         /* Darker shade */
    --color-accent: #F6E2AD;                /* Accent (gold) */
    --color-text: #FFFFFF;                  /* Main text */
    --color-text-secondary: #D1D5DB;        /* Secondary text */
}
```

### Example: Blue and Orange Theme

```css
:root {
    --color-primary-bg: #1e3a8a;           /* Deep blue */
    --color-primary-dark: #1e293b;         /* Darker blue */
    --color-accent: #f97316;                /* Orange */
    --color-text: #FFFFFF;
    --color-text-secondary: #94a3b8;
}
```

### Example: Dark Gray and Teal Theme

```css
:root {
    --color-primary-bg: #1a1a1a;           /* Dark gray */
    --color-primary-dark: #0a0a0a;         /* Black */
    --color-accent: #14b8a6;                /* Teal */
    --color-text: #FFFFFF;
    --color-text-secondary: #9ca3af;
}
```

### Example: Light Theme

```css
:root {
    --color-primary-bg: #f8f9fa;           /* Light gray */
    --color-primary-dark: #e9ecef;         /* Lighter gray */
    --color-accent: #0d6efd;                /* Blue */
    --color-text: #212529;                  /* Dark text */
    --color-text-secondary: #6c757d;
}
```

### Adjust Card Transparency

Make cards more or less visible:

```css
:root {
    /* More visible cards */
    --color-card-bg: rgba(255, 255, 255, 0.15);

    /* Very subtle cards */
    --color-card-bg: rgba(255, 255, 255, 0.02);
}
```

---

## Updating Player Data

Player information is stored in **`data/player_summaries.json`**.

### JSON Structure

```json
{
  "Player Name": {
    "bio": "Career overview and accomplishments",
    "strengths": "Key statistical strengths and advantages",
    "weaknesses": "Areas needing improvement",
    "recent_form": "Last 20/50/100 round trends",
    "playing_style": "How the player approaches the game",
    "key_stat": "F_SG_Total: 1.45"
  }
}
```

### Adding a New Player

1. Open `data/player_summaries.json`
2. Add a new entry:

```json
{
  "John Doe": {
    "bio": "PGA Tour professional with 3 career wins",
    "strengths": "Elite driver (F_SG_OTT: 0.85), Strong iron play",
    "weaknesses": "Putting under pressure, Short game inconsistency",
    "recent_form": "Improving - Top 20 in last 5 events",
    "playing_style": "Aggressive off the tee, strategic approach",
    "key_stat": "F_SG_Total: 1.22"
  }
}
```

### Key Statistics Explained

- **F_SG_Total**: Overall strokes gained (higher is better)
- **F_SG_OTT**: Off-the-tee strokes gained (driving)
- **F_SG_APP**: Approach play strokes gained (irons)
- **F_SG_ARG**: Around-the-green strokes gained (chipping)
- **F_SG_PUTT**: Putting strokes gained

### Modifying Existing Players

Simply edit the values in the JSON file. The dashboard will automatically display updated information.

---

## Modifying Component Styles

Component styling is in **`static/styles.css`**.

### Navigation Buttons

Change button hover effects:

```css
.nav-button:hover {
    color: var(--color-accent);
    transform: translateY(-2px);        /* Lift on hover */
    transform: scale(1.05);             /* Or scale instead */
}
```

### Card Hover Effects

Modify card interactions:

```css
.section-card:hover {
    background: var(--color-card-hover);
    border-color: var(--color-card-border-hover);
    transform: translateY(-8px);        /* Increase lift */
    box-shadow: 0 12px 48px var(--color-accent-shadow);  /* Bigger shadow */
}
```

### Table Styling

Customize table appearance:

```css
.summary-table th {
    padding: 20px;                      /* More padding */
    font-size: 16px;                    /* Larger text */
}

.summary-table tbody tr:hover {
    transform: translateX(8px);         /* Bigger slide on hover */
}
```

---

## Adding Custom Fonts

### Using Google Fonts

1. Browse fonts at https://fonts.google.com
2. Select a font and copy the `<link>` tag
3. Add to `fourball_dashboard.html` in the `<head>` section:

```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

4. Update `static/theme.css`:

```css
body {
    font-family: 'Montserrat', sans-serif;
    /* ... */
}
```

### Popular Font Combinations

**Professional & Clean:**
```css
body { font-family: 'Roboto', sans-serif; }
h1, h2, h3 { font-family: 'Roboto Slab', serif; }
```

**Modern & Bold:**
```css
body { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Poppins', sans-serif; }
```

**Elegant & Refined:**
```css
body { font-family: 'Lato', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }
```

---

## Updating Charts and Images

Charts are stored as static PNG files in the **`static/`** directory.

### Current Chart Files

- `bubble_chart.png` - Performance map
- `position_range.png` - Position analysis chart
- `top_finish.png` - Top finish probabilities
- `leaderboard_table.html` - Leaderboard data table
- `table_data.html` - Player comparison table

### Replacing Charts

1. **Generate new chart** using your preferred tool (Python/matplotlib, R, Excel, etc.)
2. **Save with the same filename** in the `static/` directory
3. **Recommended dimensions:** 1200x800 pixels or higher
4. **File format:** PNG with transparent background (if desired)

### Adding New Charts

1. Add image to `static/` directory
2. Reference in HTML:

```html
<div class="chart-container">
    <img src="static/your_new_chart.png" alt="Chart Description">
</div>
```

---

## Advanced Customization

### Adding a Background Image

In `static/theme.css`:

```css
body {
    font-family: 'Inter', sans-serif;
    background-color: var(--color-primary-bg);
    background-image: url('path/to/image.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}
```

### Creating Custom Gradients

Define reusable gradients in `theme.css`:

```css
.gradient-custom {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

Use in HTML by adding the class: `class="gradient-custom"`

### Responsive Design

Styles automatically adjust for mobile devices. To customize breakpoints, edit `static/styles.css`:

```css
@media (max-width: 768px) {
    /* Tablet styles */
}

@media (max-width: 640px) {
    /* Mobile styles */
}
```

### Animation Speeds

Adjust hover and transition speeds in `static/styles.css`:

```css
.nav-button {
    transition: all 0.5s ease;  /* Slower (was 0.3s) */
}

.section-card {
    transition: all 0.2s ease;  /* Faster (was 0.3s) */
}
```

---

## Common Customization Scenarios

### Scenario 1: Rebrand for Different Tournament

1. Change colors in `static/theme.css`
2. Update title in `fourball_dashboard.html` line 37
3. Update player data in `data/player_summaries.json`
4. Replace chart images in `static/`

**Time estimate:** 15-30 minutes

### Scenario 2: Create Multiple Team Versions

1. Duplicate entire project folder
2. Rename folder (e.g., `Team_A_Dashboard`, `Team_B_Dashboard`)
3. Customize each version's `theme.css` and player data
4. Deploy each as separate Railway instance

**Time estimate:** 10 minutes per team

### Scenario 3: White-Label for Client

1. Replace all color variables with client brand colors
2. Update fonts to match client brand guidelines
3. Remove or replace logo/branding text
4. Update `server.py` authentication credentials

**Time estimate:** 30-60 minutes

---

## Testing Your Changes

### Local Testing

1. Save all changes
2. Refresh browser (Ctrl+R or Cmd+R)
3. Hard refresh if styles don't update (Ctrl+Shift+R or Cmd+Shift+R)

### Browser DevTools

- **Chrome/Firefox:** Press F12
- **Inspect elements** to see applied styles
- **Test color changes** in real-time before updating CSS

---

## Troubleshooting

### Colors Not Updating

1. **Hard refresh** the page (Ctrl+Shift+R)
2. **Check CSS file path** in HTML (should be `static/theme.css`)
3. **Verify CSS syntax** - missing semicolons or quotes cause issues

### Player Data Not Showing

1. **Validate JSON** at https://jsonlint.com
2. **Check for typos** in player names
3. **Ensure proper quotation marks** (use " not ' in JSON)

### Charts Not Loading

1. **Verify file paths** - should be `static/filename.png`
2. **Check file permissions** - ensure files are readable
3. **Confirm file extensions** - case-sensitive on Linux/Railway

---

## Quick Reference: Files to Edit

| What to Change | File to Edit | Time |
|----------------|-------------|------|
| Colors & theme | `static/theme.css` | 5 min |
| Player data | `data/player_summaries.json` | 10 min |
| Component styling | `static/styles.css` | 15 min |
| Page title | `fourball_dashboard.html` | 2 min |
| Charts | `static/*.png` | 20 min |

---

## Need More Help?

- **CSS Variables:** https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
- **JSON Format:** https://www.json.org/json-en.html
- **Color Picker:** https://htmlcolorcodes.com
- **Railway Docs:** https://docs.railway.com

---

**Happy Customizing! 🎨**
