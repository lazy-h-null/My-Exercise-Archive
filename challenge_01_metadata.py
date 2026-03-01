html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

page_title = "Yoori's Awesome Portfolio"
page_lang = "ko"
html = html.replace("My Page", page_title)
html = html.replace('lang="en"', f'lang="{page_lang}"')
print(html)