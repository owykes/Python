from pathlib import Path

path = Path('guest.txt')
name = input("Write your name: ")
path.write_text(name)




