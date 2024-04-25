import json

# Exemplo de um dicionário Python
data = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Serializar o dicionário para JSON
json_data = json.dumps(data)

print("JSON serializado:")
print(json_data)

# Deserializar JSON de volta para um dicionário Python
decoded_data = json.loads(json_data)

print("\nDicionário Python:")
print(decoded_data)
