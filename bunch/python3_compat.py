''' python 3 compatibility function '''
import six

# u('string') replaces the forwards-incompatible u'string'
if six.PY3:
    u = lambda x : x
else:
    import codecs
    def u(string):
       ''' return a unicode string in python 2 '''
       return codecs.unicode_escape_decode(string)[0]


