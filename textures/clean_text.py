import re
import string

#To Do: remove just mentions not emails
def remove_mentions(text):
    """
      Removes all mentions (characters that start with @ sign) from a string input.
     :param text: a string variable
     :return: a list of characters
     """
    return ' '.join(re.sub(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', ' ', text).split())

def remove_hashtags(text):

    """
     Removes all hashtags (characters that start with # sign) from a string input.
     :param text: a string variable
     :return: a list of characters
     """
    return ' '.join(re.sub(r'[#][^\s#@]+', ' ', text).split())


def remove_urls(text):
    """
     This function removes all URLs found a string input.
     :param text: a string variable
     :return: a list of characters
     """
    pass


def remove_emails(text):
    """
     removes all caps (all capitals) letters from a string input.
     :param text: a string variable
     :return: a list of characters
     """
    return re.sub(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', ' ', text)


def remove_all_caps(text):
    """
     removes all caps (all capitals) letters from a string input.
     :param text: a string variable
     :return: a list of characters
     """
    return re.sub(r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
                  ' ', text)

def remove_emojis(text):
    """
     removes all emojis from a string input.
     :param text: a string variable
     :return: a list of characters
     """
    # http://stackoverflow.com/a/13752628/6762004
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', text)

def remove_hashtag_symbols(text):
    """
    Remove all # symbols from a string input.
    :param text: a string variable
    :return:
    """
    return text.replace('#','')

def remove_at_symbols(text):
    """
    Remove all @ symbols from a string input.
    :param text: a string variable
    :return:
    """
    return text.replace('@', '')

def remove_punctuations(text):
    """
    Remove all punctuations from a string input.
    :param text:a string variable
    :return:
    """
    return text.translate(str.maketrans('', '', string.punctuation))