# -*- coding: utf-8 -*-
import pytest

from mimesis.choice import Choice


@pytest.fixture
def choice():
    return Choice()


@pytest.mark.parametrize(
    'items, number', [
        (['a', 'b', 'c', 'd', 'e', 'f', 'g'], 4),
        (['a', 'b', 'c', 'd', 'e', 'f', 'g'], 5),
        (['a', 'b', 'c', 'd', 'e', 'f', 'g'], 1),
    ])
def test_choice(choice, items, number):
    result = choice(items=items, number=number)
    assert len(result) == number


@pytest.mark.parametrize('items', ['a', 'b', 'c', 'd', 'e'])
def test_choice_unique(choice, items):
    result = choice(items=items, number=4, unique=True)
    assert len(result) == len(set(result))


@pytest.mark.parametrize('items', ['a', 'b', 'c', 'd', 'e'])
def test_choice_one_element(choice, items):
    result = choice(items=items)
    assert isinstance(result, str)
