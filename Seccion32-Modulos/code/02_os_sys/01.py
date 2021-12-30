
import os   # operating system

print(list(os.environ.keys()))
# ['PATH', 'HOME', 'USER', 'PWD', ..... ]

print(os.environ['HOME'])
print(os.environ['USER'])
print(os.environ['PWD'])
# location of the standard Python libraries
print(os.environ.get('PYTHONHOME'))


# careful if key !exist
print(os.environ.get('nnnnn'))  # Always None in new session
os.environ['nnnnn'] = 'Only in this session'

# os.environ doesn’t overwrite the system vars
# to overwrite: use shell environment, such as Bash
# Future reading: python-dotenv