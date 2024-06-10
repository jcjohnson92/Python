import argparse
import os
from time import strftime

def create_header(user):
    border = "#" * 100
    date = strftime("%a, %d %b %Y")
    created = (f"\n# Created by {user}")
    creation = (f"\n# Date Created: {date}\n")
    header = border + date + created + creation  + border
    return header

def file_creation(path, filename, program, user):
    file_extension = None
    x = create_header(user)
    if program == '.html':
        file_extension = program
        print(f"Creating {file_extension}")
        # Create html File
        html = open(path + "/" + filename + "/" + filename + file_extension, 'w')
        html.write(x)
        html.close()
        # Create CSS file
        css = open(path + "/" + filename + "/" + "style.css", 'w')
        css.write(x)
        css.close()
        # Create Javascript file
        js = open(path + "/" + filename + "/" + "js.js", 'w')
        js.write(x)
        js.close()

    else:
        file_extension = program
        python = open(path + "/" + filename + "/" + filename + file_extension, 'w')
        python.write(x)
def folder_creation(filename, path):
    os.mkdir(path + "/" + filename)

def main():
    parser = argparse.ArgumentParser(
        prog="Project Starter",
        description="Create folder and file for new coding project",
        epilog="I DONT KNOW"
    )

    parser.add_argument('filename', help="Name of file")
    parser.add_argument('-u', '--user', help="User creating", default='Joshua Johnson')
    parser.add_argument('-p', '--program', help="Type of programming code", default='python')
    parser.add_argument('-l', '--location', help="Directory location [Default: Current location]", default=os.getcwd())
    args = parser.parse_args()
    path = args.location
    print(f"Creating folder at {args.location}")
    folder_creation(filename=args.filename, path=path)
    print("Creating Files")
    file_creation(path=args.location, filename=args.filename, program=args.program, user=args.user)


if __name__ == "__main__":
    main()