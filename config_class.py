import configparser
import os


class Config:
    def __init__(self, file_path='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(file_path)
        # Docx Generator
        self.font_name = self.config.get('DOCX GENERATOR PARAMS', 'font_name')
        self.font_size = self.config.getint('DOCX GENERATOR PARAMS', 'font_size')
        self.output_docx_path = self.config.get('DOCX GENERATOR PARAMS', 'output_file_path')
        self.document_style = self.config.get('DOCX GENERATOR PARAMS', 'document_style')

        # JSON Generator
        self.output_json_path = self.config.get('JSON GENERATOR PARAMS', 'output_json_path')
