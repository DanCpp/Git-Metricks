import json
import subprocess
import base64

from commit import Commit

def place_diff_commit(c: Commit):
  result = subprocess.run(["bash", "./src/init_diff_data.sh", c.commit_hash])

  if result.returncode != 0:
    print("Poshlo vse nahuy")
    raise KeyError
  
def get_diff(c: Commit) -> (str, list[str], list[str]):
  with open(f"./test-data/data_{c.commit_hash}.json", 'r') as file:
    data = json.load(file)['data']

  return data['content'], data['large_files'], data['excluded_files']
  
def delete_diff_commit(c: Commit):
  result = subprocess.run(["rm", "-f", f"./test-data/data_{c.commit_hash}.json"])

  if result.returncode != 0:
    print("Poshlo vse nahuy blyat")
    raise KeyError

def parse(commits: list[Commit]) -> dict[Commit, str]:
  result: dict[Commit, str] = dict()
  for c in commits:
    place_diff_commit(c)
    # large_files and excluded_files are now discarded, maybe in future...?
    content, _, _ = get_diff(c)
    result[c] = base64.b64decode(content)
    delete_diff_commit(c)

  return result
