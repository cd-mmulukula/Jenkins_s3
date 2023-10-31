import json

def lambda_handler(event, context):
    name = event.get('name', 'World')
    greeting = f"Hello, {name}!"
    
    return {
        'statusCode': 200,
        'body': json.dumps(greeting)
    }
