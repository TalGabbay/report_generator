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

    def add_paragraph(self, text):
        self.commands.append({
            'type': 'add_paragraph',
            'data': {
                'text': text
            }
        })

    def set_text(self, text):
        self.commands.append({
            'type': 'set_text',
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
            'type': 'add_number_point',
            'data': {
                'text': text
            }
        })

    def add_table(self, file, heading):
        self.commands.append({
            'type': 'add_table',
            'data': {
                'file': file,
                'heading': heading
            }
        })

    def save(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.commands, file, indent=4)


if __name__ == '__main__':
    # Create a JsonGenerator instance
    json_generator = JsonGenerator('commands.json')

    # Add commands
    json_generator.add_heading('Main Heading', 1)
    json_generator.add_paragraph('This is an example of using JsonGenerator to create a JSON document.')
    json_generator.set_text(
        'We can include various components such as headings, text, bullet points, figures, and tables.')
    json_generator.add_bullet_point('Bullet point 1')
    json_generator.add_bullet_point('Bullet point 2')
    json_generator.add_number_point('Numbered point 1')
    json_generator.add_number_point('Numbered point 2')
    json_generator.add_table('blabla.csv', 'table heading')

    # Save the JSON file
    json_generator.save()
