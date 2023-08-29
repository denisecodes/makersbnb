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

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    page.click("text=Login")
    login_tag = page.locator("p")
    expect(login_tag).to_have_text("This is the login page.")

def test_get_spaces_from_login_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/new")
    page.click("text=Sign in")
    login_tag = page.locator("p")
    expect(login_tag).to_have_text("This is the spaces page.")

def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    info_tag = page.locator("p")
    expect(info_tag).to_have_text("This is the spaces page.")

def test_get_requests(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=Requests")
    info_tag = page.locator("p")
    expect(info_tag).to_have_text("This is the requests page.")   

def test_get_sign_out(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=Sign out")
    info_tag = page.locator("p")
    expect(info_tag).to_have_text("This is the homepage.")   