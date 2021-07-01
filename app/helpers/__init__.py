from os import getenv
from requests import post
from json import dumps


def sender_graph(**kwargs):
    post('https://graph.facebook.com/v11.0/me/messages',
        params={
            'access_token': getenv('FB_PAGE_TOKEN')
        },
        headers={
            'Content-Type': 'application/json'
        },
        data=dumps({
            'messaging_type': 'RESPONSE',
            'recipient': {
                'id': kwargs['recipient_id']
            },
            'message': {
                'text': kwargs['message']
            }
        }))