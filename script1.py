import sys
import math
import pyperclip as pc



input = sys.argv[1:]

pc.copy(' '.join(input))

print(pc.paste())

