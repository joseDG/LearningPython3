import ourlib
print('After importing ourlib')

print(f'__file__ {__file__}')
print(f'__name__ {__name__}')

# No effect. Loaded once!
import ourlib
import ourlib
import ourlib

if __name__ == '__main__':
    # Only the script you run has:
    # __name__ = '__main__'
    # Otherwise: file name
    print('Script from program1')