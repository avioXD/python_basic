# importing os module
import os
     
cwd = os.getcwd()   # Get the current working
print("Current working directory:", cwd)

new_dir = "os_test1"
# os.chdir('../') # Changing the CWD
path_dir =  os.getcwd()
print("Current working directory:", path_dir)
path = os.path.join(path_dir , new_dir) #creating new directory path
os.mkdir(path)
print("Directory '%s' created "% new_dir )


new_dir = "os_test2"
#os.chdir('../') # Changing the CWD
path_dir =  os.getcwd()
print("Current working directory:", path_dir)
mode = 0o666
path = os.path.join(path_dir , new_dir) #creating new directory path

os.mkdir(path)
print("Directory '%s' created "% new_dir )

print(os.listdir())
