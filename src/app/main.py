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


app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

app.run(host='0.0.0.0', port=8050, debug=True)