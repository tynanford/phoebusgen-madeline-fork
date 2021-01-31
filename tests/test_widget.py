import sys
sys.path.insert(1, '../phoebusgen/widget/')
sys.path.insert(1, './phoebusgen/widget/')
import unittest
import _widget


class TestWidgetClass(unittest.TestCase):
    def setUp(self):
        self.base_type = 'test_widget_type'
        self.base_name = 'Just Basic Widget Test'
        self.base_x = 10
        self.base_y = 12
        self.base_width = 14
        self.base_height = 15

    def create_basic_widget(self):
        return _widget._Widget(self.base_type, self.base_name, self.base_x,
                               self.base_y, self.base_width, self.base_height)

    def test_basic_widget(self):
        widget_type = 'label'
        name = 'Label_1'
        x = 10
        y = 12
        width = 14
        height = 15
        w = _widget._Widget(widget_type, name, x, y, width, height)
        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'label')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(height))

    def test_visible(self):
        w = self.create_basic_widget()

        self.assertEqual(w.root.tag, 'widget')
        self.assertEqual(w.root.attrib['type'], 'test_widget_type')
        self.assertEqual(w.root.attrib['version'], '2.0.0')

        self.assertEqual(len(w.root), 5)
        for child in w.root:
            if child.tag == 'name':
                self.assertEqual(child.text, self.base_name)
            elif child.tag == 'x':
                self.assertEqual(child.text, str(self.base_x))
            elif child.tag == 'y':
                self.assertEqual(child.text, str(self.base_y))
            elif child.tag == 'width':
                self.assertEqual(child.text, str(self.base_width))
            elif child.tag == 'height':
                self.assertEqual(child.text, str(self.base_height))

        w.visible(False)
        self.assertEqual(len(w.root), 6)
        for child in w.root:
            if child.tag == 'visible':
                self.assertEqual(child.text, 'False')



if __name__ == '__main__':
    unittest.main()
