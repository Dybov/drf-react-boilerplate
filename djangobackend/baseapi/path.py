import re

from django.urls import path

KEYWORD_PATTERN = '\(\?P\<(?P<name>[^>]+)\>(?P<value>.*)\)'


class ReactPath(object):

    _react_nodes = []

    def __new__(self, *args, **kwargs):
        resolver = path(*args, **kwargs)
        ReactPath._react_nodes.append(resolver)
        return resolver

    @staticmethod
    def get_react_nodes():
        return ReactPath._react_nodes


def recursive_sub(pattern, func, string):
    """ Replace the the pattern string while it can"""
    new_string = re.sub(pattern, func, string)
    if string != new_string:
        return recursive_sub(pattern, func, new_string)
    return new_string


def to_path_repl(matchobj):
    """Replace regex keyword param to the react-router path"""
    name = matchobj.group('name')
    value = matchobj.group('value')
    if name and value:
        return ':%s(%s)' % (name, value)
    else:
        return ''


def transform_regex_to_react_router(regex_pattern):
    if regex_pattern.startswith('^'):
        regex_pattern = regex_pattern[1:]
    if regex_pattern.endswith('$'):
        regex_pattern = regex_pattern[:-1]
    if regex_pattern.endswith('/'):
        # regex_pattern = regex_pattern[:-1]
        regex_pattern += ''

    regex_pattern = recursive_sub(KEYWORD_PATTERN, to_path_repl, regex_pattern)
    regex_pattern = recursive_sub(r'\\', '', regex_pattern)

    return regex_pattern


def iterate_urls(
        urls, nodes, output_dict={},
        entry_point='/', parent_react=False, prefix=''):
    for url in urls:
        _has_urls = hasattr(url, 'url_patterns')

        if not parent_react and url not in nodes and not _has_urls:
            continue
        regex_pattern = entry_point + transform_regex_to_react_router(
            url.pattern.regex.pattern)
        if _has_urls:
            if not parent_react and url not in nodes:
                continue

            next_prefix = prefix
            if next_prefix:
                next_prefix += ':'

            if hasattr(url, "namespace") and url.namespace:
                next_prefix += url.namespace + ':'
            if (
                hasattr(url, "module") and
                hasattr(url.module, 'app_name') and
                url.module.app_name
            ):
                next_prefix += url.module.app_name

            iterate_urls(
                url.url_patterns,
                nodes,
                output_dict,
                entry_point=regex_pattern,
                parent_react=True,
                prefix=next_prefix)
            continue

        name = prefix + url.name

        output_dict[name] = regex_pattern
    return output_dict


def build_react_pathes():
    from conf.urls import urlpatterns
    nodes = ReactPath.get_react_nodes()
    output_dict = {}
    return iterate_urls(urlpatterns, nodes, output_dict)
