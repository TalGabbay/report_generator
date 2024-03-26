import os.path

from config_class import Config
from docx_generator import DocxGenerator
from definitions import DocxFunctionKey
import json

# TODO Numerize headings following convention.
# TODO Add functionality to build list of all figures.


class JsonToDocx:

    def __init__(self, docx_generator_obj: DocxGenerator):
        self.config = Config("config.ini")
        self.json_file_path = os.path.join(self.config.output_json_path)
        self.command_dict = None
        self.funct_map = docx_generator_obj.function_map
        self.__load_json()

    def __load_json(self):
        with open(self.json_file_path, 'r') as file:
            # Load the JSON data into a dictionary
            self.command_dict = json.load(file)

    def execute_commands(self):
        for command in self.command_dict:
            type = command['type']
            # TODO Add type validation
            cmd = DocxFunctionKey[type].value
            cmd_args = command['data']
            self.funct_map[cmd](**cmd_args)


if __name__ == '__main__':
    JsonToDocx(DocxGenerator()).execute_commands()

