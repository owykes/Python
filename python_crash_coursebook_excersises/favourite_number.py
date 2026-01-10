from pathlib import Path
import json

    
path = Path('favourite_number.json')
if path.exists():
    contents = path.read_text()
    favourite_number = json.loads(contents)
    print(f"{favourite_number}")
else:
    while True:
        try:
            favourite_number = int(input("Enter your favourite number: "))
        except ValueError:
            print("please enter an integer")
        else:
            break
    contents = json.dumps(favourite_number)
    path.write_text(contents)
    

