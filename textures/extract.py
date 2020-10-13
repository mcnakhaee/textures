import re

def extract_mentions(text):
    """
     This function extracts and returns all mentions (characters that start with @ sign) found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'[@][^\s#@]+', text)
def extract_hashtags(text):
    """
    This function extracts and returns all hashtags (characters that start with # sign) found in a string variable.
    :param text: a string variable
    :return: a list of characters
    """
    return re.findall(r'[#][^\s#@]+', text)
def extract_urls(text):
    """
     This function extracts and returns all URLs found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'(https?://[^\s]+)', text)
def extract_emails(text):
    """
     This function extracts and returns all emails found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', text)

def extract_all_caps(text):
    """
     This function extracts and returns all caps (all capitals) letters found in a string variable.
     :param text: a string variable
     :return: a list of characters
     """
    return re.findall(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", text)

def extract_emojis(text):
    """
     This function extracts and returns all emojis found in a string variable.
     :param text: a string variable
     :return: a list of characters
     # http://stackoverflow.com/a/13752628/6762004
     """
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.findall(text)