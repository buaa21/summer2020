import json
import sqlite3
import datetime

# read username reference
username_ref = dict()
with open("username-reference.txt", 'r', encoding='utf8') as f:
    for line in f.readlines():
        [name, username] = line.split()
        username_ref[username] = name
username_list = list(username_ref.keys())

print(username_list)

# read json
with open('data_comments.json', 'r', encoding='utf8') as f:
    comments = json.load(f)

print("Read comments from data_comments.json: "+str(len(comments)))

# load into sqlite


conn = sqlite3.connect(":memory:")

# create table
conn.executescript(
    '''
    CREATE TABLE comments (
        id INTEGER NOT NULL PRIMARY KEY,
        url TEXT,
        html_url TEXT,
        issue_url TEXT,
        body TEXT,
        username TEXT,
        avatar_url TEXT,
        created_at DATETIME,
        updated_at DATETIME
    )
    '''
)

# save into sqlite
for c in comments:
    conn.execute('''INSERT INTO comments(id, url, html_url, issue_url, body, username, avatar_url, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (c['id'], c['url'], c['html_url'], c['issue_url'], c['body'], c['username'], c['avatar_url'], c['created_at'], c['updated_at']))

comment_cnt = conn.execute("SELECT count(*) from comments").fetchone()[0]
print(f"Saved to sqlite: {comment_cnt}")

# 2020.8.27
t_start = datetime.date(2020, 8, 27) - \
    datetime.timedelta(hours=8)  # beijing to utc
t_end = t_start + datetime.timedelta(days=1)

cnt2 = conn.execute(
    "select count(*) from comments where created_at > ? and created_at < ?", (t_start, t_end)).fetchone()[0]
print(cnt2)

r = conn.execute('''
    select A.username, count(*) as cnt from (select username, issue_url from comments group by username, issue_url) A
    group by A.username order by cnt desc ''').fetchall()

r = [x for x in r if x[0] in username_ref]

for [username, cnt] in r:
    name = username_ref[username]
    print(f"{username} {name} {cnt}")