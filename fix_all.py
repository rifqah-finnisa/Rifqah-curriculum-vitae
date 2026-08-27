# Fix 1: Update HTML - replace placeholder management image with silhouette
# Fix 2: Replace footer h2 to always be visible
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the management placeholder image with the silhouette
html = html.replace(
    '<img src="assets/images/placeholder_management.jpg" alt="Ilustrasi Manajemen Proyek">',
    '<img src="assets/images/silhouette_placeholder.jpg" alt="Profil Kosong" style="object-fit:contain; background:#F8F5F2;">'
)

# Fix footer - remove the broken GSAP-targeted h2, make it visible by default with spans for animation
old_footer = """<div class="footer-content">
                <h2 class="reveal-text">MARI <br><span class="copper">BEKERJA SAMA.</span></h2>"""

new_footer = """<div class="footer-content">
                <div class="footer-title">
                    <h2 class="footer-line">Yuk, <em>Kita</em></h2>
                    <h2 class="footer-line footer-big">BEKERJA</h2>
                    <h2 class="footer-line footer-outline">SAMA~ ✨</h2>
                </div>"""
html = html.replace(old_footer, new_footer)

# Fix contact grid - set linkedin to be 5th item properly (no change needed in HTML just CSS)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated")