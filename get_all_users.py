import boto3


def get_all_users(event, context):
    dynamodb = boto3.client('dynamodb', 'eu-west-2')
    users = dynamodb.scan(
        TableName='StepFunctionDemoDynamoDB'
    )
    # initiated = ['first_one']
    users = users['Items']
    users.insert(0, "First_One")
    users.append("DONE")
    # initiated.append(users)
    # initiated.append('DONE')
    return {
        "users": users
    }
