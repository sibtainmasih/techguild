import unittest

from html_tag import html_tag

class HTMLTagTests(unittest.TestCase):

    """Tests for html_tag."""

    def assertTagEqual(self, tag1, tag2):
        split1 = tag1[1:-1].split(' ')
        name1, attrs1 = split1[0], split1[1:]
        split2 = tag2[1:-1].split(' ')
        name2, attrs2 = split2[0], split2[1:]
        self.assertEqual(name1, name2)
        self.assertEqual(sorted(attrs1), sorted(attrs2))
        self.assertEqual(tag1[0], tag2[0])
        self.assertEqual(tag1[-1], tag2[-1])

    def test_input(self):
        html = html_tag("input", type="email", name="email",
                        placeholder="E-mail")
        expected = '<input name="email" placeholder="E-mail" type="email">'
        self.assertTagEqual(html, expected)

    def test_img(self):
        html = html_tag("img", src="https://placehold.it/10x10", alt="Sample")
        expected = '<img alt="Sample" src="https://placehold.it/10x10">'
        self.assertTagEqual(html, expected)

if __name__ == "__main__":
    unittest.main()