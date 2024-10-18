import os
files = {}
print(os.getcwd())
for dir in (os.walk('F:/')):
# for dir in (os.walk(os.getcwd()+'/get_large_files_os')):
    for file in dir[2]:
        if (os.path.getsize(dir[0]+'\\'+file)>5368709120): #5GB
            files[file] = {dir[0] : os.path.getsize(dir[0]+'\\'+file)}
        # if file[str.rfind(file,'.')+1:] in files.keys():
        #     files[file[str.rfind(file,'.')+1:]] += 1
        # else:
        #     files[file[str.rfind(file,'.')+1:]] = 1
print(files)