__author__ = 'vladimir'

import urllib2
import base64

def test(username, password):
    request = urllib2.Request("http://127.0.0.1:8001/api/test/")
    # You need the replace to handle encodestring adding a trailing newline
    # (https://docs.python.org/2/library/base64.html#base64.encodestring)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    response = result.read()
    return response


def OrderHandler(request, order_form, order):
    pass
    print('User {} made order!'.format(request.user))
