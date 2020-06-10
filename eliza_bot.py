import praw
import eliza
import config
import time
import string
import re
import random
import os


def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="eliza")
    return r


if not os.path.isfile("comment_replied_to.txt"):
    comment_replied_to = []
else:
    with open("comment_replied_to.txt", "r") as f:
        comment_replied_to = f.read()
        comment_replied_to = comment_replied_to.split("\n")
        comment_replied_to = list(filter(None, comment_replied_to))


therapist = eliza.Eliza()


def run_bot(r):
    for comment in r.subreddit('test').comments(limit=100):
        if re.search("talk to eliza", comment.body, re.IGNORECASE):
            if comment.id not in comment_replied_to:
                print("string found in" + comment.id)
                input = comment.body
                reply = therapist.respond(input)
                print(reply)
                # comment.reply(reply)
                comment_replied_to.append(comment.id)
                with open("comment_replied_to.txt", "w") as f:
                    for comment.id in comment_replied_to:
                        f.write(comment.id + "\n")
    time.sleep(10)


while True:
    r = bot_login()
    run_bot(r)
