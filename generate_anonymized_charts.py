#!/usr/bin/env python3
"""
Generate anonymized chart images for Fourball Players Analysis Tool
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

# Set style
plt.style.use('dark_background')

# Read player data from HTML tables
def load_player_data():
    """Load player statistics from table_data.html"""
    with open('static/table_data.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header

    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 8:
            data.append({
                'player': cols[0].text.strip(),
                'F_SG_Total': float(cols[1].text.strip()),
                'win_probability': float(cols[2].text.strip()),
                'top_5_probability': float(cols[3].text.strip()),
                'top_10_probability': float(cols[4].text.strip()),
                'avg_position': float(cols[5].text.strip()),
                'position_20th': int(cols[6].text.strip()),
                'position_80th': int(cols[7].text.strip())
            })

    return pd.DataFrame(data)

# Color scheme - Majesticks style
COLORS = {
    'bg': '#1a0f3e',
    'secondary': '#2b1854',
    'accent': '#00d4ff',
    'accent_hover': '#5ce4ff',
    'text': '#ffffff'
}

def create_position_range_chart(df):
    """Create position range chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['secondary'])

    # Sort by average position
    df_sorted = df.sort_values('avg_position')

    # Plot ranges
    for idx, row in df_sorted.iterrows():
        y_pos = len(df_sorted) - idx - 1

        # Draw range line
        ax.plot([row['position_20th'], row['position_80th']], [y_pos, y_pos],
                color=COLORS['accent'], linewidth=3, alpha=0.6, zorder=1)

        # Draw average marker
        ax.scatter(row['avg_position'], y_pos, s=200,
                  color=COLORS['accent_hover'], edgecolors=COLORS['text'],
                  linewidth=2, zorder=2, marker='D')

        # Add player name
        ax.text(-2, y_pos, row['player'],
               va='center', ha='right', fontsize=10,
               color=COLORS['text'], weight='bold')

    ax.set_xlabel('Position', fontsize=14, color=COLORS['accent'], weight='bold')
    ax.set_title('EXPECTED FINISHING POSITION RANGES',
                fontsize=18, color=COLORS['accent'], weight='bold', pad=20)

    ax.set_yticks([])
    ax.set_xlim(0, max(df_sorted['position_80th'].max() + 5, 55))
    ax.grid(axis='x', alpha=0.2, color=COLORS['accent'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(COLORS['accent'])
    ax.tick_params(colors=COLORS['text'])

    plt.tight_layout()
    plt.savefig('static/position_range.png', dpi=150, facecolor=COLORS['bg'])
    plt.close()
    print("✓ Generated position_range.png")

def create_top_finish_chart(df):
    """Create top finish probabilities chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['secondary'])

    # Sort by win probability
    df_sorted = df.sort_values('win_probability', ascending=True).tail(12)

    # Create grouped bar chart
    x = np.arange(len(df_sorted))
    width = 0.25

    bars1 = ax.barh(x - width, df_sorted['win_probability'], width,
                    label='Win %', color=COLORS['accent_hover'], alpha=0.9)
    bars2 = ax.barh(x, df_sorted['top_5_probability'], width,
                    label='Top 5 %', color=COLORS['accent'], alpha=0.8)
    bars3 = ax.barh(x + width, df_sorted['top_10_probability'], width,
                    label='Top 10 %', color=COLORS['accent'], alpha=0.6)

    ax.set_yticks(x)
    ax.set_yticklabels(df_sorted['player'], fontsize=10, color=COLORS['text'])
    ax.set_xlabel('Probability (%)', fontsize=14, color=COLORS['accent'], weight='bold')
    ax.set_title('TOP FINISH PROBABILITIES',
                fontsize=18, color=COLORS['accent'], weight='bold', pad=20)

    ax.legend(loc='lower right', framealpha=0.9, facecolor=COLORS['secondary'],
             edgecolor=COLORS['accent'], fontsize=10)
    ax.grid(axis='x', alpha=0.2, color=COLORS['accent'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['accent'])
    ax.spines['bottom'].set_color(COLORS['accent'])
    ax.tick_params(colors=COLORS['text'])

    plt.tight_layout()
    plt.savefig('static/top_finish.png', dpi=150, facecolor=COLORS['bg'])
    plt.close()
    print("✓ Generated top_finish.png")

def create_bubble_chart(df):
    """Create performance bubble chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['secondary'])

    # Create bubble chart
    scatter = ax.scatter(df['F_SG_Total'], df['avg_position'],
                        s=df['win_probability'] * 200,  # Size based on win probability
                        c=df['win_probability'], cmap='cool',
                        alpha=0.7, edgecolors=COLORS['accent'], linewidth=2)

    # Add labels for top players
    for idx, row in df.iterrows():
        if row['win_probability'] > 2.0 or row['F_SG_Total'] > 1.0:
            ax.annotate(row['player'],
                       xy=(row['F_SG_Total'], row['avg_position']),
                       xytext=(10, 10), textcoords='offset points',
                       fontsize=9, color=COLORS['text'], weight='bold',
                       bbox=dict(boxstyle='round,pad=0.3',
                                facecolor=COLORS['secondary'],
                                edgecolor=COLORS['accent'], alpha=0.8))

    ax.set_xlabel('Strokes Gained Total (F_SG_Total)',
                 fontsize=14, color=COLORS['accent'], weight='bold')
    ax.set_ylabel('Average Position',
                 fontsize=14, color=COLORS['accent'], weight='bold')
    ax.set_title('SKILL VS POSITION - PERFORMANCE MAP',
                fontsize=18, color=COLORS['accent'], weight='bold', pad=20)

    # Invert y-axis (lower position is better)
    ax.invert_yaxis()

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
    cbar.set_label('Win Probability (%)', color=COLORS['accent'], weight='bold')
    cbar.ax.tick_params(colors=COLORS['text'])

    ax.grid(alpha=0.2, color=COLORS['accent'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['accent'])
    ax.spines['bottom'].set_color(COLORS['accent'])
    ax.tick_params(colors=COLORS['text'])

    plt.tight_layout()
    plt.savefig('static/bubble_chart.png', dpi=150, facecolor=COLORS['bg'])
    plt.close()
    print("✓ Generated bubble_chart.png")

def main():
    print("Generating anonymized chart images...")
    print("=" * 60)

    # Load data
    df = load_player_data()
    print(f"Loaded data for {len(df)} players")

    # Generate charts
    create_position_range_chart(df)
    create_top_finish_chart(df)
    create_bubble_chart(df)

    print("=" * 60)
    print("✅ All charts generated successfully!")
    print("\nGenerated files:")
    print("  - static/position_range.png")
    print("  - static/top_finish.png")
    print("  - static/bubble_chart.png")

if __name__ == '__main__':
    main()
