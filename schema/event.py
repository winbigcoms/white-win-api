def indivisual_event_serial(event)->dict:
    return {
        "id":str(event['_id']),
        "event_title":str(event['event_title']),
        "date":str(event['date']),
        "opponent_name":str(event['opponent_name']),
    }

def event_list_serial(events) -> list:
    return [indivisual_event_serial(event) for event in events]