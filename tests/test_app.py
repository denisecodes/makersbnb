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
def test_go_to_sign_up(page, test_web_address, db_connection):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    title = page.locator("h1")
    expect(title).to_have_text("Sign Up to MakersBnB")

    page.fill("input[name='first_name']", "Denise")
    page.fill("input[name='last_name']", "Chan")
    page.fill("input[name='email_address']", "denise@gmail.com")
    page.fill("input[name='user_password']", "28374663alal")
    
    page.click("text='Sign Up'")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("This is the homepage.")
    row = db_connection.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    user = row[0]
    assert user["id"] == 7
    assert user["first_name"] == "Denise"
    assert user["last_name"] == "Chan"
    assert user["email_address"] == "denise@gmail.com"
    assert user["user_password"] == "28374663alal"

def test_validate_user(page, test_web_address, db_connection):
    db_connection.seed('seeds/users.sql')
    page.goto(f"http://{test_web_address}/sign_up")

    page.click("text='Sign Up'")

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: "
        "First name must not be blank, " \
        "Last name must not be blank, " \
        "Email address must not be blank, " \
        "Password must not be blank"
    )