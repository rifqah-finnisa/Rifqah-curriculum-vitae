with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

anim_js = """
    // ════════════════════════════════════════
    // EDUCATION PHOTO FADE
    // ════════════════════════════════════════
    const eduPhoto = document.querySelector(".education-photo");
    if (eduPhoto) {
        gsap.fromTo(eduPhoto,
            { y: 60, opacity: 0, scale: 0.94 },
            {
                y: 0, opacity: 1, scale: 1,
                duration: 1.4, ease: "power4.out",
                scrollTrigger: {
                    trigger: eduPhoto,
                    start: "top 85%",
                    toggleActions: "play none none reverse"
                }
            }
        );
        // Parallax
        gsap.to(eduPhoto.querySelector(".photo-pill-wrapper"), {
            yPercent: -15,
            ease: "none",
            scrollTrigger: {
                trigger: eduPhoto,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    }
"""

js = js.replace("\n});\n", anim_js + "\n});\n")

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
print("JS for education photo animation added back")