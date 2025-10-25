from commit import Commit
import datetime

import math


def calculate_KPI(diff: dict[Commit, str], people: list[str], commit_by_name: dict[str, list[Commit]]) -> dict[str, float]:
    sum_metric = dict()

    for author_name in people:
        people_commits = commit_by_name[author_name]
        metric = 0
        last_date = None
        for people_commit in people_commits:
            str_diff = diff[people_commit]
            cnt_add, cnt_del = 0, 0


            last_dura = datetime.timedelta(seconds=0)

            if last_date:
                last_dura = last_date - people_commit.commit_date
            else:
                last_dura = datetime.timedelta(seconds=60*60*24)
                last_date = people_commit.commit_date

            for changes_str in str_diff.split('\n'):
                if changes_str and changes_str[0] == "+" and changes_str[:3] != "+++":
                    cnt_add += 1
                elif changes_str and changes_str[0] == '-' and changes_str[:3] != "---":
                    cnt_del += 1

            metric =  10 * (math.log(abs(cnt_add - cnt_del * 0.5) * len(people_commits) + 1) / math.log10(last_dura.total_seconds() / 60 + 1)) ** 0.5

            sum_metric[author_name] = metric
            last_date = people_commit.commit_date


    return sum_metric