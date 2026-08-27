with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# ── FIX 1: Contact grid — force 5 columns on desktop ───────────────────
old_grid = """.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 2rem;
    max-width: 960px;
    margin: 0 auto;
}"""
new_grid = """.contact-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);   /* always 5 in a row */
    gap: 2rem;
    max-width: 960px;
    margin: 0 auto;
}
@media (max-width: 780px) {
    .contact-grid { grid-template-columns: repeat(2, 1fr); }
}"""
css = css.replace(old_grid, new_grid)

# ── FIX 2: Footer title — big, visible, playful ───────────────────────
footer_title_css = """
/* ─── Footer Title — Playful & Always Visible ─── */
.footer-title {
    margin-bottom: 2.5rem;
    text-align: center;
}

.footer-line {
    font-family: var(--ff-head);
    font-weight: 700;
    line-height: 1.0;
    display: block;
    letter-spacing: -0.02em;
    text-transform: uppercase;
    color: var(--text);
}

.footer-line em {
    font-family: var(--ff-serif);
    font-style: italic;
    font-weight: 400;
    color: var(--accent);
    font-size: 0.9em;
    text-transform: none;
}

.footer-line:first-child {
    font-size: clamp(1.6rem, 4vw, 3.5rem);
    font-family: var(--ff-serif);
    font-style: italic;
    font-weight: 400;
    text-transform: none;
    color: var(--text-mid);
    letter-spacing: 0.02em;
    margin-bottom: 0.3rem;
}

.footer-big {
    font-size: clamp(3.5rem, 9vw, 8rem);
    -webkit-text-stroke: 0;
    color: var(--text);
    margin-bottom: 0.1rem;
}

.footer-outline {
    font-size: clamp(2rem, 5.5vw, 5rem);
    color: transparent;
    -webkit-text-stroke: 1.5px var(--accent);
    font-family: var(--ff-serif);
    font-style: italic;
    font-weight: 400;
    text-transform: none;
    letter-spacing: 0.02em;
}

/* ─── Floating petal particles for feminine scroll ─── */
.petal {
    position: fixed;
    pointer-events: none;
    z-index: 9999;
    width: 10px;
    height: 10px;
    border-radius: 50% 0 50% 0;
    opacity: 0;
    transform: rotate(45deg);
}

/* ─── Cursor sparkle dot ─── */
.cursor-sparkle {
    position: fixed;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    background: var(--accent-lt);
    transform: translate(-50%, -50%);
    mix-blend-mode: multiply;
    opacity: 0;
    transition: opacity 0.1s;
}
"""

# Append to end of CSS
css = css + footer_title_css

# ── FIX 3: Fix old footer-content h2 styles that may conflict ─────────
# Remove any old .footer-content h2 that would hide text
css = css.replace(
    ".footer-content h2 {",
    ".footer-content-h2-old {"   # neutralize
)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated")