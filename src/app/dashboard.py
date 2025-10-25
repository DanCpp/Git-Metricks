from commit import Commit
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

def build_interactive_dashboard(kpi_by_name: dict[str, float]) -> go.Figure:
    fig = px.bar(x=list(kpi_by_name.values()), 
                 y=list(kpi_by_name.keys()),
                 orientation='h',
                 title='KPI по сотрудникам')
    return fig


def build_time_commits(people: list[str], commit_by_author: dict[str, list[Commit]]) -> list:
    result: list = []
    for author in people:
        commits_dates = sorted([str(commit.commit_date.date()) for commit in commit_by_author[author]])
        unique_dates = sorted(list(set(commits_dates)))

        scores = [commits_dates.count(date) for date in unique_dates]

        result.append(px.bar(
            x=unique_dates,
            y=scores,
            orientation='h',
            title=f'{author}',
        ))

    return result
        

def create_commits_timeline(commit_by_author: dict[str, list[Commit]]) -> go.Figure:
    all_dates = []
    for commits in commit_by_author.values():
        for commit in commits:
            all_dates.append(str(commit.commit_date.date()))
    
    if not all_dates:
        return px.line(title='Нет данных о коммитах')
    
    all_dates.sort()
    
    fig = go.Figure()
    
    for author, commits in commit_by_author.items():
        if commits:
            date_counts = defaultdict(int)
            for commit in commits:
                date = str(commit.commit_date.date())
                date_counts[date] += 1
            
            dates = sorted(date_counts.keys())
            counts = [date_counts[date] for date in dates]
            
            fig.add_trace(go.Scatter(
                x=dates,
                y=counts,
                mode='lines+markers',
                name=author,
                hovertemplate=f'<b>{author}</b><br>Дата: %{{x}}<br>Коммитов: %{{y}}<extra></extra>'
            ))
    
    fig.update_layout(
        title='Коммиты по сотрудникам (временная шкала)',
        xaxis_title='Дата',
        yaxis_title='Количество коммитов',
        hovermode='closest'
    )
    
    return fig


def create_weekday_chart(commit_by_author: dict[str, list[Commit]]) -> go.Figure:
    weekday_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    weekday_data = []
    
    for author, commits in commit_by_author.items():
        author_weekdays = [0] * 7
        for commit in commits:
            try:
                date_obj = commit.commit_date.date()
                
                weekday = date_obj.weekday() 
                author_weekdays[weekday] += 1
            except:
                continue
        
        for i, count in enumerate(author_weekdays):
            if count > 0:
                weekday_data.append({
                    'author': author,
                    'weekday': weekday_names[i],
                    'commits': count
                })
    
    if not weekday_data:
        return px.bar(title='Нет данных для графика дней недели')
    
    fig = px.bar(
        weekday_data,
        x='weekday',
        y='commits',
        color='author',
        title='Распределение коммитов по дням недели',
        category_orders={'weekday': weekday_names}
    )
    
    return fig
