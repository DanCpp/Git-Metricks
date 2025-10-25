import parse_commits
import parse_diff
import parser
import dashboard
import dash
from dash import dcc, html

app = dash.Dash(__name__)

commits, commits_by_author, people = parse_commits.parse()

difference = parse_diff.parse(commits)

kpi_by_name = parser.calculate_KPI(difference, people, commits_by_author)

fig = dashboard.build_interactive_dashboard(kpi_by_name)


timeline_fig = dashboard.create_commits_timeline(commits_by_author)
weekday_fig = dashboard.create_weekday_chart(commits_by_author)


app.layout = html.Div([
    html.H1("Дашборд KPI и коммитов сотрудников", style={'textAlign': 'center'}),
    
    dcc.Graph(figure=fig),
    
    html.Hr(),
    
    html.H2("Аналитика коммитов", style={'textAlign': 'center'}),
    
    dcc.Graph(figure=timeline_fig),
    dcc.Graph(figure=weekday_fig),
    
    html.Div([
        html.H3("Детальная информация по коммитам"),
        html.Div(id='commit-details')
    ])
])

app.run(host='0.0.0.0', port=8050, debug=True)