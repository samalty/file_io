# Variable f will open our relative_data txt file for reading. This is contained within a separate folder, and so we have used a relative path to access it.
# If we wanted to find the absolute path, we could enter 'readlink -f relative_data.txt' into git
# Then we call the read method, and put that within the variable lines
# Then we close our file handle before printing the results to screen

f = open('files/relative_data.txt', 'r') 
lines = f.read() 
f.close()
print(lines) 