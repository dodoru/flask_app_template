import random
import string
from datetime import datetime
from flask.json import JSONEncoder


def short_uuid(length=8):
    charset = string.ascii_lowercase + string.digits
    return ''.join([random.choice(charset) for i in range(length)])


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%SZ")
        # return super(CustomJSONEncoder, self).default(obj)
        return JSONEncoder.default(self, obj)
