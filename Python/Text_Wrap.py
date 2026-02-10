def wrap(string, max_width):
    ss= textwrap.wrap(string, width=max_width)
    pp='\n'.join(ss)
    return pp
