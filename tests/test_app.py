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
    spaces_page = page.locator("h1")
    expect(spaces_page).to_have_text("Spaces")


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
    page.fill("input[name='user_password']", "12345")
    
    page.click("text='Sign Up'")
    strong_tag = page.locator(".homepage")
    expect(strong_tag).to_have_text("This is the homepage.")
    row = db_connection.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
    user = row[0]
    assert user["id"] == 7
    assert user["first_name"] == "Denise"
    assert user["last_name"] == "Chan"
    assert user["email_address"] == "denise@gmail.com"
    assert user["user_password"] == "12345"

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
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Login")
    login_tag = page.locator(".login_header")
    expect(login_tag).to_have_text("Login")


def test_get_spaces_from_login_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/new")
    page.click("text=Sign in")
    login_tag = page.locator("h1")
    expect(login_tag).to_have_text("Spaces")

def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    info_tag = page.locator("h1")
    expect(info_tag).to_have_text("Spaces")

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

def test_post_new_space(page, test_web_address, db_connection):
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=List a new space")
    header_tag = page.locator("h1")
    expect(header_tag).to_have_text("List your space")

    page.fill("input[name='title']", "test title")
    page.fill("input[name='description']", "test description")
    page.fill("input[name='price_per_night']", "111")
    page.fill("input[name='email_address']", "test@email.com")
    page.fill("input[name='user_id']", "1")
    page.click("text=List my space")
    spaces_header_tag = page.locator("h1")
    expect(spaces_header_tag).to_have_text("Spaces")
