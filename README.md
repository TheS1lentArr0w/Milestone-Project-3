# Giveaway Hunter (Milestone-Project-3)

## Short Description
3rd and final capstone project for my Python Bootcamp.

For usage, please refer to doc.md

## Initial Idea
Create bot that goes to [r/MechanicalKeyboards][r/mk] and checks all posts (e.g. once a day) for 'giveaway' in the title. 

When there is, send links to me in an email.

## Motivation
Allows me to get an update every day to see if there are any new posts indicating a giveaway. Within the email, a link will be provided leading to the original post. This will allow me to enter the giveaway.

## Patch Notes
### V1.1
- Updated app.py to grab email credentials from a config file rather than requiring manual entry. This allows for implementation of automation.
- Due to automation now being possible, a .bat file can be created to automatically run app.py (if on a Windows OS). This can be adapted to whatever OS required.

## Additional Functionality (Future)
* Expand functionality to include [r/MechanicalKeyboardsUK][r/mkuk]
* Turn it into a fullstack project by introducing a UI, having a way to store the emails in a database.
  * Find a way to integrate multiple things into the UI (e.g. pick which subreddit to search, pick keywords, pick how often the check runs)
  * Emailchimp for managing emails

## Study Links
* [Reddit API with Python Guide][reddit-api-with-python]

[r/mk]: https://www.reddit.com/r/MechanicalKeyboards/
[r/mkuk]: https://www.reddit.com/r/MechanicalKeyboardsUK/
[reddit-api-with-python]: https://www.jcchouinard.com/reddit-api/
