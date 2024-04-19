def indivisual_serial(promise)->dict:
    return {
        "id":str(promise['_id']),
        "title":str(promise['title']),
        "memo":str(promise['memo']),
        "imgs":list(promise['imgs']),
        "isVisited":bool(promise['isVisited']),
        "tag":str(promise['tag']),
    }

def list_serial(promises) -> list:
    return [indivisual_serial(promise) for promise in promises]