#!/usr/bin/env python3
"""
Script to update navigation and footer in HTML files
"""

import re
import sys

# Navigation HTML template
NAV_HTML = '''    <!-- Navigation -->
    <nav class="navigation" id="navigation">
        <div class="nav-container">
            <a href="index.html" class="logo">MarketingTool.Pro</a>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="services.html" class="nav-link">Services</a></li>
                <li class="dropdown">
                    <div class="dropdown-toggle nav-link">
                        Resources ▼
                    </div>
                    <div class="dropdown-menu">
                        <a href="blog.html" class="dropdown-item">Blog</a>
                        <a href="guides.html" class="dropdown-item">Guides</a>
                        <a href="case-studies.html" class="dropdown-item">Case Studies</a>
                        <a href="webinars.html" class="dropdown-item">Webinars</a>
                    </div>
                </li>
                <li><a href="blog.html" class="nav-link">Blog</a></li>
                <li class="dropdown">
                    <div class="dropdown-toggle nav-link">
                        Company ▼
                    </div>
                    <div class="dropdown-menu">
                        <a href="about.html" class="dropdown-item">About Us</a>
                        <a href="careers.html" class="dropdown-item">Careers</a>
                        <a href="contact.html" class="dropdown-item">Contact</a>
                        <a href="privacy.html" class="dropdown-item">Privacy Policy</a>
                    </div>
                </li>
                <li><a href="signin.html" class="nav-link">Sign In</a></li>
                <li><a href="trial.html" class="btn btn-primary">Start Free Trial</a></li>
            </ul>
            <button class="mobile-menu-btn" id="mobileMenuBtn">☰</button>
        </div>
    </nav>'''

# Footer HTML template
FOOTER_HTML = '''    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>MarketingTool.Pro</h3>
                    <p>AI-powered marketing automation platform with 811+ tools for complete campaign management and optimization across USA, Canada, and India markets.</p>
                    <ul class="footer-contact">
                        <li>📞 <a href="tel:+18555742506">+1-855-574-2506</a></li>
                        <li>✉️ <a href="mailto:help@marketingtool.pro">help@marketingtool.pro</a></li>
                        <li>📍 F-12 Govindam Tower, Jaipur 302012, India</li>
                        <li>🏢 Registration: RJ-17-0526261</li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Product</h4>
                    <ul class="footer-links">
                        <li><a href="index.html#features">Features</a></li>
                        <li><a href="pricing.html">Pricing</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="trial.html">Free Trial</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul class="footer-links">
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="guides.html">Guides</a></li>
                        <li><a href="case-studies.html">Case Studies</a></li>
                        <li><a href="webinars.html">Webinars</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Company</h4>
                    <ul class="footer-links">
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="careers.html">Careers</a></li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="privacy.html">Privacy Policy</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Legal</h4>
                    <ul class="footer-links">
                        <li><a href="terms.html">Terms of Service</a></li>
                        <li><a href="refund-policy.html">Refund Policy</a></li>
                        <li><a href="cookies.html">Cookie Policy</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2025 Marketing Tool Pro - Infinity Solutions (India). All rights reserved.</p>
                <p>Empowering businesses with AI-driven marketing automation | Trusted by 10,000+ customers worldwide</p>
            </div>
        </div>
    </footer>'''

# JavaScript template
JS_TEMPLATE = '''    <script>
        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const navMenu = document.getElementById('navMenu');

        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Navigation scroll effect
        const navigation = document.getElementById('navigation');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navigation.classList.add('scrolled');
            } else {
                navigation.classList.remove('scrolled');
            }
        });
    </script>'''

def update_html_file(filepath):
    """Update navigation and footer in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace navigation
        content = re.sub(
            r'<nav class="navigation"[^>]*>.*?</nav>',
            NAV_HTML,
            content,
            flags=re.DOTALL
        )

        # Replace footer
        content = re.sub(
            r'<footer class="footer">.*?</footer>',
            FOOTER_HTML,
            content,
            flags=re.DOTALL
        )

        # Replace scripts before </body>
        content = re.sub(
            r'<script.*?</script>\s*</body>',
            JS_TEMPLATE + '\n</body>',
            content,
            flags=re.DOTALL
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ Updated {filepath}")
        return True

    except Exception as e:
        print(f"✗ Error updating {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python update_nav_footer.py <file1.html> <file2.html> ...")
        sys.exit(1)

    for filepath in sys.argv[1:]:
        update_html_file(filepath)
