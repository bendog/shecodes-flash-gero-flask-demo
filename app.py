import random
from flask import Flask, render_template, request

app = Flask(__name__)

PET_LIST = [
    {'name':"Remus", "species":"dog", "age":5, "microchipped":True},
    {'name':"Izzy", "species":"cat", "age":12, "microchipped":True},
    {'name':"Archie", "species":"dog", "age":12, "microchipped":True},
    {'name':"Tuna", "species":"cat", "age":15, "microchipped":True},
    {'name':"Socks", "species":"cat", "age":3, "microchipped":False},
    {'name':"Biscuit", "species":"dog", "age":1, "microchipped":False},
    {'name':"Rory", "species":"dog", "age":7, "microchipped":True},
    {'name':"Polly", "species":"budgie", "age":23, "microchipped":False}
]

CATS = [
    'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg?resize=750px:*'
    'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR97cpOuFlad0uE8zwJ6DoBHNw7D-pHY4Oj4B_D0adMmFEh_DbG&usqp=CAU',
    'https://i.imgur.com/dc1PU8j.jpg',
    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cat-named-dymka-in-the-veterinary-clinic-best-where-it-had-news-photo-1582304174.jpg',
    'https://external-preview.redd.it/Bx-yJ3EDDpUvlcUl8IENcRXoZEpyqjD7Cpowvr0uIZw.jpg?auto=webp&s=cac1403d7c1ea4460acb0bda7a04e91a7871cdb4',
    'https://external-preview.redd.it/bI5-Tu9c1YENcqbod7uRRECMHDlLPPfLaHzSVn94nRg.jpg?width=640&crop=smart&auto=webp&s=d4d9690248a9769094d147c5d157a586984e6d27',
    'https://quokkas.amyskapers.dev/img/quokka_(1).jpg',
    'https://ichef.bbci.co.uk/news/320/media/images/68569000/jpg/_68569138_dzg_-_nidara.jpg',
    'https://www.thehappycatsite.com/wp-content/uploads/2017/10/30-Awesome-Tabby-Cat-Facts-HC-long.jpg',
]

DOGS = [
    'https://quokkas.amyskapers.dev/img/not_quokka_(1).jpg',
    'https://quokkas.amyskapers.dev/img/not_quokka_(2).jpg',
    'https://quokkas.amyskapers.dev/img/not_quokka_(3).jpg',
    'https://quokkas.amyskapers.dev/img/not_quokka_(4).jpg',
    'https://quokkas.amyskapers.dev/img/not_quokka_(5).jpg',
    'https://quokkas.amyskapers.dev/img/not_quokka_(6).jpg',
    'https://2.bp.blogspot.com/-heLpXegowfM/Wspl9Mo03OI/AAAAAAAB5xE/Rd62PDicS0YmAKjN26kAN7LJY9HjsniZACLcBGAs/s1600/cute-dogs-224-01.jpg',
    'https://i.pinimg.com/236x/a6/95/c3/a695c3240a377187a8d93871bb91f6c2.jpg',

]

def rando_pet(species):
    """ return a random picture of the desired species"""
    if species == 'cat':
        return random.choice(CATS)
    if species == 'dog':
        return random.choice(DOGS)
    

@app.route('/')
def index():
    return """<html>
    <head>
        <title>Hello SheCodes!</title>
    </head>
    <body>
        <h1>
            Hello SheCodes!
        </h1>
        <p>
            <a href='/pets'>pets list</a>
        </p>
    </body
    </html>
    """

@app.route('/pets')
def pets():
    pet_list = list(PET_LIST)
    args = request.args
    print(args)
    species = args.get('species')
    if species:
        pet_list = [pet for pet in pet_list if pet['species'] == species]
    return render_template("pets.html", pets=pet_list, pet_pic=rando_pet(species))

