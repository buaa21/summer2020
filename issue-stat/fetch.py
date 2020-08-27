import os
import json
from github import Github

# read access data
access_file = "access.json"
access_info = {"username": "", "password": ""}

# 首次运行，创建access.json
if not os.path.exists(access_file):
    with open(access_file, "w", encoding='utf8') as f:
        json.dump(access_info, f, ensure_ascii=False)
    print("access.json已生成，请填写access.json")
    exit(2)

# load access.json tp access_info
with open(access_file, "r", encoding='utf8') as f:
    access_info = json.load(f)

# access info should be modified by user
if access_info['username'] == '' or access_info['password'] == '':
    print("请填写access.json")
    exit(2)

g = Github(access_info['username'], access_info['password'])

summer_repo = g.get_repo('buaa21/summer2020')

comments = list(summer_repo.get_issues_comments())

print(f"获取的评论数量： {len(comments)}")

# convert comments to plain comments
plain_comments = []
for comment in comments:
    pc = {
        'id': comment.id,
        'url': comment.issue_url,
        'html_url': comment.html_url,
        'issue_url': comment.issue_url,
        'body': comment.body,
        'username': comment.user.login,
        'avatar_url': comment.user.avatar_url,
        'created_at': str(comment.created_at),
        'updated_at': str(comment.updated_at),
    }
    plain_comments.append(pc)

with open("data_comments.json", "w", encoding='utf8') as f:
    json.dump(plain_comments, f, ensure_ascii=False)

print("数据已保存到 data_comments.json")

limit = g.get_rate_limit()
print("api剩余: "+str(limit))
