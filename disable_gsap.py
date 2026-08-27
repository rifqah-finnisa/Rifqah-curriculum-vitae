with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

import re

# Find the beachBg gsap animation and comment it out
js = re.sub(
    r'(const beachBg = document\.querySelector\("\.bg-parallax-img"\);\s*if \(beachBg\) \{.*?\}\n)',
    r'/* \1 */\n',
    js,
    flags=re.DOTALL
)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Disabled GSAP for sticky beach bg")