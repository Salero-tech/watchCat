# discord

Go to the [group](group.md) in the notification section to which you want to add a discrod notification and copy over the following config.

```yml
discord:
    url: "https:// ...." #discord webhook
    onUpdate: "<@UserID>" #custom message
```
 - **url**: put in your discord webhook link: [instructions](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) (section "Making A Webhook")
 - **onUpdate**: add a message or/and ping a user. Pings have to be in the following format: <@UserID> [instructions to get a User id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)