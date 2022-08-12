import requests



def get_reddit(subreddit,listing,limit,timeframe,user_agent):
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
        request = requests.get(base_url,headers={"User-agent":user_agent})
    except:
        print("An error occurred.")

    return request.json()

def get_post_titles(r):
    """
    Get a list of post titles
    """
    posts = []
    for post in r["data"]["children"]:
        posts.append(post["data"]["title"])
    
    return posts

subreddit = "MechanicalKeyboards"
limit = 10
timeframe = "day"
listing = "top"
user_agent = "Giveaway Hunter v1.0 by /u/thes1lentarr0w : https://github.com/TheS1lentArr0w/Milestone-Project-3"
r = get_reddit(subreddit,listing,limit,timeframe,user_agent)
posts = get_post_titles(r)
print(posts)