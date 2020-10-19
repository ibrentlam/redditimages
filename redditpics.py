
# this is the one you'll need to "pip install praw"
import praw

# these should be standard
import re
import urllib.request
import os
from pathlib import Path

# account setup
reddit = praw.Reddit(
     client_id="client_id_here",
     client_secret="client_secret_here",
     user_agent="Mozilla",
)

# subreddit parameters
# these give about 150 images when I tried it

whichSubreddit = 'ImaginaryLandscapes'
articleCount = 1000
minScore = 300

# whichSubreddit = 'mostbeautiful'
# articleCount = 1000
# minScore = 100

# whichSubreddit = 'earthporn'
# articleCount = 1000
# minScore = 200

subreddit = reddit.subreddit(whichSubreddit)

# make the corresponding subdirectory
if not os.path.exists(whichSubreddit):
    os.makedirs(whichSubreddit)

# loop through the hot submissions
for submission in subreddit.hot(limit=articleCount):
    sub_id = submission.id     # Output: the submission's ID
    # check for image and score
    if('preview' in vars(submission) and submission.score > minScore):
        url = vars(submission)['preview']['images'][0]['source']['url']
        # I've only seen .jpg files, but just to make sure
        baseUrl = url.split('?')[0]
        suffix = Path(baseUrl).suffix
        # munge title into filename
        localFileName = "_".join( submission.title.split() ) 
        localFileName = re.sub(r'\W+', '', localFileName.title()) + suffix
        print(localFileName)
        localFilePath = whichSubreddit + '/' + localFileName
        # download and store if we don't have it already
        if(not os.path.isfile(localFilePath)):
            urllib.request.urlretrieve(url, localFilePath)

