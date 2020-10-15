import re

def find_mentions(text):
    """
     This function extracts and returns all mentions (characters that start with @ sign) found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'[@][^\s#@]+', text)
def find_hashtags(text):
    """
    This function extracts and returns all hashtags (characters that start with # sign) found in a string variable.
    :param text: a string variable
    :return: a list of characters
    """
    return re.findall(r'[#][^\s#@]+', text)
def find_urls(text):
    """
     This function extracts and returns all URLs found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))', text)
def find_emails(text):
    """
     This function extracts and returns all emails found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', text)

def find_upper(text):
    """
     This function extracts and returns all caps (all capitals) letters found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", text)
def find_lower(text):
    """
     This function extracts and returns lower case words found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'[a-z]+',text)

def find_title(text):
    """
     This function extracts and returns title case words found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'\b[A-Z][a-z]+', text)

def find_emojis(text):
    """
     This function extracts and returns all emojis found in a string variable.
     :param text: a string variable
     :return: a list of characters
     # http://stackoverflow.com/a/13752628/6762004
     """
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.findall(text)

def find_numbers(text):
    """
     This function extracts and returns all numbers found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """

    return re.findall(r'\d+', text)