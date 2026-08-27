# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman.
# All rights reserved.
# ==========================================

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. REMOVE the old photo-strip (the 2-photo-in-1-layout that user hates) ──
import re
# Remove photo-strip block
html = re.sub(
    r'\s*<!-- photo-strip: cream \+ pro -->.*?</div>\s*\n',
    '\n',
    html,
    flags=re.DOTALL
)

# ── 2. REDESIGN photo-break: from cheap full-bleed text → magazine split layout ──
old_break = '''
        <!-- ✦ Photo Break — Parallax Outdoor (photo_beach) ✦ -->
        <div class="photo-break" aria-hidden="true">
            <div class="photo-break-img-wrap">
                <img src="assets/images/photo_beach.png" alt="" class="photo-break-img" loading="lazy">
            </div>
            <div class="photo-break-overlay">
                <blockquote class="photo-quote">
                    &ldquo;Setiap project adalah kesempatan<br>untuk menciptakan sesuatu yang berarti.&rdquo;
                </blockquote>
            </div>
        </div>

'''
new_break = '''
        <!-- ✦ Editorial Photo Break — Magazine Split ✦ -->
        <div class="photo-editorial" aria-hidden="true">
            <div class="photo-editorial-text">
                <span class="editorial-label">— rifqah finnisa</span>
                <blockquote class="editorial-quote">
                    &ldquo;Setiap project adalah<br>kesempatan untuk<br>menciptakan sesuatu<br>yang berarti.&rdquo;
                </blockquote>
                <div class="editorial-line"></div>
            </div>
            <div class="photo-editorial-img">
                <img src="assets/images/photo_beach.png" alt="" loading="lazy">
            </div>
        </div>

'''
html = html.replace(old_break, new_break)

# ── 3. ADD photo_cream as a subtle background for contact section ──
old_contact = '        <section class="contact-section alternate-bg">'
new_contact = '        <section class="contact-section alternate-bg" style="position:relative;">'
html = html.replace(old_contact, new_contact)

# Insert photo_cream as background image inside the contact section
old_profile_showcase = '            <div class="profile-showcase reveal">'
new_profile_showcase = '''            <div class="contact-photo-bg" aria-hidden="true">
                <img src="assets/images/photo_cream.png" alt="" class="contact-bg-img" loading="lazy">
            </div>
            <div class="profile-showcase reveal">'''
html = html.replace(old_profile_showcase, new_profile_showcase, 1)

# ── 4. ADD photo_pro as floating pill portrait before footer ──
# Check if already exists
if 'photo-footer-accent' not in html:
    photo_pro_html = '''
        <!-- ✦ Photo Pro — Floating Portrait before footer ✦ -->
        <div class="photo-footer-accent" aria-hidden="true">
            <img src="assets/images/photo_pro.png" alt="" class="photo-footer-img" loading="lazy">
        </div>
'''
    html = html.replace(
        '        <footer class="footer reveal"',
        photo_pro_html + '        <footer class="footer reveal"'
    )

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

print("photo-editorial ok:", "photo-editorial" in c)
print("photo_cream bg ok:", "contact-bg-img" in c)
print("photo_pro pill ok:", "photo-footer-accent" in c)
print("photo-strip removed:", "photo-strip" not in c)