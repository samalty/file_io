# f is our variable, although we could have called it whatever we want
# When you get the results of the open function, 'f' stores an object. This is called a file handle, which allows us to manipulate our files.
# Attached to this object are various methods that we use for reading and writing the contents of our files
# If we type 'f.' in cloud9, a dropdown list will appear, showing us what methods are available to use

f = open('data.txt', 'r')
lines = f.read()

line = f.readline()