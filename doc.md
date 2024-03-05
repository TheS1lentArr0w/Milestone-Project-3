# Documentation for Giveaway Hunter

## Automation
For my personal use case, I'm on a Windows 10 OS. This means that the CRON process takes the form of Task Scheduler and Windows batch (.bat) files.

----

Within the batch file, it's as simple as the below:

- Enter the path to your Python executable
- Put an explicit space
- Enter the path of app.py

If there's any whitespace in the filepaths above, wrap the filepath in " quotation marks.

E.g.

> C:\python3\python.exe C:\GiveawayHunter\app.py

---

To have this batch file automated, navigate to the 'Task Scheduler' on Windows and create a basic task.

Set the trigger to be however frequently you desire and have the action be to 'Start a Program' and navigate to the newly created batch file.