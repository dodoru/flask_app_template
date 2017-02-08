# -*- coding:utf-8 -*-


class UnauthorizedError(Exception):
    def __init__(self, user_id=None, tips=None):
        self.code = 401
        self.user_id = None
        if tips is None:
            tips = u'用户(id:{})尚未授权,请申请试用'.format(user_id)
        self.tips = tips


class ConflictError(Exception):
    def __init__(self, **kwargs):
        self.code = 409
        if kwargs:
            self.tips = '\n'.join('{} : {} {}'.format(key, type(value), value) for key, value in kwargs.items())
        else:
            self.tips = u''
