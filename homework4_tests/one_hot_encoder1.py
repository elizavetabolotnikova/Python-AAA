import unittest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestOneHotEncoder(unittest.TestCase):
    def test_fit_transform_one_word(self):
        result = fit_transform('hello')
        expected = [('hello', [1])]
        self.assertEqual(result, expected)

    def test_fit_transform(self):
        result = fit_transform('hello', 'world', 'hello', '!', 'world')
        expected = [('hello', [0, 0, 1]),
                    ('world', [0, 1, 0]),
                    ('hello', [0, 0, 1]),
                    ('!', [1, 0, 0]),
                    ('world', [0, 1, 0])]
        self.assertEqual(result, expected)

    def test_fit_transform_list(self):
        result = fit_transform(['hello', 'world', 'hello', '!', 'world'])
        expected = [('hello', [0, 0, 1]),
                    ('world', [0, 1, 0]),
                    ('hello', [0, 0, 1]),
                    ('!', [1, 0, 0]),
                    ('world', [0, 1, 0])]
        self.assertEqual(result, expected)

    def test_fit_transform_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
