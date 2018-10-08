import os

path, dirs, files = next(os.walk("content/r18")) #change dir accordingly
file_count = len(files)
print(file_count)