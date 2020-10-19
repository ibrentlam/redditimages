
This program downloads images from a subreddit into a subdirectory, to be used on screensavers, backgrounds, etc.

You'll need the PRAW python library:
install PRAW:
https://praw.readthedocs.io/en/latest/getting_started/installation.html

tl;dr
pip install praw


and reddit developer credentials 
https://www.reddit.com/wiki/api#wiki_reddit_api_access


you'll enter these at the top as client_id, client_secret and user_agent

then select the subreddit, how many top posts to look back through, and the minimum score for each, some examples are provided. 

the images that match will be downloaded into a folder of the same name as the subreddit and the filenames will be sanitized versions of the post title. 

