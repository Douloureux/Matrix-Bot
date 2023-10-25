# Matrix Bot

A simple bot based on [matrix-nio](https://github.com/poljar/matrix-nio), designed for the [Matrix]("https://matrix.org") communication protocol.

# Features 

This bot's features include, but are not limited to:

## Matrix

+ [XKCD](https://xkcd.com/) within Matrix
+ Sends you the latest news.
+ Tells you about the weather.
+ Gives you Urban Dictionary definitions.
+ Has a database of fundamental physical constants so you won't forget them.
+ Can give you data about all the elements in the periodic table.
+ Notifies you about uploads to YouTube.
+ Rate command 
+ Garfield comics*
+ Automatic tracker remover for links.

## Server Maintenance 

+ CPU temperature of the server (Raspberry Pi only).
+ Limited shell access from matrix. (can be disabled for security)
+ Updates software and reports it to your specified channel.
+ Server specific features.

# Setup 

Only supports Linux. The system update features (located in the `scheduler` folder) are system specific, and you have to modify the code based on your needs.
The given scripts are examples for what can be done. 

## Debian 11

Required dependencies:

```sudo apt install libolm-dev libpython3.9-dev libpython3-dev build-essential```

Python dependencies:

```pip install -r requirements.txt```

Move `env.example` to .env and add the required information (JSON format):
+ homeserver: The homeserver that the bot runs on.
+ owner_username: Your matrix account's username, to accesss developer commands.
+ username: The bot's username.
+ password: The bot's password.
+ github: The GitHub API token, optional in case you don't use the server features.
+ weather: An Open-Meteo API request link that can be generated [here](https://open-meteo.com/en/docs)

If you are using the server features, make sure you modify the `vars` file in the scheduler folder.

To run the bot, `python3 main.py`

# *Garfield Comic support

Download https://archive.org/details/Garfield-Comic-Strips, and extract all the images to ./assets/comics.