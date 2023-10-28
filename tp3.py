# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:49:28 2023

@author: Hp
"""
from pytrends.request import TrendReq

import datetime

import requests
#from flask import Flask, request, render_template, jsonify,redirect, url_for
from flask import Flask, request, render_template, jsonify,redirect

app = Flask(__name__,template_folder = 'templatesTP')
from io import BytesIO
import base64
import matplotlib.pyplot as plt



@app.route('/index')
def index():
    # Instancier un objet TrendReq
    pytrends = TrendReq(hl='fr-FR', tz=360)

    # Définir les paramètres de la requête
    kw_list = ["rugby","foot"]  # Liste de mots-clés ou d'expressions à rechercher

    # Calculer les dates pour les 10 derniers jours
    today = datetime.date.today()
    ten_days_ago = today - datetime.timedelta(days=10)

    timeframe = 'today 1-m'

    pytrends.build_payload(["rugby","foot"], timeframe=timeframe)  # Paramètres de la requête pour les 10 derniers jours

    # Obtenir les données d'intérêt
    interest_over_time_df = pytrends.interest_over_time()

    # Convertir les données d'intérêt en un graphique
    plt.figure(figsize=(10, 6))
    interest_over_time_df['rugby'].plot(label='Rugby')
    interest_over_time_df['foot'].plot(label='Football')
    plt.title('Google Trends Data for Rugby and Football')
    plt.xlabel('Date')
    plt.ylabel('Trends Index')
    plt.legend()

    # Convertir le graphique en une image pour l'afficher dans la page
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Retourner la page avec le graphique
    return f"<h1>Google Trends Data for Rugby and Football</h1>" \
           f"<img src='data:image/png;base64,{plot_url}'/>"
    return render_template('index7.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run()