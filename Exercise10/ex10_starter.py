import sys
import glob
import os


if sys.platform == 'win32':

    hdir = os.environ['HOMEPATH']

else:
    hdir = os.environ['HOME']

pattern = os.path.join(hdir, '*')


print(glob.glob(hdir))
files = glob.glob(pattern)
print()
print("******files within this folder****")
print("\n" .join(files))
print()
print("******size of each file****")
for filename in glob.glob(pattern):

    if os.path.getsize(filename) != 0:
        print(os.path.getsize(filename))
print()

print("******each file without it's path****")
print(os.path.basename(filename))
print()
