import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from database import SocialMediaDB
import glob
from datetime import datetime

# ============================================================================
# PROFESSIONAL COLOR PALETTE & CONFIGURATION
# ============================================================================

THEME = {
    'primary': '#1E88E5',      # Professional Blue
    'secondary': '#43A047',    # Success Green
    'accent': '#FB8C00',       # Accent Orange
    'danger': '#E53935',       # Danger Red
    'warning': '#FDD835',      # Warning Yellow
    
    'bg_primary': '#FFFFFF',   # White
    'bg_secondary': '#F5F5F5', # Light Gray
    'bg_tertiary': '#EEEEEE',  # Medium Gray
    
    'text_primary': '#212121',    # Dark Text
    'text_secondary': '#616161',  # Gray Text
    'text_light': '#FFFFFF',      # White Text
    
    'border': '#BDBDBD',       # Border Color
    'shadow': 'rgba(0, 0, 0, 0.1)'
}

# Initialize Dash app
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
    print(f"[DATABASE] Database loaded: {db_file}")
else:
    db = SocialMediaDB()
    print("[DATABASE] New database created")

df = db.get_all_posts()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _safe_count(df, label_value):
    """Safely count sentiments without KeyError"""
    if df.empty or 'sentiment_label' not in df.columns:
        return 0
    return int(df['sentiment_label'].eq(label_value).sum())

def create_stat_card(label, value, color, icon_char=""):
    """Reusable professional statistic card component"""
    return html.Div([
        html.Div([
            html.Span(label, style={
                'color': THEME['text_secondary'],
                'fontSize': '12px',
                'fontWeight': '600',
                'textTransform': 'uppercase',
                'letterSpacing': '1px',
                'display': 'block',
                'marginBottom': '8px'
            }),
            html.H2(str(value), style={
                'color': color,
                'fontSize': '36px',
                'fontWeight': '700',
                'margin': '0',
                'lineHeight': '1'
            })
        ], style={
            'padding': '20px',
        })
    ], style={
        'backgroundColor': THEME['bg_primary'],
        'border': f'2px solid {color}',
        'borderRadius': '8px',
        'boxShadow': THEME['shadow'],
        'flex': '1',
        'minWidth': '150px',
        'transition': 'transform 0.2s, box-shadow 0.2s',
    })

def create_sentiment_by_platform(df):
    """Stacked bar chart of sentiment distribution by platform"""
    if df.empty:
        return go.Figure().add_annotation(text="No data available")
    
    sentiment_counts = df.groupby(['platform', 'sentiment_label']).size().reset_index(name='count')
    
    color_map = {
        'positive': THEME['secondary'],
        'neutral': THEME['primary'],
        'negative': THEME['danger']
    }
    
    fig = px.bar(
        sentiment_counts,
        x='platform',
        y='count',
        color='sentiment_label',
        title='Sentiment Distribution by Platform',
        color_discrete_map=color_map,
        barmode='group',
        labels={'count': 'Posts', 'platform': 'Platform', 'sentiment_label': 'Sentiment'}
    )
    
    fig.update_layout(
        plot_bgcolor=THEME['bg_secondary'],
        paper_bgcolor=THEME['bg_primary'],
        font=dict(color=THEME['text_primary'], family='Segoe UI, Arial, sans-serif', size=11),
        title=dict(font=dict(size=16, color=THEME['text_primary']), x=0.5),
        hovermode='x',
        margin=dict(l=50, r=50, t=80, b=50),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor=THEME['bg_tertiary']),
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor=THEME['border'],
            borderwidth=1,
            orientation='v',
            yanchor='top',
            y=0.99,
            xanchor='left',
            x=0.01
        ),
        height=400
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
        'positive': THEME['secondary'],
        'neutral': THEME['primary'],
        'negative': THEME['danger']
    }
    
    fig = px.area(
        timeline_data,
        x='date',
        y='count',
        color='sentiment_label',
        title='Sentiment Trends Over Time',
        color_discrete_map=color_map,
        labels={'count': 'Posts', 'date': 'Date'}
    )
    
    fig.update_layout(
        plot_bgcolor=THEME['bg_secondary'],
        paper_bgcolor=THEME['bg_primary'],
        font=dict(color=THEME['text_primary'], family='Segoe UI, Arial, sans-serif', size=11),
        title=dict(font=dict(size=16, color=THEME['text_primary']), x=0.5),
        hovermode='x',
        margin=dict(l=50, r=50, t=80, b=50),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor=THEME['bg_tertiary']),
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor=THEME['border'],
            borderwidth=1,
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        height=350
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
        title='Distribution by Platform',
        color_discrete_sequence=[THEME['primary'], THEME['secondary'], THEME['accent']]
    )
    
    fig.update_layout(
        plot_bgcolor=THEME['bg_primary'],
        paper_bgcolor=THEME['bg_primary'],
        font=dict(color=THEME['text_primary'], family='Segoe UI, Arial, sans-serif', size=11),
        title=dict(font=dict(size=16, color=THEME['text_primary']), x=0.5),
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor=THEME['border'],
            borderwidth=1
        ),
        height=350
    )
    
    return fig

def create_sentiment_gauge(df, platform_filter=None):
    """Create gauge chart showing overall sentiment"""
    if df.empty:
        avg_sentiment = 0
    else:
        if platform_filter and platform_filter != 'all':
            df_filtered = df[df['platform'] == platform_filter]
        else:
            df_filtered = df
        
        if df_filtered.empty:
            avg_sentiment = 0
        else:
            avg_sentiment = df_filtered['sentiment_score'].mean()
    
    # Convert -1 to 1 range to 0 to 100 range
    gauge_value = (avg_sentiment + 1) * 50
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = gauge_value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': 'Overall Sentiment'},
        delta = {'reference': 50},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': THEME['primary']},
            'steps': [
                {'range': [0, 33], 'color': THEME['danger']},
                {'range': [33, 67], 'color': THEME['warning']},
                {'range': [67, 100], 'color': THEME['secondary']}
            ],
            'threshold': {
                'line': {'color': THEME['text_primary'], 'width': 2},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        plot_bgcolor=THEME['bg_primary'],
        paper_bgcolor=THEME['bg_primary'],
        font=dict(color=THEME['text_primary'], family='Segoe UI, Arial, sans-serif'),
        height=300,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig

def create_top_posts_table(df):
    """HTML table showing top 10 posts by score"""
    if df.empty or 'score' not in df.columns:
        return html.Div(
            "No data available",
            style={'color': THEME['text_secondary'], 'padding': '20px', 'textAlign': 'center'}
        )
    
    top_posts = df.nlargest(10, 'score')[['platform', 'title', 'text', 'score', 'sentiment_label']].copy()
    
    top_posts['text'] = top_posts['text'].fillna('').astype(str).str[:100]
    top_posts['title'] = top_posts['title'].fillna('').astype(str).str[:50]
    
    sentiment_color = {
        'positive': THEME['secondary'],
        'neutral': THEME['primary'],
        'negative': THEME['danger']
    }
    
    rows = []
    for idx, (_, row) in enumerate(top_posts.iterrows()):
        bg_color = THEME['bg_secondary'] if idx % 2 == 0 else THEME['bg_primary']
        color = sentiment_color.get(row['sentiment_label'], THEME['text_primary'])
        
        rows.append(html.Tr([
            html.Td(
                row['platform'].upper(),
                style={
                    'color': THEME['text_primary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {THEME["border"]}',
                    'fontWeight': '600',
                    'fontSize': '12px',
                    'width': '80px'
                }
            ),
            html.Td(
                row['title'] or row['text'],
                style={
                    'color': THEME['text_secondary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {THEME["border"]}',
                    'maxWidth': '400px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'whiteSpace': 'nowrap',
                    'fontSize': '12px'
                }
            ),
            html.Td(
                str(int(row['score'])),
                style={
                    'color': THEME['text_primary'],
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {THEME["border"]}',
                    'textAlign': 'center',
                    'fontWeight': '600',
                    'fontSize': '12px',
                    'width': '70px'
                }
            ),
            html.Td(
                row['sentiment_label'].upper(),
                style={
                    'color': color,
                    'padding': '12px',
                    'backgroundColor': bg_color,
                    'borderBottom': f'1px solid {THEME["border"]}',
                    'textAlign': 'center',
                    'fontWeight': '600',
                    'fontSize': '11px',
                    'width': '100px'
                }
            )
        ]))
    
    return html.Table(
        [
            html.Thead(html.Tr([
                html.Th('Platform', style={
                    'color': THEME['text_light'],
                    'padding': '12px',
                    'backgroundColor': THEME['primary'],
                    'textAlign': 'left',
                    'fontWeight': '600',
                    'fontSize': '12px',
                    'width': '80px'
                }),
                html.Th('Content', style={
                    'color': THEME['text_light'],
                    'padding': '12px',
                    'backgroundColor': THEME['primary'],
                    'textAlign': 'left',
                    'fontWeight': '600',
                    'fontSize': '12px'
                }),
                html.Th('Score', style={
                    'color': THEME['text_light'],
                    'padding': '12px',
                    'backgroundColor': THEME['primary'],
                    'textAlign': 'center',
                    'fontWeight': '600',
                    'fontSize': '12px',
                    'width': '70px'
                }),
                html.Th('Sentiment', style={
                    'color': THEME['text_light'],
                    'padding': '12px',
                    'backgroundColor': THEME['primary'],
                    'textAlign': 'center',
                    'fontWeight': '600',
                    'fontSize': '12px',
                    'width': '100px'
                })
            ])),
            html.Tbody(rows)
        ],
        style={
            'width': '100%',
            'borderCollapse': 'collapse',
            'borderRadius': '4px',
            'overflow': 'hidden',
            'boxShadow': THEME['shadow'],
            'fontSize': '12px'
        }
    )

# ============================================================================
# LAYOUT & APP DEFINITION
# ============================================================================

# Calculate metrics
total_posts = len(df) if not df.empty else 0
positive_count = _safe_count(df, 'positive')
negative_count = _safe_count(df, 'negative')
neutral_count = _safe_count(df, 'neutral')

app.layout = html.Div(
    style={
        'backgroundColor': THEME['bg_secondary'],
        'color': THEME['text_primary'],
        'fontFamily': 'Segoe UI, Arial, sans-serif',
        'minHeight': '100vh',
        'padding': '0'
    },
    children=[
        # HEADER
        html.Div([
            html.Div([
                html.H1(
                    'Social Media Analytics Dashboard',
                    style={
                        'margin': '0',
                        'fontSize': '28px',
                        'fontWeight': '700',
                        'color': THEME['primary']
                    }
                ),
                html.P(
                    f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | Database: {db_file or "New"}',
                    style={
                        'color': THEME['text_secondary'],
                        'margin': '8px 0 0 0',
                        'fontSize': '12px'
                    }
                )
            ])
        ], style={
            'backgroundColor': THEME['bg_primary'],
            'padding': '24px 40px',
            'borderBottom': f'1px solid {THEME["border"]}',
            'boxShadow': THEME['shadow']
        }),

        # MAIN CONTENT
        html.Div([
            # STATISTICS CARDS
            html.Div([
                create_stat_card('Total Posts', total_posts, THEME['primary']),
                create_stat_card('Positive', positive_count, THEME['secondary']),
                create_stat_card('Neutral', neutral_count, THEME['primary']),
                create_stat_card('Negative', negative_count, THEME['danger'])
            ], style={
                'display': 'flex',
                'gap': '16px',
                'marginBottom': '24px',
                'flexWrap': 'wrap'
            }),

            # CHARTS ROW 1
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='sentiment-by-platform',
                        figure=create_sentiment_by_platform(df),
                        config={'displayModeBar': False}
                    )
                ], style={
                    'flex': '2',
                    'minWidth': '400px',
                    'backgroundColor': THEME['bg_primary'],
                    'padding': '20px',
                    'borderRadius': '8px',
                    'boxShadow': THEME['shadow']
                }),

                html.Div([
                    dcc.Graph(
                        id='overall-sentiment-gauge',
                        figure=create_sentiment_gauge(df),
                        config={'displayModeBar': False}
                    )
                ], style={
                    'flex': '1',
                    'minWidth': '300px',
                    'backgroundColor': THEME['bg_primary'],
                    'padding': '20px',
                    'borderRadius': '8px',
                    'boxShadow': THEME['shadow']
                })
            ], style={
                'display': 'flex',
                'gap': '16px',
                'marginBottom': '24px',
                'flexWrap': 'wrap'
            }),

            # CHARTS ROW 2
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='sentiment-over-time',
                        figure=create_sentiment_timeline(df),
                        config={'displayModeBar': False}
                    )
                ], style={
                    'backgroundColor': THEME['bg_primary'],
                    'padding': '20px',
                    'borderRadius': '8px',
                    'boxShadow': THEME['shadow']
                })
            ], style={
                'marginBottom': '24px'
            }),

            # CHARTS ROW 3
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='platform-distribution',
                        figure=create_platform_pie(df),
                        config={'displayModeBar': False}
                    )
                ], style={
                    'flex': '1',
                    'minWidth': '300px',
                    'backgroundColor': THEME['bg_primary'],
                    'padding': '20px',
                    'borderRadius': '8px',
                    'boxShadow': THEME['shadow']
                })
            ], style={
                'display': 'flex',
                'gap': '16px',
                'marginBottom': '24px'
            }),

            # TOP POSTS TABLE
            html.Div([
                html.H2(
                    'Top Posts by Engagement',
                    style={
                        'color': THEME['text_primary'],
                        'marginTop': '0',
                        'marginBottom': '16px',
                        'fontSize': '18px',
                        'fontWeight': '600'
                    }
                ),
                create_top_posts_table(df)
            ], style={
                'backgroundColor': THEME['bg_primary'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': THEME['shadow']
            })

        ], style={
            'padding': '24px 40px',
            'maxWidth': '1400px',
            'margin': '0 auto'
        })
    ]
)

# ============================================================================
# APP ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("SOCIAL MEDIA ANALYTICS DASHBOARD")
    print("=" * 70)
    print(f"\n[DATABASE] {db_file or 'New'}")
    print(f"[POSTS] Total Posts: {total_posts}")
    print(f"[SENTIMENT] Positive: {positive_count}, Neutral: {neutral_count}, Negative: {negative_count}")
    print(f"\n[SERVER] Open your browser at: http://127.0.0.1:8050")
    print(f"[SERVER] Press Ctrl+C to stop")
    print("\n" + "=" * 70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=8050, use_reloader=False)