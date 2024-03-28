import boto3
from decimal import Decimal
import logging


# Configure the logging module
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'measurements'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Log information using the logging module
    logger.info("EVENT")
    item = {
        'sensor_id': event['sensor_id'],
        'created_at': event['created_at']
    }
    
    if 'temperature' in event:
        item['temperature'] = Decimal(event['temperature'])
    if 'humidity' in event:
        item['humidity'] = Decimal(event['humidity'])
    if 'preasure' in event:
        item['preasure'] = Decimal(event['preasure'])
    if 'gas' in event:
        item['gas'] = Decimal(event['gas'])
    if 'co2' in event: 
        item['co2'] = Decimal(event['co2'])
    
    logger.info(event['sensor_id'])
    
    # Write to DynamoDB
    table.put_item(
        Item=item
    )
    
    logger.info('Done Inputting')