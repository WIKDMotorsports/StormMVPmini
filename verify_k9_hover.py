from playwright.sync_api import sync_playwright
import time
import os

def run():
    if not os.path.exists('/home/jules/verification'):
        os.makedirs('/home/jules/verification')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/K9.html")

        # Wait for animations
        time.sleep(2)

        # Screenshot 1: Base State
        page.screenshot(path="/home/jules/verification/1_base.png")
        print("Captured Base State")

        # Screenshot 2: Hover over Image
        page.hover(".product-image")
        time.sleep(1) # Wait for transition
        page.screenshot(path="/home/jules/verification/2_hover_image.png")
        print("Captured Hover Image State")

        # Reset mouse
        page.mouse.move(0, 0)
        time.sleep(1) # Wait for transition back

        # Screenshot 3: Hover over Buttons
        # Find the CTA buttons container
        page.hover(".product-cta")
        time.sleep(1) # Wait for transition
        page.screenshot(path="/home/jules/verification/3_hover_buttons.png")
        print("Captured Hover Buttons State")

        browser.close()

if __name__ == "__main__":
    run()
