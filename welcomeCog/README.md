# WelcomeCog
this is the kanium guild welcome cog. it sends a direct message to a user who has joined the kanium discord with a [message](./data/embedded_message.json) thats been templated in a json format.

# How to use:

in order to use our cog you would need to install it onto your instance of [RedBot](https://github.com/Cog-Creators/Red-DiscordBot).


## requirments:

- Instance of [RedBot](https://github.com/Cog-Creators/Red-DiscordBot)
- Downloader cog has to be loaded. to load:
    ```[Prefix]load downloader```

## The commands:

1. ```[PREFIX]repo add [RepoName] https://github.com/Kanium/KaniumCogs [ActiveBranch  (EX: Master)] ```
2. ```[PREFIX]cog install [RepoName] welcomeCog```
3. ```[PREFIX]load welcomeCog```

### To update the Cog:
- ```[PREFIX]repo update [RepoName]```

### To modify the sent message:

if you would like to modify the message to your liking, you can either :
- fork the bot. change the [message](./data/embedded_message.json) and [welcome.py](./welcome.py) line 9 to your repo.
- fork the bot. update the [welcome.py](./welcome.py) line 9 to be directed to your message.json file that you like without having it hosted on github with your repo.
