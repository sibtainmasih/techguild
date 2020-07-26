# Before
def html_tag(tag_name, **attributes):
    """Make an HTML tag from the given tag name and attributes."""
    tag = '<' + tag_name
    for param, value in attributes.items():
        tag += ' ' + param + '="' + value + '"'
    tag += '>'
    return tag


# After Refactoring
def html_tag(tag_name, **attributes):
    """Make an HTML tag from the given tag name and attributes."""
    tag = f'<{tag_name}'
    attrib_list = [f'{param}={value}' for param, value in attributes.items()]
    return f'{tag} {" ".join(attrib_list)}>'
    
if __name__ == "__main__":
    html_tag('table', border="1", bgcolor="red")