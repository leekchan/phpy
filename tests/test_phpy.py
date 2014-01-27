# encoding: utf-8
import os.path
import pytest
from phpy import PHP


test_php_path = os.path.join(os.path.dirname(__file__), 'test.php')


@pytest.mark.parametrize(('foo', 'bar', 'baz'), [
    (1, 2, 3),
    (0.0, 1.1, 2.2),
    ('foo', 'bar', 'baz'),
])
def test_get_dict(foo, bar, baz):
    php = PHP(test_php_path)
    assert (
        php.get_dict('mapping', [foo, bar, baz]) ==
        dict(foo=foo, bar=bar, baz=baz)
    )
