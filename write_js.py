script = r"""/*
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

    // ════════════════════════════════════════
    // 2. CURSOR SPARKLE TRAIL — Feminine Touch
    // ════════════════════════════════════════
    const sparkleColors = ["#E8C5BE","#C07E72","#F5D6CE","#D4A0A0","#FAEAE6"];
    let lastX = 0, lastY = 0;

    window.addEventListener("mousemove", (e) => {
        const dx = e.clientX - lastX;
        const dy = e.clientY - lastY;
        if (Math.abs(dx) < 8 && Math.abs(dy) < 8) return;
        lastX = e.clientX; lastY = e.clientY;

        const dot = document.createElement("div");
        dot.style.cssText = `
            position:fixed; pointer-events:none; z-index:9998;
            width:${5+Math.random()*6}px; height:${5+Math.random()*6}px;
            border-radius:50%; left:${e.clientX}px; top:${e.clientY}px;
            background:${sparkleColors[Math.floor(Math.random()*sparkleColors.length)]};
            transform:translate(-50%,-50%); opacity:0.85;
        `;
        document.body.appendChild(dot);
        gsap.to(dot, {
            y: -(20 + Math.random()*30),
            x: (Math.random()-0.5)*20,
            opacity: 0,
            scale: 0.3,
            duration: 0.8 + Math.random()*0.4,
            ease: "power2.out",
            onComplete: () => dot.remove()
        });
    });

    // ════════════════════════════════════════
    // 3. HERO — Cinematic Entrance
    // ════════════════════════════════════════
    const heroTl = gsap.timeline({ defaults: { ease: "power4.out" } });
    heroTl
        .from(".hero-image", { scale:1.08, opacity:0, duration:1.8, ease:"power3.out" }, 0)
        .from(".reveal-text:first-of-type", { y:120, opacity:0, duration:1.2 }, 0.2)
        .from(".reveal-text.outline", { y:80, opacity:0, duration:1.2 }, 0.35)
        .from(".hero-roles", { y:20, opacity:0, duration:0.8 }, 0.65)
        .from(".hero-bio", { y:20, opacity:0, duration:0.8 }, 0.75)
        .from(".scroll-indicator", { y:16, opacity:0, duration:0.7 }, 0.9);

    // Hero parallax
    gsap.to(".hero-image", {
        yPercent: 22, ease:"none",
        scrollTrigger: { trigger:".hero", start:"top top", end:"bottom top", scrub:1.5 }
    });

    // Hero content fades out while scrolling
    gsap.to(".hero-content", {
        y:-35, opacity:0.3, ease:"none",
        scrollTrigger: { trigger:".hero", start:"35% top", end:"bottom top", scrub:true }
    });

    // ════════════════════════════════════════
    // 4. FLOATING PETAL EMITTERS on section enter
    // ════════════════════════════════════════
    function burstPetals(count=8) {
        for (let i=0; i<count; i++) {
            const p = document.createElement("div");
            p.style.cssText = `
                position:fixed; pointer-events:none; z-index:9000;
                width:${6+Math.random()*8}px; height:${6+Math.random()*8}px;
                border-radius: ${Math.random()>0.5 ? "50%" : "50% 0 50% 0"};
                background: ${sparkleColors[Math.floor(Math.random()*sparkleColors.length)]};
                left:${10+Math.random()*80}vw; top:${30+Math.random()*40}vh;
                opacity:0.9; transform:rotate(${Math.random()*360}deg);
            `;
            document.body.appendChild(p);
            gsap.to(p, {
                y: -(80+Math.random()*120),
                x: (Math.random()-0.5)*80,
                rotation: Math.random()*360,
                opacity: 0,
                duration: 1.5 + Math.random(),
                ease: "power2.out",
                delay: Math.random()*0.4,
                onComplete: () => p.remove()
            });
        }
    }

    // ════════════════════════════════════════
    // 5. SECTION TITLE — Word by Word Reveal
    // ════════════════════════════════════════
    document.querySelectorAll(".section-title").forEach(title => {
        const inner = title.innerHTML;
        const parts = inner.split(/(<[^>]+>|\s+)/g);
        let rebuilt = "";
        parts.forEach(p => {
            if (!p || p.startsWith("<") || /^\s+$/.test(p)) { rebuilt += p; }
            else { rebuilt += `<span class="word-wrap" style="overflow:hidden;display:inline-block;"><span class="word" style="display:inline-block;">${p}</span></span>`; }
        });
        title.innerHTML = rebuilt;

        const words = title.querySelectorAll(".word");
        gsap.set(words, { y:"110%", opacity:0 });
        ScrollTrigger.create({
            trigger: title, start:"top 80%", once:true,
            onEnter: () => {
                gsap.to(words, { y:"0%", opacity:1, duration:0.9, ease:"power4.out", stagger:0.07 });
                burstPetals(5);
            }
        });
    });

    // ════════════════════════════════════════
    // 6. TIMELINE — Split Slide with Bounce
    // ════════════════════════════════════════
    gsap.utils.toArray(".timeline-item").forEach((item) => {
        gsap.from(item.querySelector(".timeline-meta"), {
            x:-50, opacity:0, duration:0.9, ease:"back.out(1.5)",
            scrollTrigger: { trigger:item, start:"top 83%", toggleActions:"play none none none" }
        });
        gsap.from(item.querySelector(".timeline-content"), {
            x:50, opacity:0, duration:0.9, ease:"back.out(1.5)",
            scrollTrigger: { trigger:item, start:"top 83%", toggleActions:"play none none none" },
            delay:0.08
        });
    });

    // ════════════════════════════════════════
    // 7. GALLERY — Stagger with cute bounce
    // ════════════════════════════════════════
    gsap.utils.toArray(".experience-gallery").forEach(gallery => {
        gsap.from(gallery.querySelectorAll("img"), {
            scale:0.88, opacity:0, y:30, duration:0.8,
            ease:"back.out(2)", stagger:0.12,
            scrollTrigger: { trigger:gallery, start:"top 86%", toggleActions:"play none none none" }
        });
    });

    // ════════════════════════════════════════
    // 8. GALLERY HOVER TILT — 3D
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
    // 9. PROFILE CARD — float up
    // ════════════════════════════════════════
    gsap.from(".profile-showcase", {
        y:70, opacity:0, scale:0.96, duration:1.3, ease:"power4.out",
        scrollTrigger: { trigger:".profile-showcase", start:"top 86%", toggleActions:"play none none none" }
    });

    // ════════════════════════════════════════
    // 10. CONTACT ITEMS — cute cascade
    // ════════════════════════════════════════
    gsap.from(".contact-item", {
        y:30, opacity:0, scale:0.95, duration:0.7, ease:"back.out(1.8)", stagger:0.1,
        scrollTrigger: { trigger:".contact-grid", start:"top 85%", toggleActions:"play none none none" }
    });

    // ════════════════════════════════════════
    // 11. BACKGROUND COLOR SHIFT — smooth sections
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
        });
    });

    // ════════════════════════════════════════
    // 12. FOOTER — Staggered playful reveal
    // ════════════════════════════════════════
    const footerLines = document.querySelectorAll(".footer-line");
    if (footerLines.length) {
        gsap.set(footerLines, { y:60, opacity:0 });
        ScrollTrigger.create({
            trigger:".footer", start:"top 80%", once:true,
            onEnter: () => {
                gsap.to(footerLines, {
                    y:0, opacity:1, duration:1.0,
                    ease:"back.out(1.7)", stagger:0.15
                });
                gsap.to(".magnetic-btn", {
                    opacity:1, y:0, duration:0.9, ease:"back.out(1.5)", delay:0.5
                });
                burstPetals(12);
            }
        });
        gsap.set(".magnetic-btn", { opacity:0, y:20 });
    }

    // ════════════════════════════════════════
    // 13. MAGNETIC BUTTON — elastic
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

        // Heart burst on click
        btn.addEventListener("click", (e) => {
            for(let i=0; i<10; i++) {
                const h = document.createElement("div");
                h.textContent = ["💕","✨","🌸","💗","⭐"][Math.floor(Math.random()*5)];
                h.style.cssText = `position:fixed;font-size:${14+Math.random()*16}px;left:${e.clientX}px;top:${e.clientY}px;pointer-events:none;z-index:9999;`;
                document.body.appendChild(h);
                gsap.to(h, {
                    y:-(60+Math.random()*80), x:(Math.random()-0.5)*80,
                    opacity:0, duration:1+Math.random()*0.5,
                    ease:"power2.out", onComplete:()=>h.remove()
                });
            }
        });
    }

    // ════════════════════════════════════════
    // 14. SKILL CATEGORIES — cascade
    // ════════════════════════════════════════
    gsap.utils.toArray(".skill-category").forEach((cat,i) => {
        gsap.from(cat, {
            y:30, opacity:0, duration:0.8, ease:"back.out(1.5)",
            delay:i*0.1,
            scrollTrigger: { trigger:cat, start:"top 88%", toggleActions:"play none none none" }
        });
    });

});
"""
with open("script.js", "w", encoding="utf-8") as f:
    f.write(script)
print("script.js written with feminine animations")