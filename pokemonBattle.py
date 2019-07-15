# Soal 3 - Pokemon Battle
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import os

dataCombats = pd.read_csv('combats.csv')
dataPokemon = pd.read_csv('pokemon.csv')
dataTests = pd.read_csv('tests.csv')

dataPokemon.dropna(subset=['Name'], inplace=True)
dataPokemon1 = dataPokemon[[ '#', 'Name', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed' ]].copy()
dataPokemon1['sum'] = dataPokemon1.sum(axis=1)

# print(dataPokemon1.head())

import joblib
joblib.dump(dataPokemon1, 'modelDataPokemon')