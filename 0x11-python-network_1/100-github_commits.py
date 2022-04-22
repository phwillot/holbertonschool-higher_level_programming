#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve
this challenge.
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from sys import argv
import requests

if __name__ == "__main__":
    repoName = argv[1]
    ownerName = argv[2]

    r = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(
            ownerName, repoName))
    dict = r.json()
    for i in range(10):
        print("{}: {}".format(dict[i].get('sha'),
              dict[i].get('commit').get("author").get('name')))
