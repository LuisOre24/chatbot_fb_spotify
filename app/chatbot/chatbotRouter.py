from app import api
from os import getenv
from json import dumps
from requests import post as post_request, delete as delete_request
from flask_restx import Resource, Namespace
from app.chatbot.chatbotRequest import ChatbotRequest
from app.chatbot.chatbotFlow import initial_message, random_messages, color_message

chatbot_ns = Namespace('chatbot', description='webhook messengerr facebook')

@chatbot_ns.route('/webhook')
class webhook(Resource):
    @chatbot_ns.doc('webhook_connect')
    @chatbot_ns.expect(ChatbotRequest.webhook())
    def get(self):
        '''Webhook Facebook Messenger'''
        parser = ChatbotRequest.webhook().parse_args()
        h_mode = parser['hub.mode']
        h_challenge = parser['hub.challenge']
        h_vtoken = parser['hub.verify_token']

        if h_mode and h_vtoken and h_mode == 'subscribe' and h_vtoken == getenv('FB_HOOK_TOKEN'):
            return int(h_challenge), 200
        return 'Token erroneo', 403

    @chatbot_ns.doc('webhook_messages')
    def post(self):
        '''Webhook Messenger Facebook - POST'''
#        print(self.api.payload)
        payload = self.api.payload
        print(payload)
        for event in payload['entry']:
            messaging = event['messaging']
            for message in messaging:
                recipient_id = message['sender']['id']
                if message.get('postback') \
                    and message['postback'] \
                    and message['postback'].get('payload'):

                    postback = message['postback'].get('payload')
                    if postback == '<GET_STARTED_PAYLOAD>':
                        initial_message(recipient_id=recipient_id)  
                if message.get('message') and message['message']:
                    if message['message'].get('quick_reply'):
                        quick_reply = message['message'].get('quick_reply')
                        if quick_reply['payload'] == 'red_payload':
                            color_message(recipient_id=recipient_id, color='rojo')

                        if quick_reply['payload'] == 'green_payload':
                            color_message(recipient_id=recipient_id, color='verde')
                    
                    random_messages(recipient_id=recipient_id)
        return 'Message received', 200

@chatbot_ns.route('/setup')
class bot_setup(Resource): 
    @chatbot_ns.doc('chatbot_setup')
    def get(self):
        '''Setup Get Started'''
        post_request('https://graph.facebook.com/v11.0/me/messenger_profile',
        params={
            'access_token': getenv('FB_PAGE_TOKEN')
        },
        headers={
            'Content-Type': 'application/json'
        },
        data=dumps({
            'get_started' : {
                'payload' : '<GET_STARTED_PAYLOAD>'
            },
            'greeting' : [
                {
                    'locale' : 'default',
                    'text' : 'Hola {{user_full_name}} !!!'
                }
            ]
        }))
        return 'Success', 200

@chatbot_ns.route('/setup/remove')
class bot_setup_remove(Resource):
    @chatbot_ns.doc('chatbot_remove_setup')
    def delete(self):
        '''Remove Get Started and Greeting'''
        delete_request('https://graph.facebook.com/v11.0/me/messenger_profile', 
            params={
                'access_token': getenv('FB_PAGE_TOKEN')
            },
            headers={
                'Content-Type': 'application/json'
            },
            data=dumps({
                'fields': ['get_started', 'greeting']
            }))

        return 'Success Deleted', 200

api.add_namespace(chatbot_ns)