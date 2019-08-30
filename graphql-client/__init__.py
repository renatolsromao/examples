import os

from graphqlclient import GraphQLClient
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    client = GraphQLClient(os.getenv('GRAPHQL_ENDPOINT'))
    client.inject_token(
        'Bearer {}'.format(os.getenv('GRAPHQ_AUTH_TOKEN')))

    result = client.execute("""
    {
        user {
            environmentId
        }
    }
    """)

    print(result)
