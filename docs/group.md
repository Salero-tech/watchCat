# Manage your notitications in groups

## create a group

Go to the Notivication section in your config.yml file.
```yml
notification:
    default:
        discord: # rest of config
    backup:
        discord: # rest of config
    testing:
        discord: # rest of config
```
Add your group in the stile (default, backup, testing) shown above. **No spaces allowed!** [create notification for every group, see 4.](../README.md#quick-start)


## add a container to a group
Add the config below to your docker-compose.yml file you want to monitor. To add a container to multiple groups use a space.
```yml
labels:
    - "watchCat=True"
    - "watchCat.group=default backup"
```