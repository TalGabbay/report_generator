class HeaderNumerizer:
    def __init__(self, max_depth=4):
        self.heading_level = 0
        self.heading_numbers = {i: 1 for i in range(max_depth)}

    def add_heading(self, text, level):
        if level > self.heading_level:
            self.heading_numbers[level] = 1
        else:
            self.heading_numbers[level] += 1

        for i in range(level + 1, 10):
            self.heading_numbers[i] = 1

        self.heading_level = level
        heading_number = '.'.join(str(self.heading_numbers[i]) for i in range(1, level + 1))
        heading_text = f"{heading_number} {text}"
        return heading_text
