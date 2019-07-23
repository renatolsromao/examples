def hello(event, context):
    if 'raiseError' in event:
        raise ValueError('Intentional throw error.')

    response = {
        "statusCode": 200,
        "body": ''
    }

    return response


if __name__ == '__main__':
    hello('', '')
