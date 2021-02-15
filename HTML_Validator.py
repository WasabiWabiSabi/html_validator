#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    else:
        extracted_html = _extract_tags(html)
        stack = []
        char = "/"
        if len(extracted_html) == 0:
            return False
        else:
            for tag in extracted_html:
                if char not in tag:
                    stack.append(tag)
                else:
                    if len(stack) == 0:
                        return False
                    tag_new = tag.replace("/", "")
                    if stack[-1] == tag_new:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained
    in the input string, stripping out all text not contained
    within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    html_tags = []
    tag = ""
    flag = 0
    for symbol in html:
        if symbol == "<":
            flag = 1
        if flag == 1:
            tag += symbol
        if symbol == ">":
            html_tags.append(tag)
            tag = ""
            flag = 0
    return html_tags
