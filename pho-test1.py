#!/usr/local/bin/python
# coding:utf8
import re
from trans_dict import trans_bng
from literal_dict import literal
from literal_dict import modific
from pyavrophonetic import avro
from default_dict import trans_words

org_word="cellglÃ²"
if re.match('^[a-zA-Z0-9]*$', org_word):
    print('TL-NW-ALNUM')
else:
    print('TL-NW-ALNUM-SP')

word = "piur"
for key in modific:
    if key in word:
        print(key, "->", modific[key])
        word=word.replace(key, modific[key])
print(word)
print(avro.parse(word))
