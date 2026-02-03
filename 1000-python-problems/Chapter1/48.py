# good question
import os
# Access all environment variables
print('*----------------------------------*')
print("Environment is ",os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print("home is ", os.environ['HOMEPATH'])
print('*----------------------------------*')
print("Path is ",os.environ['PATH'])
print('*----------------------------------*')
