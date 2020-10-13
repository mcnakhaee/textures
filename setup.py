from setuptools import setup
import setuptools
setup(name='textures',
      version='0.1.3',
      url="https://github.com/mcnakhaee/textfeatures",
      description="A python package to extract features from text data",
      long_description=open('DESCRIPTION.rst').read(),
      author='Muhammad Chenariyan Nakhaee',
      author_emai='mcnakhaee@gmail.com',
      packages = ['textfeatures'],
      install_requires=['pandas', 'spacy','pyenchant','textblob','nltk','langdetect','textstat','pyenchant'],
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      )
