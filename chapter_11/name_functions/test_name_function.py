"""A slew of tests for name_function.py. For use with pytest."""

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """Do names like Wolfgang Amadeus Mozart work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', middle='amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'