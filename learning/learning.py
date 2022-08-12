# HTTP GET
# Acquires JSON file
import urllib.request
# contents = urllib.request.urlopen("https://www.reddit.com/r/python/top.json?limit=100&t=year").read()

#######
## More info on Reddit API request
# https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}
# {subreddit} - subreddit
# {listing} - controversial, best, hot, new, etc
# {count} - number of posts retrieved
# {timeframe} - hour, day, week, month, year, all
#######

# HTTP GET request from a more basic package
import requests
import pandas as pd

subreddit = "python"
limit = 100
timeframe = "month"
listing = "top"


def get_reddit(subreddit, listing, limit, timeframe):
    try:
        base_url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}"
        request = requests.get(base_url, headers={"User-agent": "yourbot"})
    except:
        print("An Error Occurred")

    return request.json()


r = get_reddit(subreddit, listing, limit, timeframe)
# r = urllib.request.urlopen("https://www.reddit.com/r/python/top.json?limit=100&t=year").read()


# r is JSON file
# Need to parse to find title, link, score, number of comments
# Score computed with upvotes and downvotes

# Everything needed is under r['data']['children'] JSON object


def get_post_titles(r):
    """
    Get a list of post titles
    """
    posts = []
    for post in r["data"]["children"]:
        posts.append(post["data"]["title"])

    return posts


posts = get_post_titles(r)
print(posts)

def get_results(r):
    """
    Create DataFrame showing title, url, score, and number of comments
    """
    my_dict = {}
    for post in r["data"]["children"]:
        my_dict[post["data"]["title"]] = {
            "url": post["data"]["url"],
            "score": post["data"]["score"],
            "comments": post["data"]["num_comments"],
        }
    df = pd.DataFrame.from_dict(my_dict, orient="index")
    return df


df = get_results(r)

# r = get_reddit(subreddit, listing, 1, timeframe)
# for post in r["data"]["children"]:
#     for k in post["data"].keys():
#         print(k)
