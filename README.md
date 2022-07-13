# calendar_project
Create Events on Google Calendar with Git Commit

# requirements and setup

pip install google-api-python-client oauth2 rfc3339

curl -L http://s.liap.us/gcal-post-commit.py > .git/hooks/post-commit

chmod +x .git/hooks/post-commit

nano .git/hooks/post-commit

# after that steps for oauth with google calendar api

step 1 - Go to https://console.cloud.google.com/apis/dashboard

step 2 - select  New project from drop down menu

step 3 - Add project name, organization,location.

step 4 - search Google calendar api and press enable

step 5 - go-to Oauth consent screen and fill the details which are necessary (usertype - internal)

step 6 - here we were writing scopes manually in python file so no need to select scopes.

step 7 - Go to credentials and click create credentials and select oauth , select application type as "DESKTOP"

step 8 - client id and secret are created , save them.

step 9 - for developer key - again go to create credentials and select api key and api key is created.

# for calendar id
go to you calendar select any calendar from my calendars , scroll and click to : and go to settings and there you find you calendar id .

after that run project, for the first time it will asks permissions to authenticate and event is created .
