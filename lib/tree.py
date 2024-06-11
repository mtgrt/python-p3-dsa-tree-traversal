

class Tree:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def get_element_by_id(self, element_id):
        for element in self.elements:
            if element['id'] == element_id:
                return element
        return None

