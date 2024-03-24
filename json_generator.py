import os
import json
from config_class import Config
from definitions import *
# TODO change name to recipe generator
# TODO change type from function name to key for instance add_heading -> heading
# TODO export extra functionality to different functions heading0(text) instead of heading("text",0)

class JsonGenerator:
    def __init__(self):
        self.config = Config("config.ini")
        self.json_file_path = self.config.output_json_path
        self.commands = []

    def add_heading(self, text, level):
        self.commands.append({
            'type': 'add_heading',
            'data': {
                AddHeading.text.value: text,
                AddHeading.level.value: level
            }
        })

    def add_text(self, text, bold=False, italic=False):
        self.commands.append({
            'type': 'add_text',
            'data': {
                AddText.text.value: text,
                AddText.bold.value: bold,
                AddText.italic.value: italic
            }
        })

    def add_bullet_point(self, text):
        """
        :param text:
        :return:
        """
        self.commands.append({
            'type': 'add_bullet_point',
            'data': {
                AddBulletPoint.text.value: text
            }
        })

    def add_number_point(self, text):
        self.commands.append({
            'type': 'add_bullet_point',
            'data': {
                AddBulletPoint.text.value: text,
                AddBulletPoint.numbers.value: True
            }
        })

    def add_table(self, csv_path, heading):
        self.commands.append({
            'type': 'add_table',
            'data': {
                AddTable.csv_path.value: csv_path,
                AddTable.heading.value: heading
            }
        })

    def add_figure(self, image_path, title, width=None, height=None):
        self.commands.append({
            'type': 'add_figure',
            'data': {
                AddFigure.image_path.value: image_path,
                AddFigure.title.value: title,
                AddFigure.width.value: width,
                AddFigure.height.value: height
            }
        })

    def save(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.commands, file, indent=4)


if __name__ == '__main__':
    # Create a JsonGenerator instance
    json_generator = JsonGenerator()

    # Add commands
    json_generator.add_heading('fghjfhk', 0)
    json_generator.add_heading('Heading 1', 1)
    json_generator.add_text(
        'We can include various components such as headings,'
        ' text, bullet points, figures, and tables.\n'
        'also this section will store whitespaces new line and more\n'
        'bye')
    json_generator.add_heading('Heading 1', 1)
    json_generator.add_text(
        'We can include various components such as headings,'
        ' text, bullet points, figures, and tables.\n'
        'also this section will store whitespaces new line and more\n'
        'bye')
    json_generator.add_heading('Heading 2', 2)
    json_generator.add_heading('Heading 3', 3)
    json_generator.add_text(
        'We can include various components such as headings,'
        ' text, bullet points, figures, and tables.\n'
        'also this section will store whitespaces new line and more\n'
        'bye')
    json_generator.add_text(
        'We can include various components such as headings,'
        ' text, bullet points, figures, and tables.\n'
        'also this section will store whitespaces new line and more\n'
        'bye')
    json_generator.add_heading('Heading 1', 1)
    json_generator.add_bullet_point('Bullet point 1')
    json_generator.add_bullet_point('Bullet point 2')
    json_generator.add_number_point('Numbered point 1')
    json_generator.add_number_point('Numbered point 2')
    json_generator.add_heading('Heading 2', 2)
    json_generator.add_table(r'C:\Users\talgab\PycharmProjects\report_generator\figure.csv', 'table heading')
    json_generator.add_figure(r'C:\Users\talgab\OneDrive - Mobileye\Pictures\Picture1.jpg', 'table heading')

    # Save the JSON file
    json_generator.save()
