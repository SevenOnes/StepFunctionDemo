import boto3
import uuid


def seed_dynamodb_handler(event, context):
    dynamodb = boto3.client('dynamodb', 'eu-west-2')
    try:
        response1 = dynamodb.put_item(
            TableName='StepFunctionDemoDynamoDB',
            Item={
                'userId': {
                    'S': "1"
                },
                'name': {
                    'S': 'Name1'
                },
                'surname': {
                    'S': 'Surname1'
                },
                'social_security': {
                    'S': '123456789'
                },
                'rating': {
                    'S': '4'
                },
                'phone': {
                    'S': '12345678910'
                },
                'email': {
                    'S': 'a@a.com'
                }
            }
        )

        response2 = dynamodb.put_item(
            TableName='StepFunctionDemoDynamoDB',
            Item={
                'userId': {
                    'S': "2"
                },
                'name': {
                    'S': 'Name2'
                },
                'surname': {
                    'S': 'Surname2'
                },
                'social_security': {
                    'S': '12345678911'
                },
                'rating': {
                    'S': '4'
                },
                'phone': {
                    'S': '12345678910'
                },
                'email': {
                    'S': 'b@b.com'
                }
            }
        )

        response3 = dynamodb.put_item(
            TableName='StepFunctionDemoDynamoDB',
            Item={
                'userId': {
                    'S': "3"
                },
                'name': {
                    'S': 'Name3'
                },
                'surname': {
                    'S': 'Surname3'
                },
                'social_security': {
                    'S': '123456789'
                },
                'rating': {
                    'S': '1'
                },
                'phone': {
                    'S': '12345678910'
                },
                'email': {
                    'S': 'c@c.com'
                }
            }
        )

        response4 = dynamodb.put_item(
            TableName='StepFunctionDemoDynamoDB',
            Item={
                'userId': {
                    'S': "4"
                },
                'name': {
                    'S': 'A'
                },
                'surname': {
                    'S': 'Surname4'
                },
                'social_security': {
                    'S': '123456789'
                },
                'rating': {
                    'S': '2'
                },
                'phone': {
                    'S': '12345678910'
                },
                'email': {
                    'S': 'd@d.com'
                }
            }
        )
    except:
        pass

    return "SUCCESS"
