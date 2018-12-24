import unittest

import imbea

class TestIMBEA(unittest.TestCase):

    def test_article_example(self):
        G = [
            ('u1', 'v1'),
            ('u1', 'v2'),
            ('u1', 'v3'),

            ('u2', 'v1'),
            ('u2', 'v2'),
            ('u2', 'v3'),

            ('u3', 'v1'),
            ('u3', 'v4'),

            ('u4', 'v2'),
            ('u4', 'v5'),

            ('u5', 'v1'),
            ('u5', 'v4'),

            ('u6', 'v1'),
            ('u6', 'v2'),
            ('u6', 'v5'),

            ('u7', 'v1'),
            ('u7', 'v3'),

            ('u8', 'v2'),
            ('u8', 'v3'),
            ('u8', 'v4')
        ]

        for i, (U, V) in enumerate(imbea.biclique_find(G)):
            print('\nLargest biclique #%d:' % i)
            print('U: %s' % str(U))
            print('V: %s' % str(V))


if __name__ == '__main__':
    unittest.main()
