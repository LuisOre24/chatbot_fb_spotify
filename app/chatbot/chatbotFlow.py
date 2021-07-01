from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], message='Hola mucho gusto, en que te puedo ayudar?')

def random_messages(**kwargs):
    palabras = ['que tal', 'no hay de que', 'no molestes', 'te observo']
    return sender_graph(recipient_id=kwargs['recipient_id'], message=choice(palabras))