
def change_password(user, old_password, new_password):
    if user.verify_password(old_password):
        user.set_password(new_password)
        return True
    return False