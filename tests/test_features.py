import pytest
import pandas as pd
from textures.features import extract_features

df = pd.DataFrame({'text':['1 BRown #fox jumps over 22  lazzzy   dog!🐶😒 @lazydog']})
f = extract_features(df)
def test_shape():
    assert f.shape[1] == 34