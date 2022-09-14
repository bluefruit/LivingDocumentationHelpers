#!/usr/bin/env python3
import sys
import pathlib
from os import path
from glob import glob
from .collecting_formatter import CollectedStep
from .feature_file import load_feature_file
from jinja2 import Environment, FileSystemLoader


current_directory = pathlib.Path(__file__).parent.resolve()
env = Environment(loader=FileSystemLoader(current_directory, followlinks=True))
template = env.get_template('feature.jinja2')

status_to_style_dict = {
    'not run': 'notrun',
    # behave.model_core.Status
    'untested': 'notrun',
    'skipped': 'notrun',
    'passed': 'passed',
    'failed': 'failed',
    'undefined': 'notimplemented',
    'executing': 'notrun'
}


def status_to_style(status):
    return status_to_style_dict.get(status, 'failed')


def screenshots_from_step(step: CollectedStep):
    screenshots = []
    for line in step.text:
        line_text: str = line.strip()
        line_split = line_text.split("'")
        if len(line_split) == 3 and line_split[0] == 'Save screenshot ':
            screenshots.append(line_split[1])
    return screenshots

def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 2:
        print('Invalid command format, format is:\n {a[0]} <json feature result>\n'.format(a=args))
        exit(1)

    feature = load_feature_file(args[1])

    context = {
        "feature": feature,
        "status_to_style": status_to_style,
        "screenshots_from_step": screenshots_from_step
    }

    (file_name, _) = path.splitext(args[1])
    file_name += '.rst'

    with open(file_name, 'wt') as file:
        file.write(template.render(**context))


def process_files_in_current_directory():
    files = glob(path.join(path.curdir, '*.json'))

    for file in files:
        print(u'Converting {f}'.format(f=file))
        feature = load_feature_file(file)

        context = {
            "feature": feature,
            "status_to_style": status_to_style,
            "screenshots_from_step": screenshots_from_step
        }

        (file_name, _) = path.splitext(file)
        file_name += '.rst'

        with open(file_name, 'wt') as file:
            file.write(template.render(**context))


if __name__ == "__main__":
    main()
