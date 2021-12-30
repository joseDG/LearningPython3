import sys

print(sys.version)
print(sys.version_info)

print(sys.platform)

print(len(sys.modules.keys()))

print(sys.prefix)

sys.stdout.write('Hi')

for inp in sys.stdin:
    print(inp, end = '')