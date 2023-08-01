import requests
# 批量下载项目
SERVER_URL = ""
git_repo_urls = []

for repo_url in git_repo_urls:
    res = requests.post(SERVER_URL, json={"url": repo_url}, auth=())
    print(res.status_code, repo_url)
    if res.status_code != 200:
        print('Failed to create job for', repo_url, res.text)
# https_proxy= http_proxy= python batch_download_git_repos_demo.py
# 不需要使用代理
