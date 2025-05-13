import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0

    # Counts how many words are present in each predefined message
    # Included words that is familiar to the bot, but is not part of the trivial facts
    main_words = ['multiple', 'IoT', 'device', 'controller', 'understand', 'context', 'adapt', 'interepret', 'language', 'integrate', 'siri', 'unique', 'accents', 'different', 'human', 'conversation', 'languages', 'it']
    for word in user_message:
        if word in recognised_words:
            message_certainty += 100
        elif word in main_words:
            message_certainty += 2

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words) + len(main_words))

    # Checks that the required words are in the string
    has_required_words = all(word in user_message for word in required_words) 

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}
    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Introductory responses -------------------------------------------------------------------------------------------------------
    response('It\'s nice to see you again, my friend! What can I do for you?', ['hello', 'sup', 'hi', 'yo'], single_response=True)
    response('It\'s a good thing I know that one. Shoot me some questions, my friend!', ['want', 'know', 'IoT device controller'], single_response=True)
    response('Welcome! You can ask me anytime you want.', ['thank you', 'thanks'], single_response=True)  
    response('Bye! Stay safe and healthy, my friend!', ['bye', 'goodbye'], single_response=True)  
    
    # Longer responses (Trivial facts) ---------------------------------------------------------------------------------------------
    response(long.R_IOT, [' provide', 'overview', 'explain'], single_response=True)
    response(long.R_WHERE, ['where', 'home'], single_response=True)
    response(long.R_BENEFIT, ['using', 'benefit', 'gain'], single_response=True)
    response(long.R_DEVICES, ['devices', 'gadgets', 'gadget', 'control', 'monitor'], single_response=True)
    response(long.R_STUDENT, ['alleviate', 'stress', 'student'], single_response=True)
    response(long.R_WORKING, ['chores', 'asisst', 'working', 'homework'], single_response=True)
    response(long.R_NOT, ['easy', 'old'], required_words=['technology', 'knowledgeable'])
    response(long.R_PRIORITIES, ['manage', 'managing', 'priorities', 'tasks'], single_response=True)
    response(long.R_COMMUNICATION, ['problems', 'safe', 'communication', 'information'], single_response=True)
    response(long.R_CUSTOMIZE, ['change', 'changes', 'customize', 'preference'], single_response=True)
    response(long.R_BILL, ['cost', 'increase', 'electricicty', 'bill'], single_response=True)
    response(long.R_EYES, ['affect', 'eyes', 'strain'], single_response=True )

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    if highest_prob_list[best_match] > 200:
        return best_match
    elif highest_prob_list[best_match] > 1 and highest_prob_list[best_match] < 200: 
        return "Sorry but, I'm not quite sure about that. I'll update you once I know more, my friend."
    else:
        return "I'm truly sorry about that. I don't know that one, my friend."


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))