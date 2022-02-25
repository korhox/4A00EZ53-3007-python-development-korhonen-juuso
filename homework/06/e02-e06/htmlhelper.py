
def generate_html_page(title, content):
    """
    Function will return a valid html5 page as string.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
        {content}
    </body>
</html>"""


html_page = generate_html_page("My title", "<p>Hello</p>")
print(html_page)
