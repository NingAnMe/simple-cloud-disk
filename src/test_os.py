import os

src_dir = os.path.abspath(os.path.dirname(__file__))

s_dir = os.path.dirname(src_dir)

print(src_dir)
print(s_dir)

files_found = os.listdir(src_dir)
files_found.sort()

dirs = list()
files = list()
for f in files_found:
    if os.path.isdir(f):
        dirs.append(f)
    elif os.path.isfile(f):
        files.append(f)

print(files)
