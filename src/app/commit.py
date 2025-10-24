from datetime import datetime


class Commit:
  commit_hash: str
  commit_date: datetime
  commit_author_name: str
  commit_author_email: str
  commit_mesage: str
  commit_Tags: list[str]
  commit_tag_names: list[str]

  def __init__(self, c: dict) -> None:
    self.commit_hash = c['hash']
    self.commit_mesage = c['message']
    self.commit_author_name = c['author']['name']
    self.commit_author_email = c['author']['email']
    self.commit_date = datetime.strptime(c['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    self.commit_tag_names = c['tag_names']
    self.commit_Tags = c['Tags']

  def __str__(self) -> str:
    return f"hash: {self.commit_hash}\n" + f"date: {self.commit_date}\n" + f"author: {self.commit_author_name}"