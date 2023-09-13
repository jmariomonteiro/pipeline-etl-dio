# %%
import json
import pandas as pd
import openai
import random
import os
path = '/home/dell/DIO/pipeline-etl-dio/databases/inputs'

file = 'usuarios.csv'
nomes = ["Vinicius", "Mario", "Marcelino"]
openai.api_key = ''

df = pd.read_csv(os.path.join(path, file))
user_ids = df['userID'].tolist()


def atribuir_nomes_e_frases(users, nomes):
    nomes_atribuidos = []
    nomes_disponiveis = nomes.copy()

    for user_id in users:
        if not nomes_disponiveis:
            print("Não há nomes suficientes para atribuir a todos os userIDs.")
            break

        nome_usuario = random.choice(nomes_disponiveis)
        frase_motivacional = generate_motivational_phrase()
        nomes_atribuidos.append({
            "userID": user_id,
            "name": nome_usuario,
            "motivational_phrase": frase_motivacional
        })
        nomes_disponiveis.remove(nome_usuario)

    return nomes_atribuidos


def generate_motivational_phrase():
    input_text = "Me dê uma mensagem motivacional:"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=input_text,
        max_tokens=50,
    )
    return response.choices[0].message.content.strip('"')


nomes_atribuidos = atribuir_nomes_e_frases(user_ids, nomes)

json_data = json.dumps(nomes_atribuidos, indent=4)

print(json_data)


def update_message(user_data):
    for user in user_data:
        new_motivational_phrase = generate_motivational_phrase()
        user["motivational_phrase"] = new_motivational_phrase


update_message(nomes_atribuidos)

json_data_updated = json.dumps(nomes_atribuidos, indent=4)

print(json_data_updated)
