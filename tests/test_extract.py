import pytest
from textures.extract import extract_mentions, extract_hashtags,extract_numbers,extract_urls,extract_emails,extract_emojis,extract_upper


def test_extract_mentions():
    assert extract_mentions('A brown @fox jumps over the lazy @dog') == ['@fox', '@dog']

def test_extract_hashtags():
    assert extract_hashtags('A brown #fox jumps over the lazy #dog') == ['#fox', '#dog']

def test_extract_numbers():
    assert extract_numbers('1 brown fox jumps over 22 lazy dogs') == ['1', '22']

def test_extract_emails():
    assert extract_emails('A brown fox sent an email to over the lazy dogs lazydog@mail.com') == ['lazydog@mail.com']

def test_extract_emojis():
        assert extract_emojis('A brown fox jumps over the lazy dog 🐶😒') == ['🐶', '😒']

def test_extract_upper():
    assert extract_upper('The brown FOX jumps over the lazy DOG') == ['FOX', 'DOG']

