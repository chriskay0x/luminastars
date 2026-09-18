/* ============================================================
   LUMINASTARS — main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ── LUCIDE ICONS ───────────────────────────────────────────
    lucide.createIcons();


    // ── SCROLL PROGRESS BAR ────────────────────────────────────
    const progressBar = document.getElementById('scrollProgress');

    window.addEventListener('scroll', () => {
        const scrollTop    = window.scrollY;
        const docHeight    = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled     = (scrollTop / docHeight) * 100;
        progressBar.style.width = `${scrolled}%`;
    }, { passive: true });


    // ── NAVBAR SCROLL GLASS EFFECT ─────────────────────────────
    const header = document.getElementById('header');

    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });


    // ── MOBILE MENU ────────────────────────────────────────────
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    menuToggle.addEventListener('click', () => {
        const isOpen = mobileMenu.classList.toggle('open');
        menuToggle.classList.toggle('open', isOpen);
        menuToggle.setAttribute('aria-expanded', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close mobile menu on link click
    document.querySelectorAll('.mobile-nav-link, .mobile-book').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('open');
            menuToggle.classList.remove('open');
            menuToggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        });
    });


    // ── ANIMATED COUNTERS ──────────────────────────────────────
    const counters = document.querySelectorAll('.stat-number');

    const animateCounter = (el) => {
        const target   = parseInt(el.getAttribute('data-target'), 10);
        const duration = 1800;
        const step     = target / (duration / 16);
        let current    = 0;

        const update = () => {
            current += step;
            if (current < target) {
                el.textContent = Math.floor(current);
                requestAnimationFrame(update);
            } else {
                el.textContent = target;
            }
        };

        requestAnimationFrame(update);
    };

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));


    // ── SCROLL REVEAL ──────────────────────────────────────────
    const revealEls = document.querySelectorAll(
        '.service-card, .celebrity-card, .project-card, .stat-item, .intro-left, .intro-right'
    );

    // Add reveal class
    revealEls.forEach((el, i) => {
        el.classList.add('reveal');
        el.style.transitionDelay = `${(i % 4) * 80}ms`;
    });

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });

    revealEls.forEach(el => revealObserver.observe(el));


    // ── NEWSLETTER FORM ────────────────────────────────────────
    const newsletterForm = document.getElementById('newsletterForm');

    if (newsletterForm) {
        newsletterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = newsletterForm.querySelector('.newsletter-input');
            const btn   = newsletterForm.querySelector('.newsletter-btn');

            if (!input.value || !input.value.includes('@')) return;

            btn.innerHTML = '<i data-lucide="check"></i>';
            input.value   = 'You\'re on the list!';
            input.disabled = true;
            lucide.createIcons();

            setTimeout(() => {
                input.value    = '';
                input.disabled = false;
                btn.innerHTML  = '<i data-lucide="arrow-right"></i>';
                lucide.createIcons();
            }, 3000);
        });
    }


    // ── ACTIVE NAV LINK ON SCROLL ──────────────────────────────
    const sections  = document.querySelectorAll('section[id]');
    const navLinks  = document.querySelectorAll('.nav-link');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.toggle(
                        'active',
                        link.getAttribute('href') === `#${entry.target.id}`
                    );
                });
            }
        });
    }, { threshold: 0.4 });

    sections.forEach(s => sectionObserver.observe(s));

});