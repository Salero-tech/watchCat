# watch cat

Tired of checking if your docker containers are up to date manually? Watch cat checks all specified containers periodically for updates from the regrestry.


## futures

 - allows you to specify which containers should be monitored
 - specify who to contact when updates are available via groups
 - specify check cycle
 - run at specified time

| Message Service  | Status |
|------------------|--------|
| discord          | ✅     |
| email            | ✅     |

## quick start

 1. Download the Docker-Compose file & and **change the timezone to suit you**:
    ```bash
    wget https://raw.githubusercontent.com/Salero-tech/watchCat/main/docker-compose.yml
    ```

 2. create config folder & download config file
    ```bash
    mkdir config && cd config && wget https://raw.githubusercontent.com/Salero-tech/watchCat/main/src/config/config.yml
    ```

 3. edit the config file for your prefered update cycle
    - **every** specifies the interval of days
    - **time** is the time of day the update check runs
    ```yml
    interval:
        every: 1 # every day: 1, every two days: 2, etc
        time: "02:30" # run at 2:30 in the morning
    ```

 4. To setup your notification:
    - [organzie notifications in groups](docs/group.md)
    - [discord](docs/discord.md)
    - [mail](docs/mail.md)

 5. Add container to be monitored (if no group is specified the container is added to group "default"; [more details](docs/group.md)): <br>
    docker-compose:
    ```yml
    labels:
        - "watchCat=True"
        - "watchCat.group=default"
    ```
    CLI:
    ```bash
    docker run -l watchCat=True hello-world:latest
    ```

 6. start the container:
    ```bash
    docker-compose up -d
    ```