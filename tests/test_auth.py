from auth import Auth

def test_register():
    auth = Auth()
    auth.register("user1", "password1")
    assert "user1" in auth.users

def test_request_password_reset():
    auth = Auth()
    auth.register("user1", "password1")
    token = auth.request_password_reset("user1")
    assert token is not None

def test_reset_password():
    auth = Auth()
    auth.register("user1", "password1")
    token = auth.request_password_reset("user1")
    assert auth.reset_password("user1", token, "new_password1")

def test_send_password_reset_email():
    auth = Auth()
    auth.register("user1", "password1")
    token = auth.request_password_reset("user1")
    auth.send_password_reset_email("user1", token)

def test_authenticate():
    auth = Auth()
    auth.register("user1", "password1")
    assert auth.authenticate("user1", "password1")
    assert not auth.authenticate("user1", "wrong_password")
