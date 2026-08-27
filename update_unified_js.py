with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

import re

# Replace the old Contact BG parallax
old_parallax = re.search(r'\s*// ════════════════════════════════════════\s*// CONTACT BG PARALLAX.*?}\s*', js, flags=re.DOTALL)
if old_parallax:
    new_parallax = """
    // ════════════════════════════════════════
    // UNIFIED BG PARALLAX (Contact + MC Events)
    // ════════════════════════════════════════
    const unifiedBg = document.querySelector(".unified-bg-img");
    if (unifiedBg) {
        gsap.fromTo(unifiedBg, 
            { yPercent: -5 },
            { 
                yPercent: 15,
                ease: "none",
                scrollTrigger: {
                    trigger: ".unified-bg-wrapper",
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                }
            }
        );
    }
"""
    js = js.replace(old_parallax.group(0), new_parallax)
    
    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("JS updated for unified bg parallax")
else:
    print("Could not find old parallax code")