

''''
1>>	r
Opens a file for reading only.
The file pointer is placed at the beginning of the file.
This is the default mode.

2>>	rb
Opens a file for reading only in binary format.
The file pointer is placed at the beginning of the file.
This is the default mode.

3>>	r+
Opens a file for both reading and writing.
The file pointer placed at the beginning of the file.

4>>	rb+
Opens a file for both reading and writing in binary format.
The file pointer placed at the beginning of the file.

5>>	w
Opens a file for writing only.
Overwrites the file if the file exists. If the file does not exist,
creates a new file for writing.

6>>	wb
Opens a file for writing only in binary format.
Overwrites the file if the file exists. If the file does not exist,
creates a new file for writing.

7>>	w+
Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist, creates a new file for reading and writing.

8>> wb+
Opens a file for both writing and reading in binary format.
Overwrites the existing file if the file exists.
If the file does not exist,
creates a new file for reading and writing.

9>> a
Opens a file for appending.
The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist,
it creates a new file for writing.

10>> ab
Opens a file for appending in binary format.
The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

11>> a+
Opens a file for both appending and reading.
The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

12>> ab+
Opens a file for both appending and reading in binary format.
The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''




# # create a file
fo = open("foo.txt", "w")
fo.write( "My name is Abhishek Das And I am learning Python")

# # Close opend file
fo.close()


# open a file read mode 
fo = open("foo.txt", "r+")
data = fo.read()
print(data)
fo.close()



# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

# Close opened file
fo.close()


#rename file :
import os

# delete a file : 
os.remove("sample.txt")

# Rename a file from test1.txt to test2.txt
os.rename( "foo.txt", "sample.txt" )

 