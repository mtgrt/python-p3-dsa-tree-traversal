# get_element_by_id_test.py

import pytest
from tree import Tree

class TestTree:
    def test_get_element_by_id(self):
        tree = Tree()
        tree.add_element({'id': 'heading', 'tag_name': 'h1', 'text_content': 'Title', 'children': []})
        
        # Update the assertion to compare the returned value properly
        assert tree.get_element_by_id('heading') == {'id': 'heading', 'tag_name': 'h1', 'text_content': 'Title', 'children': []}
