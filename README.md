# calendar_project
Create Events on Google Calendar with Git Commit

# requirements and setup

pip install google-api-python-client oauth2 rfc3339

curl -L http://s.liap.us/gcal-post-commit.py > .git/hooks/post-commit
chmod +x .git/hooks/post-commit

nano .git/hooks/post-commit
