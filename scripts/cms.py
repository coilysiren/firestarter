def build_html (path):
    '''
    input: path_name[.md|.html]
    html: <some html></some html>
    '''
    # try for markdown
    try:
        with open('paths/'+path+'.md', 'r') as md_data:
            text = md_data.read()
        # create html
        import markdown
        md = markdown.Markdown()
        return md.convert(text)
    except IOError: pass
    # try for html
    try:
        with open('paths/'+path+'.html', 'r') as html_data:
            text = html_data.read()
        return text
    # if neither? fail
    except IOError: return 'something broke???'
