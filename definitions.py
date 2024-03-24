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


class AddTable(Enum):
    csv_path = 'csv_path'
    heading = 'heading'
