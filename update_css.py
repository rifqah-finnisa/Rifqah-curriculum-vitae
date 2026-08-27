import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Change --font-display
css = re.sub(r"--font-display:.*?;\n", "--font-display: 'Playfair Display', serif;\n", css)

# Make background colors a bit softer/more blush
css = re.sub(r"--color-bg: #faf8f5;", "--color-bg: #fdfaf6;", css)
css = re.sub(r"--color-bg-alt: #fcf8f7;", "--color-bg-alt: #fbf5f3;", css)
css = re.sub(r"--color-accent: #c48c7e;", "--color-accent: #d29b8c;", css)
css = re.sub(r"--color-text-primary: #2d2a29;", "--color-text-primary: #4a3e3c;", css)

# Fix outline class for delicate look
css = css.replace(".outline {\n    color: transparent;\n    -webkit-text-stroke: 1.5px var(--color-text-primary);\n}", ".outline {\n    color: transparent;\n    -webkit-text-stroke: 1px var(--color-accent);\n    font-style: italic;\n}")

# Fix section title
css = css.replace(".section-title {", ".section-title {\n    font-family: var(--font-display);\n    letter-spacing: -0.01em;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Done")