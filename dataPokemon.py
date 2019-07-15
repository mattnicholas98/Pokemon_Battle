# Soal 3 - Pokemon Battle
# =========================

import pandas as pd
import numpy as np

# reading the pokemon csv file
dataPoke = pd.read_csv(
    'pokemon.csv',
    index_col = 0
)
dataPoke =dataPoke[[ 'Name', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed' ]]

dataCombats = pd.read_csv('combats.csv')

# =============================================================================
# creating lists for all the variables

id1 = []
id2 = []
hp1 = []
hp2 = []
atk1 = []
atk2 = []
def1 = []
def2 = []
spatk1 = []
spatk2 = []
spdef1 = []
spdef2 = []
speed1 = []
speed2 = []
winner = []

for i in range(len(dataCombats)):
    idPoke1 = dataCombats.iloc[i]['First_pokemon']
    idPoke2 = dataCombats.iloc[i]['Second_pokemon']

    winners = dataCombats.iloc[i]['Winner']

    id1.append(idPoke1)
    id2.append(idPoke2)

    hp1.append(dataPoke.loc[idPoke1]['HP'])
    hp2.append(dataPoke.loc[idPoke2]['HP'])

    atk1.append(dataPoke.loc[idPoke1]['Attack'])
    atk2.append(dataPoke.loc[idPoke2]['Attack'])

    def1.append(dataPoke.loc[idPoke1]['Defense'])
    def2.append(dataPoke.loc[idPoke2]['Defense'])

    spatk1.append(dataPoke.loc[idPoke1]['Sp. Atk'])
    spatk2.append(dataPoke.loc[idPoke2]['Sp. Atk'])

    spdef1.append(dataPoke.loc[idPoke1]['Sp. Def'])
    spdef2.append(dataPoke.loc[idPoke2]['Sp. Def'])

    speed1.append(dataPoke.loc[idPoke1]['Speed'])
    speed2.append(dataPoke.loc[idPoke2]['Speed'])

    if winners == idPoke1:
        win = 0
        winner.append(win)
    else:
        win = 1
        winner.append(win)

df = pd.DataFrame(
    dict(
        idPoke1 = id1,
        idPoke2 = id2,
        hp1 = hp1,
        hp2 = hp2,
        attack1 = atk1,
        attack2 = atk2,
        defense1 = def1,
        defense2 = def2,
        spatk1 = spatk1,
        spatk2 = spatk2,
        spdef1 = spdef1,
        spdef2 = spdef2,
        speed1 = speed1,
        speed2 = speed2,
        winner = winner
    )
)

# putting all these to a csv file
df.to_csv('datasetTrainPokemon.csv')