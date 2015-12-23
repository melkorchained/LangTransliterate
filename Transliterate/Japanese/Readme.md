# USAGE:

In order for readability, consider tokenizing (segmenting) the text first and then applying the transliterator.

To tokenize, use the following methods:

from tinysegmenter import TinySegmenter
ts = TinySegmenter()
sent = '<insert text here>'
print(' '.join(ts.tokenize(sent)))

To transliterate, use the following methods:

from hira.py import Japanese
jap = Japanese()
print(jap.jap_to_roman(sent))
