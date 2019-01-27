
def send_email(event, context):

    return "Mail sent to " + str(event["users"][0]["name"])
