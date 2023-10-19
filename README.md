# SORTER, make your computer life better
Sorter is my one little part for "package" of bigger project to make a computer life easier (**MACLE**)

Sorter uses TOML config file to make it to config as simply as possible, however in plans for SORTER are:

- file size specified actions
- work files sorting and protection before removing (idk now how can i make it but i think it will be great to do this)
- more advanced iteration thru toml file
- and maybe many more


If you want to config sorter by yourself it's just simple as it looks for now:
```toml
[config]
folder = "/home/vidmo/Pulpit/myFolder" # folder where the sorter will work on
logs = "/home/vidmo/Pulpit/KRET/logs" # logs files location (where the logs stored)

# Ignore that section below (it will be changed)
[filetypes]
music = [ "mp3" ] # list of music file extensions like .mp3 .ogg etc
text = [ "txt" ]
images = [ "jpg", "jpeg", "png", "bmp" ]
```
  Have a good day/night.
  
