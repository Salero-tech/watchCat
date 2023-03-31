# email

Go to the [group](group.md) in the notification section to which you want to add a email(smtp) notification and copy over the following config.

```yml
mail:
    host: "smtp.gmail.com"
    port: 587
    user: "noreply@example.net"
    passwd: "*******"
    from_mail: "noreply@example.net"
    to_mail: ["admin@example.net", "admin2@example.net"]
```
 - **host**: SMTP-server host
 - **port**: SMTP port default: 587
 - **user**: user used to log in (probebly your email)
 - **passwd**: password used to login
 - **from_mail**: email which is used to send email notification
 - **to_mail**: a list of emails which will receive the notification