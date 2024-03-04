def valid_email(email):
    if "@" in email:
        if "." in email:
            if len(email.split("@")[-1].split('.')) >= 2:
                return True
    return False
