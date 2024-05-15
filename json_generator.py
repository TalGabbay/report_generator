import json
from config_class import Config
from definitions import *


class JsonGenerator:
    def __init__(self):
        self.config = Config("config.ini")
        self.json_file_path = self.config.output_json_path
        self.commands = []
        self.__figure_number = 0
        self.__list_of_figures = []

    def add_title(self, text):
        self.commands.append(
            {
                'type': DocxFunctionKey.title.name,
                'data': {
                        AddTitle.text.value: text,
                }
            }
        )

    def add_heading_1(self, text):
        self.__add_header(text, 1)

    def add_heading_2(self, text):
        self.__add_header(text, 2)

    def add_heading_3(self, text):
        self.__add_header(text, 3)

    def add_heading_4(self, text):
        self.__add_header(text, 4)

    def add_plain_text(self, text):
        self.__add_text(text)

    def add_bold_text(self, text, bold=True):
        self.__add_text(text,bold=bold)

    def add_italic_text(self, text, italic=True):
        self.__add_text(text, italic=italic)

    def add_bullet_point(self, text):
        """
        :param text:
        :return:
        """
        self.commands.append({
            'type': DocxFunctionKey.bullet_point.name,
            'data': {
                AddBulletPoint.text.value: text
            }
        })

    def add_number_point(self, text):
        self.commands.append({
            'type': DocxFunctionKey.numbered_bullet_point.name,
            'data': {
                AddBulletPoint.text.value: text,
                AddBulletPoint.numbers.value: True
            }
        })

    def add_table(self, csv_path, heading):
        self.commands.append({
            'type': DocxFunctionKey.table.name,
            'data': {
                AddTable.csv_path.value: csv_path,
                AddTable.heading.value: heading
            }
        })

    def add_figure(self, image_path, title, width=None, height=None):
        title = f"figure - {self.__figure_number} - " + title
        self.__list_of_figures.append(title)
        self.__figure_number += 1
        self.commands.append({
            'type': DocxFunctionKey.figure.name,
            'data': {
                AddFigure.image_path.value: image_path,
                AddFigure.title.value: title,
                AddFigure.figure_number.value: self.__figure_number,
                AddFigure.width.value: width,
                AddFigure.height.value: height
            }
        })

    def add_page_break(self):
        self.commands.append({
            'type': DocxFunctionKey.page_break.name,
            'data': {}
        })

    def __add_header(self, text, level):
        self.commands.append({
            'type': DocxFunctionKey.heading.name,
            'data': {
                AddHeading.text.value: text,
                AddHeading.level.value: level
            }
        })

    def __add_text(self, text, bold=False, italic=False):
        self.commands.append({
            'type': DocxFunctionKey.text.name,
            'data': {
                AddText.text.value: text,
                AddText.bold.value: bold,
                AddText.italic.value: italic
            }
        })

    def save(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.commands, file, indent=4)


if __name__ == '__main__':
    # Generator instance
    json_generator = JsonGenerator()

    # Run some basic commands
    json_generator.add_title("System integration blabla")

    # save file
    json_generator.save()