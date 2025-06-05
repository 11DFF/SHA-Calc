import hashlib
import sys

SupportedAlgo = hashlib.algorithms_available
version = '1.1'
CreditsAndLicense = 'This code written by 11DFF and licensed under MIT License.'\
                    '\nTo view full license text, open "LICENSE" file'

# Checking argument1
try:
    argument1 = sys.argv[1]
except IndexError:
    print('Error: argument1 not defined\nTry "python shacalc.py -h" in CMD.exe or Terminal')
    input('Press ENTER to exit...')
    sys.exit()

# Help page
if argument1 == '-help' or argument1 == '-h' or argument1 == '--help':
    print('Usage: python shacalc.py <algorithm> <file>' # PEP8
          '\nExample: python shacalc.py sha256 "E:/test.txt"'
          '\nYou can see all supported algorithms in your os with argument "-algo"')
    sys.exit()

# Algorithms page
if argument1 == '-algo' or argument1 == '-algorithm' or argument1 == '--algorithm':
    print('Supported algorithms (including OpenSSL installed in your system):')
    print(SupportedAlgo)
    print('Supported algorithms (only "hashlib" python module, 100% support):')
    print(hashlib.algorithms_guaranteed)
    sys.exit()

# Version display
if argument1 == '-v' or argument1 == '-V' or argument1 == '--version':
    print('SHA-Calc version: ',version,sep='')
    sys.exit()

# Credits
if argument1 == '-credits' or argument1 == '--credits' or argument1 == '-license' or argument1 == '--license':
    print('Credits: ',CreditsAndLicense,sep='')
    sys.exit()

# Selecting algorithm
if argument1 in SupportedAlgo:
    filehash = hashlib.new(argument1)
else:
    print('Error: Unsupported algorithm: ',argument1,'\nTry "python shacalc.py -h"',sep='')
    sys.exit()

# Checking argument2
try:
    argument2 = sys.argv[2]
    file = open(argument2, "rb")
    filehash.update(file.read())
except IndexError:
    print('Error: argument2 not defined')
    sys.exit()
except FileNotFoundError:
    print('Error: File "',argument2,'" not found',sep='')
    sys.exit()

# Print hash and finish
print(filehash.hexdigest())
sys.exit(0)
