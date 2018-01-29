import praw

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT,
                     username=USERNAME)

submission = reddit.submission(id='7tnnv9')
comments = submission.

submission.comments()

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri='https://www.google.com',
                     user_agent='updates by /u/goodtime_slim')
x = reddit.auth.url(['identity'], '...', 'permanent')

