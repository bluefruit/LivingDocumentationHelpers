import sys
from os import path
from .template import convert_template
from .userneeds import load_userneeds_from_file

def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 2:
        print('Invalid command format, format is:\n {a[0]} <userneed text file>\n'.format(a=args))
        exit(1)

    userneeds = load_userneeds_from_file(args[1])

    context = {
        "userneeds": userneeds
    }

    (file_name, _) = path.splitext(args[1])
    file_name += '.rst'

    with open(file_name, 'wt') as file:
        file.write(convert_template('userneeds.jinja2', context))


if __name__ == "__main__":
    main()
