import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('viso')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    name = event['firstName'] +' '+ event['lastName']
    email = event['email']
    response = table.put_item(
        Item={
            'ID': name,
            'Email' : email,
            'LatestGreetingTime':now
            })
    return {
        'statusCode': 200,
        'body': json.dumps('From Lambda, Hello ' + name + ', your email is' + email)
    }
