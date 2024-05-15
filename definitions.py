from enum import Enum


class AddText(Enum):
    text = 'text'
    bold = 'bold'
    italic = 'italic'


class AddBulletPoint(Enum):
    text = 'text'
    numbers = 'numbers'


class AddHeading(Enum):
    text = 'text'
    level = 'level'


class AddFigure(Enum):
    image_path = 'image_path'
    title = 'title'
    width = 'width'
    height = 'height'
    figure_number = 'figure_number'


class AddTable(Enum):
    csv_path = 'csv_path'
    heading = 'heading'


class AddTitle(Enum):
    text = 'text'


class DocxFunctionKey(Enum):
    heading = "add_heading"
    title = "add_title"
    text = "add_text"
    figure = "add_figure"
    table = "add_table"
    bullet_point = "add_bullet_point"
    numbered_bullet_point = "add_bullet_point"
    page_break = "add_page_break"
    figure_list = "add_list_of_figures"


