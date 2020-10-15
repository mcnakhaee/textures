import pytest
from textures.find import find_mentions, find_hashtags,find_numbers,find_urls,find_emails,find_emojis,find_upper


def test_find_mentions():
    assert find_mentions('A brown @fox jumps over the lazy @dog') == ['@fox', '@dog']

def test_find_hashtags():
    assert find_hashtags('A brown #fox jumps over the lazy #dog') == ['#fox', '#dog']

def test_find_numbers():
    assert find_numbers('1 brown fox jumps over 22 lazy dogs') == ['1', '22']

def test_find_emails():
    assert find_emails('A brown fox sent an email to over the lazy dogs lazydog@mail.com') == ['lazydog@mail.com']

def test_find_emojis():
        assert find_emojis('A brown fox jumps over the lazy dog 🐶😒') == ['🐶', '😒']

def test_find_upper():
    assert find_upper('The brown FOX jumps over the lazy DOG') == ['FOX', 'DOG']

