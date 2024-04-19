def indivisual_user_serial(user)->dict:
    return {
        "id":str(user["_id"]),
        "email":str(user["email"]),
        "name":str(user["name"]),
        "main_event":str(user["main_event"])
    }

