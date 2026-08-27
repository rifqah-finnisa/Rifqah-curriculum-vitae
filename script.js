/*
 * ==========================================
 * AEGIS COGNITIVE RUNTIME PLATFORM
 * PROPRIETARY AND CONFIDENTIAL
 * Copyright (c) 2024-2026 Wahyu Nur Iman.
 * All rights reserved.
 * ==========================================
 */

document.addEventListener("DOMContentLoaded", () => {
    // Initialize Lucide Icons
    lucide.createIcons();

    // ════════════════════════════════════════
    // 1. LENIS — Cinematic Smooth Scroll
    // ════════════════════════════════════════
    const lenis = new Lenis({
        duration: 1.4,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        smooth: true,
        smoothTouch: false,
    });

    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((time) => { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);

    // ════════════════════════════════════════
    // 2. HERO — Cinematic Entrance
    // ════════════════════════════════════════
    const heroTl = gsap.timeline({ defaults: { ease: "power4.out" } });

    heroTl
        // Photo slides in from right with a light scale
        .from(".hero-image", {
            scale: 1.08,
            opacity: 0,
            duration: 1.8,
            ease: "power3.out"
        }, 0)
        // Name RIFQAH drops in from below
        .from(".reveal-text:first-of-type", {
            y: 120,
            opacity: 0,
            duration: 1.2,
        }, 0.2)
        // FINNISA outline follows slightly after
        .from(".reveal-text.outline", {
            y: 80,
            opacity: 0,
            duration: 1.2,
        }, 0.38)
        // Subtitle, bio, scroll indicator appear
        .from(".reveal-fade", {
            y: 24,
            opacity: 0,
            duration: 0.9,
            stagger: 0.12,
        }, 0.7)
        .from(".scroll-indicator", {
            y: 16,
            opacity: 0,
            duration: 0.8,
        }, 1.0);

    // ════════════════════════════════════════
    // 3. HERO PARALLAX on Scroll
    // ════════════════════════════════════════
    gsap.to(".hero-image", {
        yPercent: 22,
        ease: "none",
        scrollTrigger: {
            trigger: ".hero",
            start: "top top",
            end: "bottom top",
            scrub: 1.5
        }
    });

    // Hero content fades and rises slightly on scroll
    gsap.to(".hero-content", {
        y: -40,
        opacity: 0.4,
        ease: "none",
        scrollTrigger: {
            trigger: ".hero",
            start: "30% top",
            end: "bottom top",
            scrub: true
        }
    });

    // ════════════════════════════════════════
    // 4. SECTION TITLE — Cinematic Text Reveal
    //    Words split and stagger up with clip-path
    // ════════════════════════════════════════
    document.querySelectorAll(".section-title").forEach(title => {
        const words = title.innerHTML.split(/(\s+|<br>|<[^>]+>)/g);
        // Wrap each word in a clip container only for text nodes
        let newHtml = words.map(part => {
            if (part.startsWith("<") || /^\s+$/.test(part) || part === "") {
                return part;
            }
            return `<span class="word-wrap"><span class="word">${part}</span></span>`;
        }).join("");
        title.innerHTML = newHtml;

        const wordEls = title.querySelectorAll(".word");
        gsap.set(wordEls, { y: "110%", opacity: 0 });

        ScrollTrigger.create({
            trigger: title,
            start: "top 80%",
            onEnter: () => {
                gsap.to(wordEls, {
                    y: "0%",
                    opacity: 1,
                    duration: 1.0,
                    ease: "power4.out",
                    stagger: 0.06
                });
            },
            once: true
        });
    });

    // ════════════════════════════════════════
    // 5. TIMELINE ITEMS — Staggered slide-in
    // ════════════════════════════════════════
    gsap.utils.toArray(".timeline-item").forEach((item, i) => {
        const meta = item.querySelector(".timeline-meta");
        const content = item.querySelector(".timeline-content");

        gsap.from(meta, {
            x: -40,
            opacity: 0,
            duration: 0.9,
            ease: "power3.out",
            scrollTrigger: {
                trigger: item,
                start: "top 82%",
                toggleActions: "play none none none"
            }
        });

        gsap.from(content, {
            x: 40,
            opacity: 0,
            duration: 0.9,
            ease: "power3.out",
            delay: 0.08,
            scrollTrigger: {
                trigger: item,
                start: "top 82%",
                toggleActions: "play none none none"
            }
        });
    });

    // ════════════════════════════════════════
    // 6. GALLERY IMAGES — Staggered reveal with slight scale
    // ════════════════════════════════════════
    gsap.utils.toArray(".experience-gallery").forEach(gallery => {
        const imgs = gallery.querySelectorAll("img");
        gsap.from(imgs, {
            scale: 0.92,
            opacity: 0,
            duration: 0.8,
            ease: "power3.out",
            stagger: 0.1,
            scrollTrigger: {
                trigger: gallery,
                start: "top 85%",
                toggleActions: "play none none none"
            }
        });
    });

    // ════════════════════════════════════════
    // 7. PROFILE CARD — floating reveal
    // ════════════════════════════════════════
    gsap.from(".profile-showcase", {
        y: 60,
        opacity: 0,
        scale: 0.97,
        duration: 1.2,
        ease: "power4.out",
        scrollTrigger: {
            trigger: ".profile-showcase",
            start: "top 85%",
            toggleActions: "play none none none"
        }
    });

    // ════════════════════════════════════════
    // 8. CONTACT ITEMS — cascade from bottom
    // ════════════════════════════════════════
    gsap.from(".contact-item", {
        y: 30,
        opacity: 0,
        duration: 0.7,
        ease: "power3.out",
        stagger: 0.1,
        scrollTrigger: {
            trigger: ".contact-grid",
            start: "top 85%",
            toggleActions: "play none none none"
        }
    });

    // ════════════════════════════════════════
    // 9. SKILL CATEGORIES — fade + y
    // ════════════════════════════════════════
    gsap.utils.toArray(".skill-category").forEach((cat, i) => {
        gsap.from(cat, {
            y: 30,
            opacity: 0,
            duration: 0.8,
            ease: "power3.out",
            delay: i * 0.12,
            scrollTrigger: {
                trigger: cat,
                start: "top 87%",
                toggleActions: "play none none none"
            }
        });
    });

    // ════════════════════════════════════════
    // 10. BACKGROUND COLOR SHIFT on section change
    // ════════════════════════════════════════
    const sections = [
        { id: "#mc-events",  bg: "#F8F4F0", duration: 1 },
        { id: "#work",       bg: "#F0EAE5", duration: 1 },
        { id: "#education-skills", bg: "#F8F4F0", duration: 1 }
    ];

    sections.forEach(({ id, bg, duration }) => {
        const el = document.querySelector(id);
        if (!el) return;
        ScrollTrigger.create({
            trigger: el,
            start: "top 50%",
            end: "bottom 50%",
            onEnter: () => gsap.to("body", { backgroundColor: bg, duration }),
            onEnterBack: () => gsap.to("body", { backgroundColor: bg, duration }),
        });
    });

    // ════════════════════════════════════════
    // 11. MAGNETIC BUTTON in Footer
    // ════════════════════════════════════════
    const magneticBtn = document.querySelector(".magnetic-btn");
    if (magneticBtn) {
        const inner = magneticBtn.querySelector(".btn-text") || magneticBtn;

        magneticBtn.addEventListener("mousemove", (e) => {
            const rect = magneticBtn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            gsap.to(magneticBtn, { x: x * 0.35, y: y * 0.35, duration: 0.5, ease: "power3.out" });
            gsap.to(inner, { x: x * 0.1, y: y * 0.1, duration: 0.5, ease: "power3.out" });
        });

        magneticBtn.addEventListener("mouseleave", () => {
            gsap.to(magneticBtn, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1,0.4)" });
            gsap.to(inner, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1,0.4)" });
        });
    }

    // ════════════════════════════════════════
    // 12. HOVER TILT on Gallery Images
    // ════════════════════════════════════════
    document.querySelectorAll(".experience-gallery img").forEach(img => {
        img.addEventListener("mousemove", (e) => {
            const rect = img.getBoundingClientRect();
            const xRatio = (e.clientX - rect.left) / rect.width - 0.5;
            const yRatio = (e.clientY - rect.top) / rect.height - 0.5;
            gsap.to(img, {
                rotationY: xRatio * 10,
                rotationX: -yRatio * 10,
                scale: 1.04,
                ease: "power2.out",
                duration: 0.4,
                transformPerspective: 600
            });
        });
        img.addEventListener("mouseleave", () => {
            gsap.to(img, {
                rotationY: 0, rotationX: 0, scale: 1,
                ease: "power3.out", duration: 0.6
            });
        });
    });

    // ════════════════════════════════════════
    // 13. FOOTER — cinematic text reveal
    // ════════════════════════════════════════
    gsap.from(".footer-content h2", {
        y: 80,
        opacity: 0,
        duration: 1.2,
        ease: "power4.out",
        scrollTrigger: {
            trigger: ".footer",
            start: "top 75%",
            toggleActions: "play none none none"
        }
    });

    gsap.from(".magnetic-btn", {
        y: 30,
        opacity: 0,
        duration: 0.9,
        ease: "power3.out",
        delay: 0.3,
        scrollTrigger: {
            trigger: ".footer",
            start: "top 75%",
            toggleActions: "play none none none"
        }
    });

});
