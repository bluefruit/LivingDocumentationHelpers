import pathlib
from jinja2 import Environment, FileSystemLoader

current_directory = pathlib.Path(__file__).parent.resolve()
env = Environment(loader=FileSystemLoader(current_directory, followlinks=True))

def convert_template(filename, context):
    template = env.get_template(filename)
    return template.render(**context)
