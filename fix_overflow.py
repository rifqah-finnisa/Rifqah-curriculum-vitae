import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(
    r'\.photo-bg-section\s*\{[^}]*\}',
    '''.photo-bg-section {
    background-color: var(--bg-alt);
    position: relative;
    color: var(--text);
}''',
    css
)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Removed overflow: hidden from photo-bg-section")