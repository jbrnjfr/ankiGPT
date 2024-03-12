# import json
# import urllib.request

# # def request(action, **params):
# #     return {'action': action, 'params': params, 'version': 6}

# # def invoke(action, **params):
# #     requestJson = json.dumps(request(action, **params)).encode('utf-8')
# #     response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
# #     if len(response) != 2:
# #         raise Exception('response has an unexpected number of fields')
# #     if 'error' not in response:
# #         raise Exception('response is missing required error field')
# #     if 'result' not in response:
# #         raise Exception('response is missing required result field')
# #     if response['error'] is not None:
# #         raise Exception(response['error'])
# #     return response['result']

# # invoke('createDeck', deck='test2')
# # result = invoke('deckNames')
# # print('got list of decks: {}'.format(result))

# import requests
# import json
# import urllib.request

# def add_cards_to_anki(cards):
#     anki_connect_url = "http://localhost:8765"
#     action = "addNotes"

#     # Construct the request payload
#     payload = {
#         "action": action,
#         "version": 6,
#         "params": {
#             "notes": cards
#         }
#     }

#     # Send the request to AnkiConnect
#     try:
#         response = requests.post(anki_connect_url, json=payload)
#         response.raise_for_status()
#         result = response.json()
#         print("Cards added successfully!")
#         print("Added notes:", result)
#     except requests.exceptions.RequestException as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     # Define the flashcards
#     flashcards = [
#         {
#             "deckName": "test2",
#             "modelName": "Basic",
#             "fields": {
#                 "Front": "Prompting a pretrained language model with natural language patterns has been proved effective for natural language understanding (NLU). However, what did our preliminary study reveal about manual discrete prompts?",
#                 "Back": "Our preliminary study reveals that manual discrete prompts often lead to unstable performance—e.g., changing a single word in the prompt might result in substantial performance drop."
#             }
#         },
#         {
#             "deckName": "test2",
#             "modelName": "Basic",
#             "fields": {
#                 "Front": "What is the proposed method for stabilizing training and improving performance in natural language understanding tasks?",
#                 "Back": "The proposed method is P-Tuning, which employs trainable continuous prompt embeddings in concatenation with discrete prompts."
#             }
#         },
#         # Add more flashcards here following the same format
#     ]

#     # Add the flashcards to AnkiWeb
#     add_cards_to_anki(flashcards)

import requests
import json

def add_card_to_anki(front, back, deck_name):
    anki_connect_url = "http://localhost:8765"
    action = "addNote"

    # Construct the request payload
    payload = {
        "action": action,
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "options": {
                    "allowDuplicate": False
                }
            }
        }
    }

    # Send the request to AnkiConnect
    try:
        response = requests.post(anki_connect_url, json=payload)
        response.raise_for_status()
        result = response.json()
        print("Card added successfully!")
        print("Added note:", result)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    # Specify the path to your text file
    text_file_path = "gans_flashcards.txt"
    deck_name = "test2"

    # Read the text file and add each flashcard
    with open(text_file_path, "r") as file:
        for line in file:
            front, back = line.strip().split("\t")  # Assuming tab-separated values
            add_card_to_anki(front, back, deck_name)
