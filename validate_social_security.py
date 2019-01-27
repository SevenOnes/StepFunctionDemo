
def validate_ss(event, context):
    ss = event["users"][0]["social_security"]["S"]
    try:
        return len(ss) > 1
    except:
        pass
    return False
