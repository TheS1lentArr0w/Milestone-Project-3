"""
Milestone Project 3
"""




### Imports
import requests
import smtplib
import getpass
import config

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
    """
    Template of sending an email from Udemy course
    """
    smtp_object = smtplib.SMTP('smtp-mail.outlook.com',587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = config.configUser
    password = config.configPass
    smtp_object.login(email,password)
    
    from_address = email
    to_address = email
    subject = "Giveaway Hunter Update"
    # Creating message
    message = "Today's links\n\n"
    for i,post in enumerate(posts):
        message += post
        message += "\n"
        message += links[i]
        message += "\n\n"
    message += "That's all!"

    msg_parts = ("From: " + from_address,
            "To: " + to_address,
            "Subject: " + subject,
            "", message)
    msg = "\n".join(msg_parts)
    smtp_object.sendmail(from_address,to_address,msg)
    smtp_object.quit()

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

# Send email if relevant posts discovered
if posts == [] or links == []:
    # Didn't find any relevant posts
    print("Nothing today!")
else:
    send_email(posts,links)

"""
Reference links
https://github.com/reddit-archive/reddit/wiki/API
"""