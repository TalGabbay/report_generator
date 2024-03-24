import os
import json


class JsonGenerator:
    def __init__(self, json_file_path):
        self.json_file_path = os.path.join(json_file_path)
        self.commands = []

    def add_heading(self, text, level):
        self.commands.append({
            'type': 'add_heading',
            'data': {
                'text': text,
                'level': level
            }
        })

    def add_text(self, text):
        self.commands.append({
            'type': 'add_text',
            'data': {
                'text': text
            }
        })

    def add_bullet_point(self, text):
        self.commands.append({
            'type': 'add_bullet_point',
            'data': {
                'text': text
            }
        })

    def add_number_point(self, text):
        self.commands.append({
            'type': 'add_bullet_point',
            'data': {
                'text': text,
                'numbers': True
            }
        })

    def add_table(self, csv_path, heading):
        self.commands.append({
            'type': 'add_table',
            'data': {
                'csv_path': csv_path,
                'heading': heading
            }
        })

    def add_figure(self, image_path, title, width=None, height=None):
        self.commands.append({
            'type': 'add_figure',
            'data': {
                'image_path': image_path,
                'title': title,
                'width': width,
                'height': height
            }
        })

    def save(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.commands, file, indent=4)


if __name__ == '__main__':
    # Create a JsonGenerator instance
    json_generator = JsonGenerator('commands.json')

    # Add commands
    json_generator.add_heading('Heading 0', 0)
    json_generator.add_heading('Heading 1', 1)
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
