import json
import datetime

from commit import Commit


commits: list[Commit] = []

commit_by_name: dict[str, list[Commit]] = dict()

people: set = set()

with open('./test-data/data.json', 'r') as file:
  data = json.load(file)['data']

for c in data:
  new_commit: Commit = Commit(c)
  commits.append(new_commit)
  if new_commit.commit_author_name in commit_by_name:
    commit_by_name[new_commit.commit_author_name].append(new_commit)
  else:
    commit_by_name[new_commit.commit_author_name] = [new_commit]
  people.add(new_commit.commit_author_name)