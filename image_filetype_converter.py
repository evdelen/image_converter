#! python3

# A simple file type converter that preserves the Date Modified value from the original image.



from PIL import Image
import os, os.path


path = input('Path: ({}) > '.format(os.getcwd())
if not path: path = os.getcwd()
ext_from = input('Convert from extension: (webp) > ').lower()
if not ext_from: ext_from = 'webp'
ext_to = input('Convert to extension: (png) > ').lower()
if not ext_to: ext_to = 'png'
if not ext_to.startswith('.'): ext_to = '.' + ext_to
while True:
    del_after_convert = input('Delete original file? [y/n] (y) > ').lower()
    if not del_after_convert: del_after_convert = 'y'
    if del_after_convert in ['y', 'n']: break
ext_format_dict = {'.jpg': 'jpeg',
                   '.jpeg': 'jpeg',
                   '.png': 'png',
                   '.webp': 'webp',
                   '.bmp': 'bmp',
                   '.gif': 'gif'}
ext_format = ext_format_dict[ext_to] if ext_to in ext_format_dict else None
if not ext_format: raise

files_to_process = {}

print('Finding Files')
for filename in os.listdir(path):
    if filename.endswith(ext_from):
        print(filename)
        files_to_process[filename] = []

print('=============')
print('Converting Files')

for filename in files_to_process.keys():
    orig_path = os.path.join(path, filename)
    nof = filename
    nof.strip(ext_from)
    dest_path = os.path.join(path, nof + ext_to)
    print(orig_path + ' > ' + dest_path)
    im = Image.open(orig_path).convert('RGB')
    im.save(dest_path, '')
    file_stat = os.stat(orig_path)
    os.utime(dest_path, (file_stat.st_atime, file_stat.st_mtime))
    if del_after_convert == 'y': os.remove(os.path.join(path, filename))

a = input('OPERATION COMPLETE - Press Any Key to Exit')
