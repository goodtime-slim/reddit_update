import praw

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     # password=PASSWORD,
                     user_agent=USER_AGENT,
                     # username=USERNAME
                     )

def get_comment_ids(thread_id):
    submission = reddit.submission(id=thread_id)
    submission.comments.replace_more(limit=None)
    comment_list = submission.comments.list()
    ids = [(x.id,) for x in comment_list]
    return ids
