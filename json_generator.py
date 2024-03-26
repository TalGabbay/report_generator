import os
import json
from config_class import Config
from definitions import *
# TODO change name to recipe generator


class JsonGenerator:
    def __init__(self):
        self.config = Config("config.ini")
        self.json_file_path = self.config.output_json_path
        self.commands = []

    def add_title(self, text):
        self.__add_header(text, 0)

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
        self.commands.append({
            'type': DocxFunctionKey.figure.name,
            'data': {
                AddFigure.image_path.value: image_path,
                AddFigure.title.value: title,
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
    # Create a JsonGenerator instance
    json_generator = JsonGenerator()
    json_generator.add_title("Docx Generator Example")
    json_generator.add_heading_1("Introduction")
    json_generator.add_plain_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    json_generator.add_heading_2("Section 1: Overview")
    json_generator.add_plain_text(
        "Nulla facilisi. Sed nec nisi id arcu luctus eleifend. Vivamus convallis velit ac eros blandit, "
        "ut interdum lorem dignissim.")
    json_generator.add_figure("resources/data.jpg", "data figure title")
    json_generator.add_figure("resources/data.jpg", "data figure title")
    json_generator.add_figure("resources/data.jpg", "data figure title")
    json_generator.add_figure("resources/data.jpg", "data figure title")
    json_generator.add_heading_3("Subsection 1.1: Background")
    json_generator.add_plain_text(
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.")
    json_generator.add_heading_3("Subsection 1.2: Objectives")
    json_generator.add_plain_text("Duis ac efficitur est. Nam ullamcorper magna quis ante auctor fringilla.")
    json_generator.add_heading_2("Section 2: Methodology")
    json_generator.add_plain_text("Suspendisse nec condimentum libero. Donec et diam nec urna gravida tempus.")

    # Adding formatted text
    json_generator.add_bold_text("This is important information.")
    json_generator.add_italic_text("Note: Please pay attention to the following details.")

    # Adding bullet points
    json_generator.add_bullet_point("Point 1: Lorem ipsum dolor sit amet.")
    json_generator.add_bullet_point("Point 2: Consectetur adipiscing elit.")
    json_generator.add_bullet_point("Point 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    # Adding numbered bullet points
    json_generator.add_number_point("Step 1: Lorem ipsum dolor sit amet.")
    json_generator.add_number_point("Step 2: Consectetur adipiscing elit.")
    json_generator.add_number_point("Step 3: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    # Adding a table
    json_generator.add_table("resources/data.csv", "Data Summary")

    # Add different level headings
    json_generator.add_page_break()
    json_generator.add_title("Header numeration check")
    json_generator.add_heading_1("Introduction")
    json_generator.add_heading_2("Background")
    json_generator.add_heading_3("Historical Context")
    json_generator.add_heading_2("Objectives")
    json_generator.add_heading_1("Methodology")
    json_generator.add_heading_2("Data Collection")
    json_generator.add_heading_2("Data Analysis")
    json_generator.add_heading_3("Quantitative Analysis")
    json_generator.add_heading_3("Qualitative Analysis")
    json_generator.add_heading_1("Results")
    json_generator.add_heading_2("Statistical Findings")
    json_generator.add_heading_3("Correlation Analysis")
    json_generator.add_heading_3("Regression Analysis")
    json_generator.add_heading_2("Qualitative Insights")
    json_generator.add_heading_1("Conclusion")
    json_generator.add_heading_2("Summary")
    json_generator.add_heading_2("Recommendations")

    # Save the JSON file
    json_generator.save()
