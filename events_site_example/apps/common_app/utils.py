# -*- coding: utf-8 -*-


def add_model_prefix(prefix, to):
    """Adds prefix to value in Django style

    @type prefix: str
    @type to: str

    @rtype: str

    """
    if prefix:
        return '%s__%s' % (prefix, to)
    else:
        return to