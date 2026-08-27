with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   EDUCATION PHOTO (Pill Shape)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.education-photo {
    width: 100%;
    height: 100%;
}

.photo-pill-wrapper {
    position: relative;
    width: clamp(220px, 28vw, 360px);
    height: clamp(320px, 38vw, 480px);
    border-radius: 200px 200px 0 0;
    box-shadow: 0 20px 50px rgba(192,126,114,0.15);
    mask-image: linear-gradient(to top, transparent 0%, black 15%, black 100%);
    -webkit-mask-image: linear-gradient(to top, transparent 0%, black 15%, black 100%);
    will-change: transform;
    transition: transform 0.8s cubic-bezier(0.25,1,0.5,1);
    margin: 0 auto;
}

.edu-photo-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 15%;
    border-radius: 200px 200px 0 0;
    filter: brightness(0.96) saturate(0.9);
}

.photo-pill-wrapper::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 200px 200px 0 0;
    border: 2px solid transparent;
    background: linear-gradient(to bottom, var(--accent-lt), transparent) border-box;
    -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: destination-out;
    mask-composite: exclude;
    pointer-events: none;
    z-index: 2;
}

.photo-pill-wrapper:hover {
    transform: translateY(-10px) scale(1.02);
}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SKILLS SECTION (Full Width)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.skills-section {
    padding: 6rem 8%;
    background: var(--bg-alt);
}
.skills-section .skills-block {
    max-width: 1200px;
    margin: 0 auto;
}
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
}

/* Mobile Adjustments for Education Photo */
@media (max-width: 768px) {
    .education-photo {
        margin-top: 1rem;
        margin-bottom: 3rem;
    }
    .photo-pill-wrapper {
        width: clamp(200px, 60vw, 280px);
        height: clamp(280px, 80vw, 380px);
    }
}
"""

css = css.replace('/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n   SMOOTHNESS', new_css + '\n/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n   SMOOTHNESS')

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("CSS for education photo and skills section added back")