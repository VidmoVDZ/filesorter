import datetime
import toml
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
myFolder_workfiles = myFolder + "/workfiles"

myFolder_workfiles_word = myFolder_workfiles + "/word"
myFolder_workfiles_powerpoint = myFolder_workfiles + "/powerpoint"
myFolder_workfiles_excel = myFolder_workfiles + "/excel"
myFolder_workfiles_other = myFolder_workfiles + "/other"

magia = magic.Magic()
magia1 = magic.Magic(mime=True)

log_file = open(logs + f"LOGFILE_{hour}{minutes}{seconds}_{day}{month}{year}", "a")

if not Path(myFolder).exists():
	print("Folder not exist, create new one for you :)")
	os.system(f"mkdir {myFolder}")
	os.system(f"mkdir {myFolder_music}")
	os.system(f"mkdir {myFolder_txt}")
	os.system(f"mkdir {myFolder_photos}")
	os.system(f"mkdir {myFolder_workfiles}")
	os.system(f"mkdir {myFolder_workfiles_excel}")
	os.system(f"mkdir {myFolder_workfiles_powerpoint}")
	os.system(f"mkdir {myFolder_workfiles_word}")
else: print("Folder exists! Waiting!")

while True:
	try:
		for item in glob.glob(myFolder + "/*"):

			if Path(item).is_dir() == True:
				continue

			elif "Audio" in magia.from_file(item) or "audio" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_music}")
				os.system(f"mv '{item}' {myFolder_music}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_music}\n")
				
			elif "image" in magia.from_file(item) or "Image" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_photos}")
				os.system(f"mv '{item}' {myFolder_photos}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_photos}\n")
				
			elif "text" in magia.from_file(item) or "Text" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_txt}")
				os.system(f"mv '{item}' {myFolder_txt}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_txt}\n")

			elif "excel" in magia1.from_file(item) or "Excel" in magia1.from_file(item) or "Excel" in magia.from_file(item) or "excel" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_excel}")
				os.system(f"mv '{item}' {myFolder_workfiles_excel}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_excel}\n")

			elif "powerpoint" in magia1.from_file(item) or "Powerpoint" in magia1.from_file(item) or "PowerPoint" in magia.from_file(item) or "powerpoint" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_powerpoint}")
				os.system(f"mv '{item}' {myFolder_workfiles_powerpoint}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_powerpoint}\n")

			elif "word" in magia1.from_file(item) or "Word" in magia1.from_file(item) or "Word" in magia.from_file(item) or "word" in magia.from_file(item):
				print(f"[{day}.{month}.{year} ::: {hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_word}")
				os.system(f"mv '{item}' {myFolder_workfiles_word}")
				log_file.write(f"[{day}.{month}.{year}:::{hour}:{minutes}:{seconds}]Moved {item} to {myFolder_workfiles_word}\n")
	except FileNotFoundError:
		pass