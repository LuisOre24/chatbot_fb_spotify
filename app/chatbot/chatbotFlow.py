from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], 
    message={
        "text": "Frase del día:",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"Red",
                "payload":"<POSTBACK_PAYLOAD>",
                "image_url":"http://example.com/img/red.png"
            },
            {
                "content_type":"text",
                "title":"Green",
                "payload":"<POSTBACK_PAYLOAD>",
                "image_url":"http://example.com/img/green.png"
            }
        ]
    }
    )

def random_messages(**kwargs):
    palabras = ['Ten un buen día', 'En estos momentos estamos ocupados', 'Lo sentimos esta fuera de horario', 'Continue intentando', 'Todo estará bien', 'Estamos trabajando', 'Todo va por buen camino', 'Vamos mejorando', 'Esto esta por explotar', 'La App falló correctamente :)']
    return sender_graph(recipient_id=kwargs['recipient_id'], message=choice(palabras))