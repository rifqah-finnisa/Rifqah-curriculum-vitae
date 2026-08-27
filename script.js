/*
 * ==========================================
 * AEGIS COGNITIVE RUNTIME PLATFORM
 * PROPRIETARY AND CONFIDENTIAL
 * Copyright (c) 2024-2026 Wahyu Nur Iman. 
 * All rights reserved.
 * ==========================================
 */

document.addEventListener("DOMContentLoaded", () => {
    lucide.createIcons();
    // 1. Initialize Lenis Smooth Scroll
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        smooth: true,
    });

    lenis.on('scroll', ScrollTrigger.update);

    gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);

    // 2. Hero Animations
    const heroTl = gsap.timeline();
    
    // Animate Text
    heroTl.from(".reveal-text", {
        y: 100,
        opacity: 0,
        duration: 1.2,
        ease: "power4.out",
        stagger: 0.1,
        delay: 0.2
    })
    // Animate smaller hero elements
    .from(".reveal-fade", {
        y: 20,
        opacity: 0,
        duration: 1,
        ease: "power3.out",
        stagger: 0.1
    }, "-=0.8");

    // 3. ScrollTrigger Animations for Sections
    // Parallax on hero image
    gsap.to(".hero-image", {
        yPercent: 30,
        ease: "none",
        scrollTrigger: {
            trigger: ".hero",
            start: "top top",
            end: "bottom top",
            scrub: true
        }
    });

    // Background color shift for freelance section
    ScrollTrigger.create({
        trigger: "#freelance",
        start: "top center",
        end: "bottom center",
        onEnter: () => gsap.to("body", { backgroundColor: "#F3EBE6", duration: 1 }), // Soft blush bg
        onLeaveBack: () => gsap.to("body", { backgroundColor: "#FAF8F5", duration: 1 }), // Soft cream bg
        onEnterBack: () => gsap.to("body", { backgroundColor: "#F3EBE6", duration: 1 }),
        onLeave: () => gsap.to("body", { backgroundColor: "#FAF8F5", duration: 1 })
    });

    // Reveal elements on scroll
    gsap.utils.toArray('.reveal').forEach(el => {
        gsap.from(el, {
            opacity: 0,
            y: 50,
            duration: 1,
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
                toggleActions: "play none none reverse"
            }
        });
    });

    // 4. Magnetic Button in Footer
    const magneticBtn = document.querySelector('.magnetic-btn');
    if (magneticBtn) {
        magneticBtn.addEventListener('mousemove', (e) => {
            const rect = magneticBtn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            gsap.to(magneticBtn, {
                x: x * 0.3,
                y: y * 0.3,
                duration: 0.5,
                ease: "power3.out"
            });
            gsap.to(magneticBtn.querySelector('.btn-text'), {
                x: x * 0.1,
                y: y * 0.1,
                duration: 0.5,
                ease: "power3.out"
            });
        });

        magneticBtn.addEventListener('mouseleave', () => {
            gsap.to(magneticBtn, {
                x: 0,
                y: 0,
                duration: 0.7,
                ease: "elastic.out(1, 0.3)"
            });
            gsap.to(magneticBtn.querySelector('.btn-text'), {
                x: 0,
                y: 0,
                duration: 0.7,
                ease: "elastic.out(1, 0.3)"
            });
        });
    }
});
