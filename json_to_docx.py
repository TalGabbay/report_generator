import os.path

from docx_generator import DocxGenerator
import json

class DocxToJson:

    def __init__(self, json_file_path):
        self.json_file_path = os.path.join(json_file_path)
        self.docx_generator_map = None

