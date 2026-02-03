#!/usr/bin/env python3
"""Screenshot the YARA Rule Skill website - mobile viewport"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 2000})
    page.goto('http://localhost:8081')
    page.wait_for_load_state('networkidle')
    
    # Take viewport screenshot (first screen only)
    page.screenshot(path='/home/neo/clawd/projects/yara-rule-skill-site/screenshot-top.png')
    print("Top screenshot saved")
    
    # Scroll and take middle
    page.evaluate("window.scrollTo(0, 1500)")
    page.screenshot(path='/home/neo/clawd/projects/yara-rule-skill-site/screenshot-mid.png')
    print("Mid screenshot saved")
    
    browser.close()
