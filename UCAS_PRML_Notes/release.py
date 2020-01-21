import os 
import shutil

pwd = os.getcwd()

release_path = pwd + "/release"

path = os.listdir()

for p in path:
	if p[0]=='.':
		continue
	if p == "release":
		continue
	if p == "数学知识":
		continue
	if p == "作业":
		continue
	if os.path.isdir(p):
		c_path = pwd + "/" + p
		file_list = os.listdir(c_path)
		for file in file_list:
			if file[-4:]==".pdf":
				shutil.copyfile(c_path + "/" + file, release_path + "/" + file)
				print(file)

	else:
		continue