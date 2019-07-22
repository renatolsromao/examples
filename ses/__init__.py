import boto3
from botocore.exceptions import ClientError


def send_example_email():
    AWS_REGION='us-east-1'
    SENDER = 'contato@renato.dev'
    RECIPIENT = 'contato@renato.dev'
    SUBJECT = 'SES Test'
    BODY_TEXT = ('Test SES email sending.')
    BODY_HTML = """
    <html>
    <head></head>
    <body>
        <p>Test SES.</p>
    </body>
    </html>
    """
    CHARSET = 'UTF-8'

    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    finally:
        print('Email sent.')


if __name__ == '__main__':
    send_example_email()