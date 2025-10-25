import plotly.express as px

def build_interactive_dashboard(kpi_by_name: dict[str, float]):
    for contributor, value in kpi_by_name.items():
        print(contributor, value)

    fig = px.bar(x=list(kpi_by_name.values()), 
                 y=list(kpi_by_name.keys()),
                 orientation='h',
                 title='KPI по сотрудникам')
    fig.show()