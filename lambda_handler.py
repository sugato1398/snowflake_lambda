import json
import time
import boto3
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE='snowflake_machine_id'
table = dynamodb.Table(TABLE)

def get_machine_id():
    for i in range(10):
        try:
            table.update_item(
                Key={'id':i},
                UpdateExpression='SET in_use = :true',
                ConditionExpression = Attr('in_use').eq(False),
                ExpressionAttributeValues={':true': True},
            )
            return i
        except Exception as e:
            print(e)
            continue

def release_machine_id(id):
    table.update_item(
        Key={'id':id},
        UpdateExpression='SET in_use = :false',
        ExpressionAttributeValues={':false': False},
    )

def lambda_handler(event, context):
    t = int(time.time()*1000)
    machine_id = get_machine_id()

    id_string = str(t)+ f"{machine_id:04d}"
    
    release_machine_id(machine_id)

    return {
        'statusCode': 200,
        'id': id_string
    }
