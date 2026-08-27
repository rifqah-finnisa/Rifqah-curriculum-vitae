/*
 * ==========================================
 * AEGIS COGNITIVE RUNTIME PLATFORM
 * PROPRIETARY AND CONFIDENTIAL
 * Copyright (c) 2024-2026 Wahyu Nur Iman.
 * All rights reserved.
 * ==========================================
 */

document.addEventListener("DOMContentLoaded", () => {
    // ── Icons ──
    lucide.createIcons();

    // ════════════════════════════════════════
    // 1. LENIS — Dreamy Smooth Scroll
    // ════════════════════════════════════════
    const lenis = new Lenis({
        duration: 1.5,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        smooth: true,
        smoothTouch: false,
    });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((time) => { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);

    // Refresh ScrollTrigger after fonts load
    window.addEventListener("load", () => ScrollTrigger.refresh());

    // ════════════════════════════════════════
    // 2. CURSOR SPARKLE TRAIL
    // ════════════════════════════════════════
    const sparkleColors = ["#E8C5BE","#C07E72","#F5D6CE","#D4A0A0","#FAEAE6"];
    let lastX = 0, lastY = 0;
    window.addEventListener("mousemove", (e) => {
        if (Math.abs(e.clientX - lastX) < 8 && Math.abs(e.clientY - lastY) < 8) return;
        lastX = e.clientX; lastY = e.clientY;
        const dot = document.createElement("div");
        dot.style.cssText = `
            position:fixed;pointer-events:none;z-index:9998;
            width:${5+Math.random()*6}px;height:${5+Math.random()*6}px;
            border-radius:50%;left:${e.clientX}px;top:${e.clientY}px;
            background:${sparkleColors[Math.floor(Math.random()*sparkleColors.length)]};
            transform:translate(-50%,-50%);opacity:0.85;`;
        document.body.appendChild(dot);
        gsap.to(dot, {
            y: -(20+Math.random()*30), x:(Math.random()-0.5)*20,
            opacity:0, scale:0.3, duration:0.8+Math.random()*0.4,
            ease:"power2.out", onComplete:()=>dot.remove()
        });
    });

    // ════════════════════════════════════════
    // 3. HERO — Cinematic Entrance (page load, NO ScrollTrigger)
    // ════════════════════════════════════════
    const heroTl = gsap.timeline({ defaults:{ ease:"power4.out" } });
    heroTl
        .from(".hero-image",            { scale:1.08, opacity:0, duration:1.8, ease:"power3.out" }, 0)
        .from(".reveal-text:first-of-type", { y:120, opacity:0, duration:1.2 }, 0.2)
        .from(".reveal-text.outline",   { y:80, opacity:0, duration:1.2 }, 0.35)
        .from(".hero-roles",            { y:20, opacity:0, duration:0.8 }, 0.65)
        .from(".hero-bio",              { y:20, opacity:0, duration:0.8 }, 0.75)
        .from(".scroll-indicator",      { y:16, opacity:0, duration:0.7 }, 0.9);

    // Hero parallax only — NO opacity scrub (was causing the stuck issue)
    gsap.to(".hero-image", {
        yPercent: 22, ease:"none",
        scrollTrigger: {
            trigger:".hero", start:"top top", end:"bottom top",
            scrub: 1.5
        }
    });

    // ════════════════════════════════════════
    // 4. PETAL BURST helper
    // ════════════════════════════════════════
    function burstPetals(count=8) {
        for (let i=0; i<count; i++) {
            const p = document.createElement("div");
            p.style.cssText = `
                position:fixed;pointer-events:none;z-index:9000;
                width:${6+Math.random()*8}px;height:${6+Math.random()*8}px;
                border-radius:${Math.random()>0.5?"50%":"50% 0 50% 0"};
                background:${sparkleColors[Math.floor(Math.random()*sparkleColors.length)]};
                left:${10+Math.random()*80}vw;top:${30+Math.random()*40}vh;
                opacity:0.9;transform:rotate(${Math.random()*360}deg);`;
            document.body.appendChild(p);
            gsap.to(p, {
                y:-(80+Math.random()*120), x:(Math.random()-0.5)*80,
                rotation:Math.random()*360, opacity:0,
                duration:1.5+Math.random(), ease:"power2.out",
                delay:Math.random()*0.4, onComplete:()=>p.remove()
            });
        }
    }

    // ════════════════════════════════════════
    // 5. SECTION TITLES — Stagger reveal
    //    toggleActions: play→reverse so it replays scrolling back
    // ════════════════════════════════════════
    document.querySelectorAll(".section-title").forEach(title => {
        const parts = title.innerHTML.split(/(<[^>]+>|\s+)/g);
        let rebuilt = "";
        parts.forEach(p => {
            if (!p || p.startsWith("<") || /^\s+$/.test(p)) { rebuilt += p; }
            else {
                rebuilt += `<span class="word-wrap" style="overflow:hidden;display:inline-block;vertical-align:bottom;"><span class="word" style="display:inline-block;">${p}</span></span>`;
            }
        });
        title.innerHTML = rebuilt;

        const words = title.querySelectorAll(".word");
        gsap.fromTo(words,
            { y:"110%", opacity:0 },
            {
                y:"0%", opacity:1, duration:0.9, ease:"power4.out", stagger:0.07,
                scrollTrigger: {
                    trigger: title,
                    start: "top 82%",
                    end: "top 30%",
                    // KEY FIX: toggleActions play forward, reverse on scroll back
                    toggleActions: "play none none reverse"
                },
                onComplete: () => burstPetals(4)
            }
        );
    });

    // ════════════════════════════════════════
    // 6. TIMELINE ITEMS — KEY FIX: reverse on leave-back
    // ════════════════════════════════════════
    gsap.utils.toArray(".timeline-item").forEach((item) => {
        const meta = item.querySelector(".timeline-meta");
        const content = item.querySelector(".timeline-content");

        gsap.fromTo(meta,
            { x:-50, opacity:0 },
            {
                x:0, opacity:1, duration:0.9, ease:"back.out(1.5)",
                scrollTrigger: {
                    trigger: item,
                    start: "top 84%",
                    end: "top 20%",
                    toggleActions: "play none none reverse"
                }
            }
        );
        gsap.fromTo(content,
            { x:50, opacity:0 },
            {
                x:0, opacity:1, duration:0.9, ease:"back.out(1.5)",
                delay: 0.08,
                scrollTrigger: {
                    trigger: item,
                    start: "top 84%",
                    end: "top 20%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    });

    // ════════════════════════════════════════
    // 7. GALLERY — bounce + reverse
    // ════════════════════════════════════════
    gsap.utils.toArray(".experience-gallery").forEach(gallery => {
        gsap.fromTo(gallery.querySelectorAll("img"),
            { scale:0.88, opacity:0, y:30 },
            {
                scale:1, opacity:1, y:0, duration:0.8,
                ease:"back.out(2)", stagger:0.12,
                scrollTrigger: {
                    trigger: gallery,
                    start: "top 87%",
                    end: "top 30%",
                    toggleActions: "play none none reverse"
                }
            }
        );
    });

    // ════════════════════════════════════════
    // 8. GALLERY HOVER TILT
    // ════════════════════════════════════════
    document.querySelectorAll(".experience-gallery img").forEach(img => {
        img.addEventListener("mousemove", (e) => {
            const rect = img.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            gsap.to(img, { rotationY:x*12, rotationX:-y*12, scale:1.05, duration:0.4, ease:"power2.out", transformPerspective:600 });
        });
        img.addEventListener("mouseleave", () => {
            gsap.to(img, { rotationY:0, rotationX:0, scale:1, duration:0.6, ease:"elastic.out(1,0.5)" });
        });
    });

    // ════════════════════════════════════════
    // 9. PROFILE CARD
    // ════════════════════════════════════════
    gsap.fromTo(".profile-showcase",
        { y:70, opacity:0, scale:0.96 },
        {
            y:0, opacity:1, scale:1, duration:1.3, ease:"power4.out",
            scrollTrigger: {
                trigger: ".profile-showcase",
                start: "top 87%",
                end: "top 40%",
                toggleActions: "play none none reverse"
            }
        }
    );

    // ════════════════════════════════════════
    // 10. CONTACT ITEMS — cascade with reverse
    // ════════════════════════════════════════
    gsap.fromTo(".contact-item",
        { y:30, opacity:0, scale:0.95 },
        {
            y:0, opacity:1, scale:1, duration:0.7, ease:"back.out(1.8)", stagger:0.1,
            scrollTrigger: {
                trigger: ".contact-grid",
                start: "top 86%",
                end: "top 30%",
                toggleActions: "play none none reverse"
            }
        }
    );

    // ════════════════════════════════════════
    // 11. BACKGROUND COLOR SHIFT
    // ════════════════════════════════════════
    [
        { id:"#mc-events", bg:"#F2F0EB" },
        { id:"#work",      bg:"#EAE4DF" },
        { id:"#education-skills", bg:"#F2F0EB" }
    ].forEach(({ id, bg }) => {
        const el = document.querySelector(id);
        if (!el) return;
        ScrollTrigger.create({
            trigger:el, start:"top 55%", end:"bottom 55%",
            onEnter:     () => gsap.to("body", { backgroundColor:bg, duration:1, ease:"power2.inOut" }),
            onEnterBack: () => gsap.to("body", { backgroundColor:bg, duration:1, ease:"power2.inOut" }),
            onLeave:     () => gsap.to("body", { backgroundColor:"#F2F0EB", duration:1 }),
            onLeaveBack: () => gsap.to("body", { backgroundColor:"#F2F0EB", duration:1 }),
        });
    });

    // ════════════════════════════════════════
    // 12. FOOTER — staggered playful reveal
    // ════════════════════════════════════════
    const footerLines = document.querySelectorAll(".footer-line");
    if (footerLines.length) {
        gsap.fromTo(footerLines,
            { y:60, opacity:0 },
            {
                y:0, opacity:1, duration:1.0, ease:"back.out(1.7)", stagger:0.15,
                scrollTrigger: {
                    trigger: ".footer",
                    start: "top 82%",
                    end: "top 40%",
                    toggleActions: "play none none reverse",
                    onEnter: () => burstPetals(12)
                }
            }
        );
        gsap.fromTo(".magnetic-btn",
            { opacity:0, y:20 },
            {
                opacity:1, y:0, duration:0.9, ease:"back.out(1.5)",
                scrollTrigger: {
                    trigger: ".footer",
                    start: "top 78%",
                    end: "top 40%",
                    toggleActions: "play none none reverse"
                },
                delay: 0.5
            }
        );
    }

    // ════════════════════════════════════════
    // 13. MAGNETIC BUTTON + Heart burst on click
    // ════════════════════════════════════════
    const btn = document.querySelector(".magnetic-btn");
    if (btn) {
        const inner = btn.querySelector(".btn-text") || btn;
        btn.addEventListener("mousemove", (e) => {
            const r = btn.getBoundingClientRect();
            const x = e.clientX - r.left - r.width/2;
            const y = e.clientY - r.top - r.height/2;
            gsap.to(btn, { x:x*0.35, y:y*0.35, duration:0.5, ease:"power3.out" });
            gsap.to(inner, { x:x*0.1, y:y*0.1, duration:0.5, ease:"power3.out" });
        });
        btn.addEventListener("mouseleave", () => {
            gsap.to(btn, { x:0, y:0, duration:0.9, ease:"elastic.out(1,0.4)" });
            gsap.to(inner, { x:0, y:0, duration:0.9, ease:"elastic.out(1,0.4)" });
        });
        btn.addEventListener("click", (e) => {
            ["💕","✨","🌸","💗","⭐","🌷","💖"].forEach((emoji, i) => {
                const h = document.createElement("div");
                h.textContent = emoji;
                h.style.cssText = `position:fixed;font-size:${16+Math.random()*14}px;left:${e.clientX}px;top:${e.clientY}px;pointer-events:none;z-index:9999;`;
                document.body.appendChild(h);
                gsap.to(h, {
                    y:-(60+Math.random()*100), x:(Math.random()-0.5)*100,
                    opacity:0, rotation:(Math.random()-0.5)*60,
                    duration:1+Math.random()*0.5, ease:"power2.out",
                    delay:i*0.06, onComplete:()=>h.remove()
                });
            });
        });
    }

    // ════════════════════════════════════════
    // 14. SKILL CATEGORIES — with reverse
    // ════════════════════════════════════════
    gsap.fromTo(".skill-category",
        { y:30, opacity:0 },
        {
            y:0, opacity:1, duration:0.8, ease:"back.out(1.5)", stagger:0.1,
            scrollTrigger: {
                trigger: ".skills-block",
                start: "top 86%",
                end: "top 30%",
                toggleActions: "play none none reverse"
            }
        }
    );

    // ════════════════════════════════════════
    // 15. EDU ITEMS — with reverse
    // ════════════════════════════════════════
    gsap.fromTo(".edu-item",
        { x:-30, opacity:0 },
        {
            x:0, opacity:1, duration:0.8, ease:"back.out(1.5)", stagger:0.15,
            scrollTrigger: {
                trigger: ".education-block",
                start: "top 86%",
                end: "top 30%",
                toggleActions: "play none none reverse"
            }
        }
    );

    // ════════════════════════════════════════
    // PHOTO BREAK — Cinematic Parallax (photo_beach)
    // ════════════════════════════════════════
    const photoBreak = document.querySelector(".photo-break");
    if (photoBreak) {
        const imgWrap = photoBreak.querySelector(".photo-break-img-wrap");

        // Parallax: image moves slower than scroll = depth effect
        gsap.to(imgWrap, {
            yPercent: -20,
            ease: "none",
            scrollTrigger: {
                trigger: photoBreak,
                start: "top bottom",
                end: "bottom top",
                scrub: 1.2
            }
        });

        // Quote fades in from below as you enter the section
        gsap.fromTo(".photo-quote",
            { y: 40, opacity: 0, scale: 0.97 },
            {
                y: 0, opacity: 1, scale: 1,
                duration: 1.2, ease: "power3.out",
                scrollTrigger: {
                    trigger: photoBreak,
                    start: "top 65%",
                    end: "top 20%",
                    toggleActions: "play none none reverse"
                }
            }
        );

        // Subtle zoom on scroll (Ken Burns feel)
        gsap.fromTo(imgWrap.querySelector("img"),
            { scale: 1.08 },
            {
                scale: 1,
                ease: "none",
                scrollTrigger: {
                    trigger: photoBreak,
                    start: "top bottom",
                    end: "bottom top",
                    scrub: 2
                }
            }
        );
    }

    // ════════════════════════════════════════
    // FOOTER ACCENT PHOTO — Float up on enter
    // ════════════════════════════════════════
    const footerPhoto = document.querySelector(".photo-footer-img");
    if (footerPhoto) {
        gsap.fromTo(footerPhoto,
            { y: 60, opacity: 0, scale: 0.94 },
            {
                y: 0, opacity: 1, scale: 1,
                duration: 1.4, ease: "power4.out",
                scrollTrigger: {
                    trigger: ".photo-footer-accent",
                    start: "top 90%",
                    end: "top 50%",
                    toggleActions: "play none none reverse"
                }
            }
        );

        // Gentle float on scroll
        gsap.to(footerPhoto, {
            yPercent: -15,
            ease: "none",
            scrollTrigger: {
                trigger: ".photo-footer-accent",
                start: "top bottom",
                end: "bottom top",
                scrub: 1.5
            }
        });
    }


    // ════════════════════════════════════════
    // BEACH BG PARALLAX (MC Events Section)
    // ════════════════════════════════════════
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
            yPercent: -10,
            ease: "none",
            scrollTrigger: {
                trigger: eduPhoto,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    }

});
