#
# Per eseguirlo aprire un terminale
# e lanciare il programma prova.py
#
import fileinput
import sys

files = fileinput.input()

for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Leggo da {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()
