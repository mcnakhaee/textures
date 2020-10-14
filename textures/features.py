import pandas as pd
import spacy
import re
from textblob import TextBlob
import enchant
import string
from textfeatures.extract import *
from langdetect import detect
import textstat

def extract_features(df, text_col='text',
                     use_spacy_features=True,
                     use_emoji_features=True,
                     use_misspelling_features=True,
                     n_hashtags=True,
                     n_unique_hashtags=True,
                     n_mentions=True,
                     n_unique_mentions=True,
                     n_tokens=True,
                     n_unique_tokens=True,
                     n_words=True,
                     n_unique_words=True,
                     n_stopwords = True,
                     n_characters=True,
                     n_unique_characters=True,
                     n_unique_urls=True,
                     n_upper=True,
                     n_lower=True,
                     n_numbers = True,
                     n_puncts=True,
                     n_exclaims=True,
                     n_extraspace=True,
                     n_all_cap=True,
                     detect_lang=True,
                     readability_score=True
                     ):
    """

    :param df:
    :param text_col:
    :param use_spacy_features:
    :param use_emoji_features:
    :param use_misspelling_features:
    :param n_hashtags:
    :param n_unique_hashtags:
    :param n_mentions:
    :param n_unique_mentions:
    :param n_tokens:
    :param n_unique_tokens:
    :param n_words:
    :param n_unique_words:
    :param n_characters:
    :param n_unique_characters:
    :param n_unique_urls:
    :param n_upper:
    :param n_lower:
    :param n_numbers:
    :param n_puncts:
    :param n_exclaims:
    :param n_extraspace:
    :param n_all_cap:
    :param detect_lang:
    :param readability_score:
    :return:
    """
    if use_emoji_features:
        df['n_emojis'] = df[text_col].apply(lambda x: len(extract_emojis(x)))
    if use_spacy_features:
        nlp = spacy.load('en_core_web_sm')
        df['nlp'] = df[text_col].apply(lambda x: nlp(x, disable=['tagger', 'parser']))
        df['n_entities'] = df['nlp'].apply(lambda x: len([ent for ent in x.ents]))
        df['tokens'] = df['nlp'].apply(lambda x: [token.text for token in x])
        df['n_stopwords'] = df['nlp'].apply(lambda x: sum([token.is_stop for token in x]))
        df['n_tokens'] = df['tokens'].apply(lambda x: len(x))
        df['n_unique_tokens'] = df['tokens'].apply(lambda x: len(set(x)))
    first_person_pronouns = ["i", "me", "myself", "my", "mine", "this"]
    first_personp_pronouns = ["we", "us", "our", "ours", "these"]
    second_person_pronouns = ["you", "yours", "your", "yourself"]
    third_person_pronouns = ["he", "she", "it", "its", "his", "hers"]
    third_personp_pronouns = ["they", "them", "theirs", "their", "they're", "their's", "those", "that"]
    to_be_verbs = ["am", "is", "are", "was", "were", "being",
                   "been", "be", "were", "be"]
    prepositions = ["about", "below", "excepting", "off", "toward", "above", "beneath",
                    "on", "under", "across", "from", "onto", "underneath", "after", "between",
                    "in", "out", "until", "against", "beyond", "outside", "up", "along", "but",
                    "inside", "over", "upon", "among", "by", "past", "around", "concerning",
                    "regarding", "with", "at", "despite", "into", "since", "within", "down",
                    "like", "through", "without", "before", "during", "near", "throughout",
                    "behind", "except", "of", "to", "for"]
    df['textblob'] = df[text_col].apply(lambda x: TextBlob(x))
    df['textblobwords'] = df['textblob'].apply(lambda x: x.words)
    df['n_words'] = df['textblobwords'].apply(lambda x: len(x))
    df['n_unique_words'] = df['textblobwords'].apply(lambda x: len(set(x)))
    df['n_sentences'] = df['textblob'].apply(lambda x: len(x.sentences))
    if use_misspelling_features:
        dict = enchant.Dict("en_US")
        df['n_misspelled_words'] = df['textblobwords'].apply(
            lambda x: len([word for word in x if dict.check(word) == False]))
    df['first_personp'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in first_personp_pronouns]))
    df['first_personp'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in first_personp_pronouns]))
    df['second_person_pronouns'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in second_person_pronouns]))
    df['third_person'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in third_person_pronouns]))
    df['third_personp'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in third_personp_pronouns]))
    df['n_to_be'] = df['textblobwords'].apply(lambda x: len([word for word in x if word.lower() in to_be_verbs]))
    df['n_prepositions'] = df['textblobwords'].apply(
        lambda x: len([word for word in x if word.lower() in prepositions]))
    df['polarity'] = df['textblob'].apply(lambda x: x.sentiment.polarity)
    df['subjectivity'] = df['textblob'].apply(lambda x: x.sentiment.subjectivity)
    if n_hashtags == True:
        df['n_hashtags'] = df[text_col].apply(lambda x: len(extract_hashtags(x)))
    if n_unique_hashtags == True:
        df['n_unique_hashtags'] = df[text_col].apply(lambda x: len(set(extract_hashtags(x))))
    if n_mentions == True:
        df['n_mentions'] = df[text_col].apply(lambda x: len(extract_mentions(x)))
    if n_unique_mentions == True:
        df['n_unique_mentions'] = df[text_col].apply(lambda x: len(set(extract_mentions(x))))
    if n_characters:
        df['n_characters'] = df[text_col].apply(lambda x: len(x))
    if n_unique_characters:
        df['n_unique_characters'] = df[text_col].apply(lambda x: len(set([char for char in x])))
    if n_unique_urls:
        df['n_unique_urls'] = df[text_col].apply(lambda x: len(re.findall(r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)', x)))
    if n_upper:
        df['n_upper'] = df[text_col].apply(lambda x: len(re.findall(r'[A-Z]', x)))
    if n_lower:
        df['n_lower'] = df[text_col].apply(lambda x: len(re.findall(r'[a-z]', x)))
    if n_numbers:
        df['n_numbers'] = df[text_col].apply(lambda x: len(re.findall(r'\d+', x)))
    if n_puncts:
        df['n_puncts'] = df[text_col].apply(lambda x: len([c for c in x if c not in string.punctuation]))
    if n_exclaims:
        df['n_exclaims'] = df[text_col].apply(lambda x: len(re.findall(r'[!]', x)))
    if n_extraspace:
        df['n_extraspace'] = df[text_col].apply(lambda x: len(re.findall('  +', x)))
    if n_all_cap:
        df['n_all_cap'] = df[text_col].apply(lambda x: len(re.findall(
            r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", x)))
    if detect_lang:
        df['language'] = df[text_col].apply(lambda x: detect(x))
    if readability_score:
        df['readability_score'] = df[text_col].apply(lambda x: textstat.flesch_reading_ease(x))
    df = df.drop(['nlp', 'tokens', 'textblob', 'textblobwords' ], axis=1)
    return df
