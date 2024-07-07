# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt", "rt")

print(f.readline())
for x in f:
  print(x)
f = open("myfile.txt", "x") # create
f = open("demofile2.txt", "a") # append
f = open("demofile2.txt", "w") # overwrite
f.write("Now the file has more content!")
f.close()

# Delete file
import os
os.remove("demofile.txt") 
# Check existence
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 
# Remove Direction
os.rmdir("myfolder") 