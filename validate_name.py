
def validate_name(event, context):
    name = event["users"][0]["name"]["S"]
    try:
        return len(name) > 1
    except:
        pass
    return False
