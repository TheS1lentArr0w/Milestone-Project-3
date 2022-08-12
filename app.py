"""
Milestone Project 3
"""




### Imports
import requests

### Functions
def get_reddit(subreddit,listing,limit,timeframe,user_agent):
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
        request = requests.get(base_url, headers={"User-agent":user_agent})
    except:
        print("An error occurred.")

    return request.json()

def get_post_titles(r,title_condition):
    """
    ### Get a list of post titles
    post["data"]["permalink"] provides the 2nd half of link
    Add "https://www.reddit.com" to beginning of link to create whole link

    """
    posts = []
    links = []
    for post in r["data"]["children"]:
        post_title = post["data"]["title"]
        post_title_lower = post_title.lower()

        if title_condition in post_title_lower:
            posts.append(post_title)
            permalink = post["data"]["permalink"]
            link = "https://www.reddit.com" + permalink
            links.append(link)

    return posts,links

def send_email(posts,links):
    # outlook: smtp-mail.outlook.com
    pass

### Main
# Declaring variables
subreddit = "MechanicalKeyboards"
limit = 100
timeframe = "day"
listing = "new"
user_agent = "Giveaway Hunter v1.0 by /u/thes1lentarr0w : https://github.com/TheS1lentArr0w/Milestone-Project-3"
title_condition = "custom"

# Post acquisition
r = get_reddit(subreddit, listing, limit, timeframe, user_agent)
posts,links = get_post_titles(r,title_condition)
print(posts)
print(links)

# Send email if relevant posts discovered


"""
Reference links
https://github.com/reddit-archive/reddit/wiki/API
"""
