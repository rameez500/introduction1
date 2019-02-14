from IPython.display import HTML

def View2(df,sen):
    css = """<style>
    table { border-collapse: collapse; border: 3px solid #eee; }
    table tr th:first-child { background-color: #eeeeee; color: #333; font-weight: bold }
    table thead th { background-color: #eee; color: #000; }
    tr, th, td { border: 1px solid #ccc; border-width: 1px 0 0 1px; border-collapse: collapse;
    padding: 4px; font-family: monospace; font-size: 12px }</style>
    """
    s  = 'var randomnumber = Math.floor((Math.random()*100)+1);'
    s  = '<script type="text/Javascript">'
    s += 'var win = window.open("","_blank", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top="+(screen.height-400)+", left="+(screen.width-840));'
    s += 'win.document.body.innerHTML = \'' + (df.to_html() + css).replace("\n",'\\') + '\';'
    # s += 'win.document.title = "Table" ';
    s += 'win.document.title = \'' + sen + '\';'
    s += '</script>'
    return(HTML(s+css))

