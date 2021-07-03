from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": "Pick a color:",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Red",
                        "payload":"red_payload",
                        "image_url":"https://upload.wikimedia.org/wikipedia/commons/b/b9/Solid_red.png"
                    },{
                        "content_type":"text",
                        "title":"Green",
                        "payload":"green_payload",
                        "image_url":"https://upload.wikimedia.org/wikipedia/commons/c/c7/Solid_green.png"
                    }
                ]
            }
    )

def random_messages(**kwargs):
    palabras = ['Ten un buen día', 'En estos momentos estamos ocupados', \
        'Lo sentimos esta fuera de horario', 'Continue intentando', 'Todo estará bien',\
        'Estamos trabajando', 'Todo va por buen camino', 'Vamos mejorando', 'Esto esta por explotar', 'La App falló correctamente :)']
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text' : choice(palabras)
    })
    
def color_message(**kwargs):
    palabras = ['que tal', 'no hay de que', 'no molestes', 'te observo']
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text': f'Escogiste el color {kwargs["color"]}'
    })