import json
from base64 import b64decode

from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseForbidden


def parse_basic_auth(auth_header):
    if auth_header.startswith('Basic '):
        base = auth_header[len('Basic '):]
        decoded = b64decode(base).decode('utf8')
        parts = decoded.split(':')
        user = parts.pop()
        password = ':'.join(parts)
        return user, password
    raise ValueError('Could not parse credentials')


def getvars(request):

    auth = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        username, password = parse_basic_auth(auth)
    except ValueError:
        return HttpResponseForbidden(json.dumps({}))

    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseForbidden(json.dumps({}))

    return HttpResponse(
        json.dumps({i.name: i.value for i in user.var_set.all()}),
        content_type="application/json")

    return HttpResponseForbidden(json.dumps({}))
