from pathlib import Path

path = Path('cats.txt')
try:
    cat_contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    cat_contents = cat_contents.rstrip()
    print(cat_contents)

path = Path('dogs.txt')
try: 
    dog_contents = path.read_text()
except FileNotFoundError:
    print("The file is not found")#
else:
    dog_contents = dog_contents.rstrip()
    print(dog_contents)

