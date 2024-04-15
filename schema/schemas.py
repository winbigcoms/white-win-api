def indivisual_serial(todo)->dict:
    return {
        "id":str(todo['_id']),
        "title":str(todo['title']),
        "memo":str(todo['memo']),
        "imgs":list(todo['imgs']),
        "isVisited":bool(todo['isVisited']),
        "tag":str(todo['tag']),
    }

def list_serial(todos) -> list:
    return [indivisual_serial(todo) for todo in todos]