import sys
from os import listdir, path, mkdir
from PIL import Image

def list_files_with_part_in_name_in_dir(dir_path,part):	
	onlyfiles = [dir_path+f for f in listdir(dir_path) if path.isfile(path.join(dir_path, f)) and part in f]
	return onlyfiles

if __name__ =='__main__':
	if len(sys.argv) !=3 :
		print("please pass source directory and destination directory")
		exit()

	source_dir_path = sys.argv[1]
	destination_dir_path = sys.argv[2]

	if not path.exists(source_dir_path):
		print("please provide an existing directory contaning images as source path")
		exit()
	if not path.isdir(source_dir_path):
		print("source is not a directory!!!")
		exit()
	print(f"using source path: {source_dir_path}")

	if path.exists(destination_dir_path) :
		if not path.isdir(destination_dir_path):
			print("destination is not a directory")
			exit()
	else : 
		print("destination dir doesn\'t exist \ncreating one...")
		mkdir(destination_dir_path)
		print(f"directory with name {destination_dir_path.replace('/','')} created")
	print(f"using destination path {destination_dir_path}")

	files_path_list = list_files_with_part_in_name_in_dir(source_dir_path,'.jpg')

	print(f"found jpg images : {files_path_list}")

	if len(files_path_list) > 0:
		print(f"found {len(files_path_list)} files to be converted")
		for image_path in files_path_list:
			print(f"processing {image_path}")
			img = Image.open(image_path)
			new_file_name = img.filename.replace(source_dir_path,destination_dir_path).replace('.jpg','.png')
			print(new_file_name)
			img.save(new_file_name,'png')
			print(f'converted to png and saved : {new_file_name}')
	print("------------------------------------------")
	print("happy converting :)")