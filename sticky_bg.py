with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make the wrapper sticky
html = html.replace(
    '<div class="photo-bg-wrapper" aria-hidden="true">',
    '<div class="photo-bg-wrapper" aria-hidden="true" style="position: sticky; top: 0; height: 100vh; width: 100%; z-index: 0;">'
)

# Pull the content back up over the sticky background
html = html.replace(
    '<div class="content-relative">',
    '<div class="content-relative" style="margin-top: -100vh; padding-top: 6rem;">'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

import re
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Make the image position right bottom so the girl is always at the bottom right of the screen
css = re.sub(
    r'\.bg-parallax-img\s*\{[^}]*\}',
    '''.bg-parallax-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: right 85%;
    opacity: 0.5;
}''',
    css
)

# Remove the absolute positioning from original CSS
css = re.sub(
    r'\.photo-bg-wrapper\s*\{\s*position:\s*absolute;[^}]*\}',
    '.photo-bg-wrapper { /* position overridden by inline sticky */ }',
    css
)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Sticky background implemented")