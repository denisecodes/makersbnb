from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
Test that user can login when correct information inputted 
"""

def test_correct_login(db_connection, page, test_web_address):
    db_connection.seed('seeds/users.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email_address]", 'email1@gmail.com')
    page.fill("input[name=user_password]", '12345')
    page.click("text='Click here to login'")
    spaces_page = page.locator("p")
    expect(spaces_page).to_have_text("This is the spaces page.")


"""
Test that when user logs in incorrectly, an error message appears
"""

def test_incorrect_login(db_connection, page, test_web_address):
    db_connection.seed('seeds/users.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email_address]", 'random@random.com')
    page.fill("input[name=user_password]", 'random')
    page.click("text='Click here to login'")
    invalid_login_error = page.locator(".login_error")
    expect(invalid_login_error).to_have_text("Please submit valid login.")
    
"""
Test that if a user leaves fields empty in login page
An error message will be produced 
"""

def test_empty_fields_login(db_connection, page, test_web_address):
    db_connection.seed('seeds/users.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email_address]", '')
    page.fill("input[name=user_password]", '')
    page.click("text='Click here to login'")
    invalid_login_error = page.locator(".login_error")
    expect(invalid_login_error).to_have_text("Please submit valid login.")