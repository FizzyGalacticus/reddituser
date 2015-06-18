#!/usr/bin/env python
#Author: Dustin Dodson
#Date modified: June 17, 2015

class RedditUser:
    """This class is for retrieving Reddit users and their information"""

    def __init__(self, username):
        self.r = praw.Reddit(user_agent='FizzyGalacticus - Reddit User Getter')
        self.username = username
        self.user = r.get_redditor(self.username)

    def getSubmissions(limit=None):
        return self.user.get_submitted(limit)

    def getComments(limit=None):
        return self.user.get_comments(limit)