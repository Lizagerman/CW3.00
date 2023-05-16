import json



def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def sort_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[0:5]

def format_data(data):
    operations = []
    for elem in data:
        date = elem["date"][:10].replace("-", ".")
        desc = elem["description"]
        sender_to = elem["to"].split()
        card_to = sender_to[-1]
        card_to = "**" + card_to[-4:]
        name_to = " ".join(sender_to[:-1])
        amount = elem["operationAmount"]["amount"] + " " + elem["operationAmount"]["currency"]["name"]
        if "from" in elem:
            sender_from = elem["from"].split()
            card_from = sender_from[-1]
            card_from = f"{card_from[:4]} {card_from[4:6]}** **** {card_from[-4:]}"
            name_from = " ".join(sender_from[:-1])
            operations.append(f"""{date} {desc} 
{name_from} {card_from} --> {name_to} {card_to} 
{amount}\n""")
        else:
            operations.append(f"""{date} {desc}
{name_to} {card_to}
{amount}\n""")
    return operations


