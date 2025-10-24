import datetime

import parse_commits
import parse_diff
import math

commits, commit_by_name, people = parse_commits.parse()

#diff = parse_diff.parse(commits)

sum_metric = dict()

for author_name in people:
    people_commits = commit_by_name[author_name]
    diff = parse_diff.parse(people_commits)

    metric = 0
    for people_commit in people_commits:

        str_diff = diff[people_commit]

        cnt_add, cnt_del = 0, 0

        last_dura = datetime.timedelta(seconds=0)
        for changes_str in str_diff.split('\n'):
            if last_dura.total_seconds() != 0:
                last_dura = last_date - people_commit.commit_date

            if changes_str[:3] == "+++":
                cnt_add += 1
            else:
                cnt_del += 1

            metric = ((cnt_add + cnt_del * 0.25) * 10 / (math.log(last_dura.total_seconds() + 1, 2.71) + 1)) / 12

            if author_name not in sum_metric.keys():
                sum_metric[author_name] = 0
            sum_metric[author_name] += metric

            last_date = people_commit.commit_date

for author_name in people:
    print(author_name, len(commit_by_name[author_name]), sum_metric[author_name])
# sum_metric[people] -> metric