import unittest
from kivy.uix.label import Label


class LabelEmptyMarkupTestCase(unittest.TestCase):
    def test_empty_markup(self):
        label = Label(text='[b][/b]', markup=True)
        label.texture_update()
        self.assertTrue(label.texture is not None)
        self.assertEqual(label.texture.width, 1)
        self.assertEqual(label.texture.height, 1)
