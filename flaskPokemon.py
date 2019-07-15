# Soal 3 - Pokemon Battle
# =========================

from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
import json
import requests
import numpy as np
import pandas as pd
import joblib
import random
import os
import matplotlib.pyplot as plt

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/hasil', methods = ['POST', 'GET'])
def hasil():

    # load the joblib file
    model = joblib.load('modelPokemon')
    db = joblib.load('modelDataPokemon')

    # get the pokemon name from the HTML file
    name1 = request.form['pokemon1'].capitalize()
    name2 = request.form['pokemon2'].capitalize()

    # using try and except method
    try:
        if name1 == "":
            return render_template('errorpage.html')

        else:
            url = 'https://pokeapi.co/api/v2/pokemon/' + name1.lower()
            url2 = 'https://pokeapi.co/api/v2/pokemon/' + name2.lower()

            pokemon1 = requests.get(url)
            pokemon2 = requests.get(url2)

            id1 = pokemon1.json()["id"]
            id2 = pokemon2.json()["id"]

            foto1 = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+str(id1)+".png"
            foto2 = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/"+str(id2)+".png"

            # ==================================================================================================
            # prediction

            id1 = db['#'][db['Name'] == name1].values[0]
            hp1 = db['HP'][db['Name'] == name1].values[0]
            atk1 = db['Attack'][db['Name'] == name1].values[0]
            def1 = db['Defense'][db['Name'] == name1].values[0]
            spatk1 = db['Sp. Atk'][db['Name'] == name1].values[0]
            spdef1 = db['Sp. Def'][db['Name'] == name1].values[0]
            speed1 = db['Speed'][db['Name'] == name1].values[0]

            id2 = db['#'][db['Name'] == name2].values[0]
            hp2 = db['HP'][db['Name'] == name2].values[0]
            atk2 = db['Attack'][db['Name'] == name2].values[0]
            def2 = db['Defense'][db['Name'] == name2].values[0]
            spatk2 = db['Sp. Atk'][db['Name'] == name2].values[0]
            spdef2 = db['Sp. Def'][db['Name'] == name2].values[0]
            speed2 = db['Speed'][db['Name'] == name2].values[0]

            prediction = model.predict([[ hp1, hp2, atk1, atk2, def1, def2, spatk1, spatk2, spdef1, spdef2, speed1, speed2 ]])
            prob = model.predict_proba([[ hp1, hp2, atk1, atk2, def1, def2, spatk1, spatk2, spdef1, spdef2, speed1, speed2 ]])
            maxprob = prob[0].max()*100

            if prediction[0] == 1:
                hasilpred = name2
            else:
                hasilpred = name1

            # ==================================================================================================
            # plotting

            nameList = [name1, name2]

            listHP = []
            listAttack = []
            listDef = []
            listSpatk = []
            listSpdef = []
            listSpeed = []

            for i in nameList:
                listHP.append(db['HP'][db['Name'] == i].values[0])
            for i in nameList:
                listAttack.append(db['Attack'][db['Name'] == i].values[0])
            for i in nameList:
                listDef.append(db['Defense'][db['Name'] == i].values[0])
            for i in nameList:
                listSpatk.append(db['Sp. Atk'][db['Name'] == i].values[0])
            for i in nameList:
                listSpdef.append(db['Sp. Def'][db['Name'] == i].values[0])
            for i in nameList:
                listSpeed.append(db['Speed'][db['Name'] == i].values[0])

            plt.clf()
            plt.figure(figsize=(10, 6))

            plt.subplot(161)
            plt.bar(nameList, listHP, color='br')
            plt.xticks(rotation=90)
            plt.title('HP')

            plt.subplot(162)
            plt.bar(nameList, listAttack, color='br')
            plt.xticks(rotation=90)
            plt.title('Attack')

            plt.subplot(163)
            plt.bar(nameList, listDef, color='br')
            plt.xticks(rotation=90)
            plt.title('Defense')

            plt.subplot(164)
            plt.bar(nameList, listSpatk, color='br')
            plt.xticks(rotation=90)
            plt.title('Sp Attack')

            plt.subplot(165)
            plt.bar(nameList, listSpdef, color='br')
            plt.xticks(rotation=90)
            plt.title('Sp Defense')

            plt.subplot(166)
            plt.bar(nameList, listSpeed, color='br')
            plt.xticks(rotation=90)
            plt.title('Speed')

            xy = random.randint(10000, 9999999)
            listplot = os.listdir('./storage')
            aa = str(len(listplot) + 1) + '_' + str(xy) + '.jpg'

            plt.savefig('storage/%s' % aa)

            return render_template('showpage.html', a1=name1, a2=name2, zz=aa,  e=foto2, f=foto1, p=hasilpred, prob=round(maxprob))

    except():
        return redirect(url_for('error'))

@app.route('/plotku/<path:yy>')
def plotku(yy):
    return send_from_directory('storage', yy)

@app.route('/error')
def error():
    return render_template('errorpage.html')

# 404 route
@app.errorhandler(404)
def error404(error):
    return render_template('errorpage.html')

if __name__ == '__main__':
    app.run(debug = True)