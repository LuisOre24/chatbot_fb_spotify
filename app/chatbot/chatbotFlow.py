from app.helpers import sender_graph
from random import choice
from app.spotify.spotifyHelper import spotify_track

def initial_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": "Elige una opcion:",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Frase del día",
                        "payload":"frase_payload",
                        "image_url":"https://toppng.com/uploads/preview/su-yan-product-class-part-of-the-mobile-cloud-saas-message-system-icon-11562987830ap2lf0x65e.png"
                    },{
                        "content_type":"text",
                        "title":"Buscar musica",
                        "payload":"spotify_payload",
                        "image_url":"https://www.clipartmax.com/png/middle/91-911777_silentdisco-listening-music-icon-png.png"
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

def music_message(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text': 'Por favor, escribe que cancion deseas que busque'
    })

def search_track(**kwargs):
    records = spotify_track(kwargs['search'])
    return track_list(records, kwargs['recipient_id'])

def track_list(records, recipient_id):
    
    #for record in records['tracks']['items']:
    #    tracks = [track_json(record)]
    #print(tracks)
    tracks = [track_json(record) for record in records['tracks']['items']]
    print(tracks)
    return sender_graph(recipient_id=recipient_id, message={
        "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements": tracks
            }
        }
    })

def track_json(records):
    title = records['name']
    image_url = records['album']['images'][0]['url']
    artist = records['artists'][0]['name']
    subtitle = f'Cancion - {artist}' if records['type'] == 'track' else '-'
    url = records['external_urls']['spotify']
    return {
        'title': title,
        'image_url': image_url,
        'subtitle': subtitle,
        'buttons': [
            {
                "type": "web_url",
                "url": url,
                "title": 'Escuchar'
            }
        ]
    }
    

def template_generic(**kwargs):
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
            "attachment": {
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title":"Welcome!",
                            "image_url":"https://petersfancybrownhats.com/company_image.png",
                            "subtitle":"We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com/view?item=103",
                                },
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"https://petersfancybrownhats.com",
                                    "title":"View Website"
                                }              
                            ]      
                        },
                        {
                            "title":"Welcome!",
                            "image_url":"https://petersfancybrownhats.com/company_image.png",
                            "subtitle":"We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com/view?item=103",
                                },
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"https://petersfancybrownhats.com",
                                    "title":"View Website"
                                }              
                            ]      
                        },
                        {
                            "title":"Welcome!",
                            "image_url":"https://petersfancybrownhats.com/company_image.png",
                            "subtitle":"We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com/view?item=103",
                                },
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url":"https://petersfancybrownhats.com",
                                    "title":"View Website"
                                }              
                            ]      
                        }

                    ]
                }
            }
        })

    
