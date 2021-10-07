import os
if os.path.exists("demofile111.txt"):
  os.remove("demofile111.txt")
else:
  print("The file does not exist")
  
# Delete Folder
import os
os.rmdir("myfolder")
