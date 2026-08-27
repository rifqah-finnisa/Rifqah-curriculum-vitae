with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the broken comment block with a clean commented out version
bad_block = """    /* const beachBg = document.querySelector(".bg-parallax-img");
    if (beachBg) {
        gsap.to(beachBg, {
            yPercent: 20,
            ease: "none",
            scrollTrigger: {
                trigger: ".photo-bg-section",
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
 */
        });
    }"""

good_block = """    /* 
    const beachBg = document.querySelector(".bg-parallax-img");
    if (beachBg) {
        gsap.to(beachBg, {
            yPercent: 20,
            ease: "none",
            scrollTrigger: {
                trigger: ".photo-bg-section",
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    }
    */"""

js = js.replace(bad_block, good_block)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Fixed JS syntax error")