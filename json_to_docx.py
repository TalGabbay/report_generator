import os.path
from docx_generator import DocxGenerator
import json


class JsonToDocx:

    def __init__(self, json_file_path, docx_generator_obj: DocxGenerator):
        self.json_file_path = os.path.join(json_file_path)
        self.command_dict = None
        self.funct_map = docx_generator_obj.function_map
        self.__load_json()

    def __load_json(self):
        with open(self.json_file_path, 'r') as file:
            # Load the JSON data into a dictionary
            self.command_dict = json.load(file)

    def execute_commands(self):
        for command in self.command_dict:
            cmd = command['type']
            cmd_args = command['data']
            self.funct_map[cmd](**cmd_args)


if __name__ == '__main__':
    JsonToDocx("commands.json", DocxGenerator('example1.docx')).execute_commands()

