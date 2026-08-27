with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

# We need to restructure the education and skills section.
# Let's extract the education block and skills block.
edu_match = re.search(r'(<div class="education-block reveal">.*?</p>\s*</div>\s*</div>)', html, flags=re.DOTALL)
skills_match = re.search(r'(<div class="skills-block reveal">.*?</section>)', html, flags=re.DOTALL)

if edu_match and skills_match:
    edu_html = edu_match.group(1)
    skills_html = skills_match.group(1)
    
    # Remove old grid-section
    html = re.sub(r'\s*<section class="grid-section" id="education-skills">.*?</section>', '', html, flags=re.DOTALL)
    
    new_html = """
        <section class="grid-section" id="education-skills" style="align-items: center;">
            <div class="education-photo reveal" aria-hidden="true" style="display:flex; justify-content:center; align-items:center;">
                <div class="photo-pill-wrapper" style="margin-top: -20px;">
                    <img src="assets/images/photo_pro.png" alt="" class="edu-photo-img" loading="lazy">
                </div>
            </div>
            
            """ + edu_html + """
        </section>

        <section class="skills-section" id="skills">
            """ + skills_html + """
"""
    
    # Insert it after the work section
    html = html.replace('</section>\n\n        <!-- FOOTER -->', '</section>\n' + new_html + '\n        <!-- FOOTER -->')
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML restructured for photo on left, education on right")
else:
    print("Failed to find education or skills block")