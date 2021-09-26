# GItAPI
proxy REST API for obtaining information about a certain GitHub repo.


# Instructions for use

**1. Get repo details**

request | response
--------|---------
/api/repo_details/{github:account}/{github:repo} | Gives full information about the repository, its owner, views, pulls and forks, etc.

**response example**  

> /api/repo_details/octocat/hello-world
```
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "private": false,
    "owner": {
        "login": "octocat",
        "id": 583231,
        "node_id": "MDQ6VXNlcjU4MzIzMQ==",
        "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false
    },
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "My first repository on GitHub!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2021-09-26T15:56:32Z",
    "pushed_at": "2021-09-17T12:36:46Z",
    "git_url": "git://github.com/octocat/Hello-World.git",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "svn_url": "https://github.com/octocat/Hello-World",
    "homepage": "",
    "size": 1,
    "stargazers_count": 1693,
    "watchers_count": 1693,
    "language": null,
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 1615,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 574,
    "license": null,
    "allow_forking": true,
    "forks": 1615,
    "open_issues": 574,
    "watchers": 1693,
    "default_branch": "master",
    "temp_clone_token": null,
    "network_count": 1615,
    "subscribers_count": 1788
})
```

**2. Get sample data from repository**
request | response
--------|---------
/api/repo_details/{github:account}/{github:repo}/pulls | Gives all the pool requests of the selected repository
/api/repo_details/{github:account}/{github:repo}/unmerged_pulls | Returns a list of all pull requests that have not been merged for 2 weeks or more
/api/repo_details/{github:account}/{github:repo}/forks | Gives all the forks of the selected repository
/api/repo_details/{github:account}/{github:repo}/issues | Gives all the issues of the selected repository

# Exceptions

In case of incorrect formation of a link by the user or an attempt to go to a non-existent page, the api gives the answer:

```{"message": "Not Found"}```

