from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
contents = contents.rstrip()

print(contents)

python_string = ''
for line in contents.splitlines():
    line = line.replace('Python','C')
    python_string += line
print(python_string)