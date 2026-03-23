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

stylesheet = "main.min.css"
script_file = "bundle.js"

start_locate = html.find("styles.css")
end_locate = start_locate + len("styles.css")
html = html[:start_locate] + stylesheet + html[end_locate:]

start_locate = html.index("app.js")
end_locate = start_locate + len("app.js")
html = html[:start_locate] + script_file + html[end_locate:]

print(html)

# Advanced Extension
# head_end = html.find("</head>")
# start_locate = html.find("app.js", head_end)
