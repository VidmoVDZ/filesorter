import datetime
import toml
import time
import magic
import glob
import os
import pathlib
from pathlib import Path

date = datetime.datetime.now()

hour = date.hour
minutes = date.minute
seconds = date.second

year = date.year
month = date.month
day = date.day




config = toml.load(f="./configs/sorter.toml")

logs = config['config']['logs'] + "/"

myFolder = config['config']['folder']
myFolder_music = myFolder + "/music"
myFolder_photos = myFolder + "/images"
myFolder_txt = myFolder + "/txt_files"

magia = magic.Magic()

log_file = open(logs + f"LOGFILE_{hour}{minutes}{seconds}_{day}{month}{year}", "a")

if not Path(myFolder).exists():
	print("Folder not exist, create new one for you :)")
	os.system(f"mkdir {myFolder}")
	os.system(f"mkdir {myFolder_music}")
	os.system(f"mkdir {myFolder_txt}")
	os.system(f"mkdir {myFolder_photos}")
else: print("Folder exists! Waiting!")

while True:
	try:
		for item in glob.glob(myFolder + "/*"):
			for i in config["filetypes"]['music']:
				if Path(item).is_dir() == True:
					continue
				elif "Audio" in magia.from_file(item) or "audio" in magia.from_file(item):
					print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_music}")
					os.system(f"mv '{item}' {myFolder_music}")
					log_file.write(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_music}\n")
					
					
			for i in config["filetypes"]['images']:
				if Path(item).is_dir() == True:
					continue
				elif "image" in magia.from_file(item) or "Image" in magia.from_file(item):
					print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_photos}")
					os.system(f"mv '{item}' {myFolder_photos}")
					log_file.write(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_photos}\n")
					
			for i in config["filetypes"]['text']:
				if Path(item).is_dir() == True:
					continue 
				elif "text" in magia.from_file(item) or "Text" in magia.from_file(item):
					print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_txt}")
					os.system(f"mv '{item}' {myFolder_txt}")
					log_file.write(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_txt}\n")
					
	except FileNotFoundError:
		pass
