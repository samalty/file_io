# The script below enables us to make changes to a separate txt file
# 'a' stands for append, meaning every time we enter something into the write function, it will add it to the pre-existing content, rather than overwriting everything. '\n' ensures that new content features on its own line.

f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.write("Hello\n")
f.writelines(lines)
f.close()