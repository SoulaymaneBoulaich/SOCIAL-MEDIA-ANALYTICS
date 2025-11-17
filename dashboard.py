import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from database import SocialMediaDB
import glob
from datetime import datetime

# ============================================================================
# CONFIGURATION & INITIALIZATION
# ============================================================================

# Color Palette - Modern Dark Theme
COLORS = {
    'bg_dark': '#0F1419',
    'bg_light': '#1A1F2E',
    'primary': '#00D9FF',
    'success': '#10B981',
    'warning': '#F59E0B',
    'danger': '#EF4444',
    'text_primary': '#FFFFFF',
    'text_secondary': '#9CA3AF',
    'border': '#374151'
}

# Initialize Dash app with external styling
app = dash.Dash(__name__, external_stylesheets=[])


# ============================================================================
# DATABASE LOADING
# ============================================================================

def find_latest_db():
    """Find the most recent social_media_*.db file"""
    dbs = sorted(glob.glob('social_media_*.db'), reverse=True)
    return dbs[0] if dbs else None


db_file = find_latest_db()
if db_file:
    db = SocialMediaDB(db_file)
    print(f"✅ Database loaded: {db_file}")
else:
    db = SocialMediaDB()
    print("⚠️  New database created")

df = db.get_all_posts()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _safe_count(df, label_value):
    """Safely count sentiments without KeyError"""
    if df.empty or 'sentiment_label' not in df.columns:
        return 0
    return int(df['sentiment_label'].eq(label_value).sum())


def create_sentiment_by_platform(df):
    """Stacked bar chart of sentiment distribution by platform"""
    if df.empty:
        return go.Figure().add_annotation(text="No data available")
    
    sentiment_counts = df.groupby(['platform', 'sentiment_label']).size().reset_index(name='count')
    
    # Map sentiment to colors
    color_map = {
        'positive': COLORS['success'],
        'neutral': COLORS['primary'],
        'negative': COLORS['danger']
    }
    
    fig = px.bar(
        sentiment_counts,
        x='platform',
        y='count',
        color='sentiment_label',
        title='Sentiment Distribution by Platform',
        color_discrete_map=color_map,
        barmode='stack',
        labels={'count': 'Number of Posts', 'platform': 'Platform'}
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['bg_light'],
        paper_bgcolor=COLORS['bg_dark'],
        font=dict(color=COLORS['text_primary'], family='Arial, sans-serif', size=12),
        title=dict(font=dict(size=18, color=COLORS['text_primary'])),
        hovermode='x unified',
        margin=dict(l=50, r=50, t=80, b=50),
        xaxis=dict(showgrid=False, gridcolor=COLORS['border']),
        yaxis=dict(showgrid=True, gridcolor=COLORS['border']),
        legend=dict(bgcolor='rgba(0,0,0,0)', bordercolor=COLORS['border'])
    )
    
    return fig


def create_sentiment_timeline(df):
    """Line chart showing sentiment trends over time"""
    if df.empty:
        return go.Figure().add_annotation(text="No data available")
    
    df_copy = df.copy()
    df_copy['created_utc'] = pd.to_datetime(df_copy['created_utc'])
    df_copy['date'] = df_copy['created_utc'].dt.date
    
    timeline_data = df_copy.groupby(['date', 'sentiment_label']).size().reset_index(name='count')
    
    color_map = {
        'positive': COLORS['success'],
        'neutral': COLORS['primary'],
        'negative': COLORS['danger']
    }
    
    fig = px.line(
        timeline_data,
        x='date',
        y='count',
        color='sentiment_label',
        title='Sentiment Trends Over Time',
        color_discrete_map=color_map,
        markers=True
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['bg_light'],
        paper_bgcolor=COLORS['bg_dark'],
        font=dict(color=COLORS['text_primary'], family='Arial, sans-serif', size=12),
        title=dict(font=dict(size=18, color=COLORS['text_primary'])),
        hovermode='x unified',
        margin=dict(l=50, r=50, t=80, b=50),
        xaxis=dict(showgrid=True, gridcolor=COLORS['border']),
        yaxis=dict(showgrid=True, gridcolor=COLORS['border'])
    )
    
    return fig


def create_platform_pie(df):
    """Pie chart showing post distribution across platforms"""
    if df.empty:
        return go.Figure().add_annotation(text="No data available")
    
    platform_counts = df['platform'].value_counts().reset_index()
    platform_counts.columns = ['platform', 'count']
    
    fig = px.pie(
        platform_counts,
        values='count',
        names='platform',
        title='Posts by Platform',
        color_discrete_sequence=[COLORS['danger'], COLORS['primary'], COLORS['success']]
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['bg_light'],
        paper_bgcolor=COLORS['bg_dark'],
        font=dict(color=COLORS['text_primary'], family='Arial, sans-serif', size=12),
        title=dict(font=dict(size=18, color=COLORS['text_primary'])),
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    return fig


def create_top_posts_table(df):
    """HTML table showing top 10 posts by score"""
    if df.empty:
        return html.Div(
            "No data available",
            style={'color': COLORS['text_secondary'], 'padding': '20px', 'textAlign': 'center'}
        )
    
    if 'score' not in df.columns:
        return html.Div(
            "No score data available",
            style={'color': COLORS['text_secondary'], 'padding': '20px', 'textAlign': 'center'}
        )
    
    top_posts = df.nlargest(10, 'score')[['platform', 'title', 'text', 'score', 'sentiment_label']].copy()
    
    # Safely truncate text
    top_posts['text'] = top_posts['text'].fillna('').astype(str).str[:100]
    top_posts['title'] = top_posts['title'].fillna('').astype(str).str[:50]
    
    # Sentiment color mapping
    sentiment_color = {
        'positive': COLORS['success'],
        'neutral': COLORS['primary'],
        'negative': COLORS['danger']
    }
    
    # Build table rows
    rows = []
    for idx, (_, row) in enumerate(top_posts.iterrows()):
        bg_color = COLORS['bg_dark'] if idx % 2 == 0 else COLORS['bg_light']
        color = sentiment_color.get(row['sentiment_label'], COLORS['text_primary'])
        
        rows.append(html.Tr([
            html.Td(
                row['platform'].upper(),
                style={
                    'color': COLORS['text_primary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {COLORS["border"]}',
                    'fontWeight': 'bold',
                    'width': '12%'
                }
            ),
            html.Td(
                row['title'] or row['text'],
                style={
                    'color': COLORS['text_secondary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {COLORS["border"]}',
                    'maxWidth': '400px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'whiteSpace': 'nowrap',
                    'width': '60%'
                }
            ),
            html.Td(
                str(row['score']),
                style={
                    'color': COLORS['text_primary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {COLORS["border"]}',
                    'textAlign': 'center',
                    'fontWeight': 'bold',
                    'width': '10%'
                }
            ),
            html.Td(
                row['sentiment_label'].upper(),
                style={
                    'color': color,
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {COLORS["border"]}',
                    'textAlign': 'center',
                    'fontWeight': 'bold',
                    'width': '18%'
                }
            )
        ]))
    
    return html.Table(
        [
            html.Thead(html.Tr([
                html.Th('Platform', style={
                    'color': COLORS['primary'],
                    'padding': '12px',
                    'backgroundColor': COLORS['bg_light'],
                    'textAlign': 'left',
                    'fontWeight': 'bold',
                    'borderBottom': f'2px solid {COLORS["primary"]}',
                    'width': '12%'
                }),
                html.Th('Content', style={
                    'color': COLORS['primary'],
                    'padding': '12px',
                    'backgroundColor': COLORS['bg_light'],
                    'textAlign': 'left',
                    'fontWeight': 'bold',
                    'borderBottom': f'2px solid {COLORS["primary"]}',
                    'width': '60%'
                }),
                html.Th('Score', style={
                    'color': COLORS['primary'],
                    'padding': '12px',
                    'backgroundColor': COLORS['bg_light'],
                    'textAlign': 'center',
                    'fontWeight': 'bold',
                    'borderBottom': f'2px solid {COLORS["primary"]}',
                    'width': '10%'
                }),
                html.Th('Sentiment', style={
                    'color': COLORS['primary'],
                    'padding': '12px',
                    'backgroundColor': COLORS['bg_light'],
                    'textAlign': 'center',
                    'fontWeight': 'bold',
                    'borderBottom': f'2px solid {COLORS["primary"]}',
                    'width': '18%'
                })
            ])),
            html.Tbody(rows)
        ],
        style={
            'width': '100%',
            'borderCollapse': 'collapse',
            'borderRadius': '8px',
            'overflow': 'hidden',
            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.3)'
        }
    )


# ============================================================================
# STAT CARD COMPONENT
# ============================================================================

def create_stat_card(label, value, color, icon=None):
    """Reusable statistic card component"""
    return html.Div([
        html.Div(icon, style={'fontSize': '24px', 'marginBottom': '10px'}) if icon else None,
        html.H3(label, style={
            'color': COLORS['text_secondary'],
            'fontSize': '14px',
            'fontWeight': 'normal',
            'margin': '0 0 10px 0',
            'textTransform': 'uppercase',
            'letterSpacing': '1px'
        }),
        html.H2(str(value), style={
            'color': color,
            'fontSize': '48px',
            'fontWeight': 'bold',
            'margin': '0',
            'lineHeight': '1'
        })
    ], style={
        'backgroundColor': COLORS['bg_light'],
        'borderLeft': f'4px solid {color}',
        'padding': '25px',
        'borderRadius': '8px',
        'flex': '1',
        'minWidth': '200px',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.2)'
    })


# ============================================================================
# LAYOUT & APP DEFINITION
# ============================================================================

# Calculate metrics
total_posts = len(df) if not df.empty else 0
positive_count = _safe_count(df, 'positive')
negative_count = _safe_count(df, 'negative')
neutral_count = _safe_count(df, 'neutral')

# Build the app layout
app.layout = html.Div(
    style={
        'backgroundColor': COLORS['bg_dark'],
        'color': COLORS['text_primary'],
        'fontFamily': 'Arial, sans-serif',
        'minHeight': '100vh',
        'padding': '20px'
    },
    children=[
        # HEADER
        html.Div([
            html.H1(
                '📊 Social Media Analytics Dashboard',
                style={
                    'margin': '0',
                    'fontSize': '32px',
                    'fontWeight': 'bold',
                    'background': f'linear-gradient(135deg, {COLORS["primary"]}, {COLORS["success"]})',
                    'WebkitBackgroundClip': 'text',
                    'WebkitTextFillColor': 'transparent'
                }
            ),
            html.P(
                f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | Database: {db_file or "New"}',
                style={
                    'color': COLORS['text_secondary'],
                    'margin': '10px 0 0 0',
                    'fontSize': '12px'
                }
            )
        ], style={
            'marginBottom': '40px',
            'paddingBottom': '20px',
            'borderBottom': f'2px solid {COLORS["border"]}'
        }),

        # STATISTICS CARDS
        html.Div([
            create_stat_card('Total Posts', total_posts, COLORS['primary'], '📝'),
            create_stat_card('Positive', positive_count, COLORS['success'], '😊'),
            create_stat_card('Negative', negative_count, COLORS['danger'], '😞'),
            create_stat_card('Neutral', neutral_count, COLORS['warning'], '😐')
        ], style={
            'display': 'flex',
            'gap': '20px',
            'marginBottom': '40px',
            'flexWrap': 'wrap'
        }),

        # CHARTS ROW 1
        html.Div([
            html.Div([
                dcc.Graph(
                    id='sentiment-by-platform',
                    figure=create_sentiment_by_platform(df),
                    style={'height': '400px'}
                )
            ], style={
                'flex': '1',
                'minWidth': '500px',
                'backgroundColor': COLORS['bg_light'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.2)'
            }),

            html.Div([
                dcc.Graph(
                    id='platform-distribution',
                    figure=create_platform_pie(df),
                    style={'height': '400px'}
                )
            ], style={
                'flex': '1',
                'minWidth': '400px',
                'backgroundColor': COLORS['bg_light'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.2)'
            })
        ], style={
            'display': 'flex',
            'gap': '20px',
            'marginBottom': '40px',
            'flexWrap': 'wrap'
        }),

        # CHARTS ROW 2
        html.Div([
            dcc.Graph(
                id='sentiment-over-time',
                figure=create_sentiment_timeline(df),
                style={'height': '400px'}
            )
        ], style={
            'backgroundColor': COLORS['bg_light'],
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.2)',
            'marginBottom': '40px'
        }),

        # TOP POSTS TABLE
        html.Div([
            html.H2(
                '🏆 Top Posts by Score',
                style={
                    'color': COLORS['text_primary'],
                    'marginTop': '0',
                    'marginBottom': '20px',
                    'fontSize': '20px'
                }
            ),
            create_top_posts_table(df)
        ], style={
            'backgroundColor': COLORS['bg_light'],
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.2)'
        })
    ]
)

# ============================================================================
# APP ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🚀  SOCIAL MEDIA ANALYTICS DASHBOARD")
    print("=" * 70)
    print(f"\n✅ Database: {db_file or 'New'}")
    print(f"📊 Total Posts: {total_posts}")
    print(f"😊 Positive Sentiments: {positive_count}")
    print(f"😞 Negative Sentiments: {negative_count}")
    print(f"😐 Neutral Sentiments: {neutral_count}")
    print(f"\n🌐 Open your browser at: http://127.0.0.1:8050")
    print(f"⏹️  Press Ctrl+C to stop the server")
    print("\n" + "=" * 70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=8050, use_reloader=False)