import parse_commits
import parse_diff
import parser
import dashboard

commits, commits_by_author, people = parse_commits.parse()

difference = parse_diff.parse(commits)

kpi_by_name = parser.calculate_KPI(difference, people, commits_by_author)

dashboard.build_interactive_dashboard(kpi_by_name)