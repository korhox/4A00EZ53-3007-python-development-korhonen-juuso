
def generate_html_page(title, content):
    """
    Function will return a valid html5 page as string.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <link rel="stylesheet" href="https://cdn.bittivirta.fi/packages/bootstrap/v5.1.3/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.bittivirta.fi/css/fonts/font-package.css">
        <style>
            body {{
                font-family:'Ubuntu';
            }}
            code {{
                font-family:'Fira Code Nerd';
            }}
        </style>
    </head>
    <body>
        {content}
    </body>
</html>"""
