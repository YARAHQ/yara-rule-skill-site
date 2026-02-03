#!/usr/bin/env python3
"""Screenshot the YARA Rule Skill website using Playwright"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('http://localhost:8080')
    page.wait_for_load_state('networkidle')
    
    # Take full page screenshot
    page.screenshot(path='/home/neo/clawd/projects/yara-rule-skill-site/screenshot.png', full_page=True)
    print("Screenshot saved to screenshot.png")
    
    browser.close()
