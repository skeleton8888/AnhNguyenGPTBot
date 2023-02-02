from bot import handle_request

def handle(event, context):
    response = handle_request(event)
    return {
        'statusCode': 200,
        'body': response
    }
