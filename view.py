import csv
import re
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Load CSV data C:\Users\lerri\Desktop\Programming\Python-Html-Css\data.csv
with open('C:\\Users\\lerri\\Desktop\\Programming\\Python-Html-Css\\data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# calculates the probability of the message and message certainty is set to 0 (to show that there is not match to any response yet)
def message_probability(user_message, response, single_response=False, required_words=[]):
    message_certainty = 0

    # main words - words that are familiar to the bot
    main_words = ['multiple', 'IoT', 'device', 'controller', 'understand', 'context', 'adapt', 'interepret', 'language', 'integrate', 'siri', 'unique', 'accents', 'different', 'human', 'conversation', 'languages', 'it']
    
    # loop that will increase by 100 if the word by the user_message is in response and will increase by 2 if it is in main words
    for word in user_message:
        if word in response:
            message_certainty += 100
        elif word in main_words:
            message_certainty += 2

    # calculates the percentage of response from message_certainty divided by the number of words in rows and main words
    # rows - message (response of bot), list of words (similar to clues for the response of bot), single response, and required words
    percentage = float(message_certainty) / float(len(rows) + len(main_words))

    # checks if all the words in user message are in required words
    has_required_words = all(word in user_message for word in required_words) 

    # checks if it has the required words or has any of the single response, if it has it will return a confidence score
    # confidence score - system's level of certainty about the correctness of the response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# will check all the messages and store the potential answers and their scores in probability in the empty dictionary
def check_all_messages(message):
    highest_prob_list = {}
    
    # will update the dictionary (highest_prob_list) with the probability computed but it requires conditions
    # conditions - bot response, list of words, single response, required words
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        center = (bot_response, tuple(list_of_words), single_response, tuple(required_words))
        highest_prob_list[center] = message_probability(message, list_of_words, single_response, required_words)
    
    # converts raw data from csv file in each row to become more usable
    responses = []
    for row in rows:
        responses.append({
            "message": row['message'],
            "list_of_words": eval(row['list_of_words']) if 'list_of_words' in row and row['list_of_words'] else [],
            "single_response": True if row["single_response"] == "True" else False,
            "required_words": eval(row['required_words']) if 'required_words' in row and row['required_words'] else [],
            })
    
    # extracts information from the message, list of words, single response, required words
    for resp in responses:
        response(resp["message"], resp["list_of_words"], resp["single_response"], resp["required_words"])
    
    # computes for the best match
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

     # if the probability for the best match is greater than 200 it will return a proper response
    # if it is greater than 1 and less than 200 (between 1 and 200) it will respond with "sorry but..."
    # if it is less than or equal to 1 it will respond with "i'm truly sorry..."
    if highest_prob_list[best_match] > 200:
        return best_match[0]
    elif highest_prob_list[best_match] > 1 and highest_prob_list[best_match] < 200: 
        return "Sorry but, I'm not quite sure about that. I'll update you once I know more, my friend."
    else:
        return "I'm truly sorry about that. I don't know that one, my friend."

# takes user's input and converts into lowercase and checks the response and returns the appropriate one
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# handles the input of the user and returns the appropriate response (JSON)
# JSON - JavaScript Object Notation used to transmit data between server and web application (store & exchange)
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

# provides instructions when someone visits the page and shows the webpage in "final.html"
@app.route('/')
def index():
    return render_template('finals.html', )

# ensures that the flask will only start if you run the script
if __name__ == '__main__':
    app.run(debug=True)