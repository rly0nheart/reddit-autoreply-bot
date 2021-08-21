# Reddit autoreply bot
![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/reddit.autoreply.bot?style=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/reddit.autoreply.bot/badge)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/reddit.autoreply.bot)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/reddit.autoreply.bot)
<a href="https://www.reddit.com/u/rly0nheart/"><img  alt="Reddit" src="https://img.shields.io/badge/Reddit-u/rly0nheart-orange?style=flat&logo=reddit"></a>
![Twitter](https://img.shields.io/twitter/follow/rly0nheart?&style=flat&logo=twitter)


A Reddit auto-reply bot.

# Prerequisites
* Reddit Account

*If you don't have an account, consider creating one.*

*If you have an account, you can also create a separate account for your bot.*

# Get Access Keys
*Assuming you're logged in to your account*

* Create an app [here](https://old.reddit.com/prefs/apps).

* Click the "*Create app*" button. Fill out the form like so:

**name:** Your app name

**App type:** Choose the script option

**description:** You can leave this blank

**about url:** You can leave this blank

**redirect url:** http://www.example.com (We won't be using this as a redirect)

> **NOTE**: These examples will only work for script type apps, which will ONLY have access to accounts registered as "developers" of the app and require the application to know the user's password. 

* Hit the "create app" button. Make note of the **client ID** and **client secret**. For the rest of this page, it will be assumed that:

*Your username is*: reddit_bot

*Your password is*: abc123

*Your app's client ID is*: p-jcoLKBynTLew

*Your app's client secret is*: gko_LXELoV07ZBNUXrvWZfzE3aI

You will use these in the *config/credentials.py* file.

> **NOTE**: You should NEVER post your client secret (or your reddit password) in public. If you create a bot, you should take steps to ensure that the bot's password and the app's client secret are secured against digital theft. The client IDs, secrets, tokens and passwords used here are, obviously, fake and invalid.

# Installation
**Clone this repo**:
> git clone https://github.com/rlyonheart/reddit.autoreply.bot

> cd reddit.autoreply.bot

> pip3 install -r requirements.txt

# Usage
> python3 bot.py
