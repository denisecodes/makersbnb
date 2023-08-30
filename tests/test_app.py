from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")

"""
Go to sign up route
See the sign up form with first_name, last_name, email and password and fields
"""
def test_go_to_sign_up(page, test_web_address):
    page.goto(f"http://{test_web_address}/sign_up")
    title = page.locator("h1")
    expect(title).to_have_text("Sign Up")
    page.fill("input[name='first_name']", "Denise")