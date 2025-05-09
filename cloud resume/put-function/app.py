import json
import boto3
from boto3.dynamodb.conditions import Key
# import requests

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')
def put_handler(event, context):
    response = table.update_item(
        Key={'ID': 'visitors'},
        UpdateExpression="SET #count = if_not_exists(#count, :start) + :inc",
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':inc': 1, ':start': 0},
        ReturnValues="UPDATED_NEW"
    )
   current_count = int(response['Attributes']['count'])

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
            },
        "statusCode": 200,
        "body": json.dumps({
            'count': 4
            # "location": ip.text.replace("\n", "")
        }),
    }
