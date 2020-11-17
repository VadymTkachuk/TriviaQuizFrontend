import requests
import json
import html
import random

def main():

    print("\nThis is a simple interactive quiz based on trivia questions.\n")
    
    url = "https://opentdb.com/api.php?amount=1"
    endGame = ""
    score_correct = 0
    score_incorrect = 0

    while endGame != "quit":
        r = requests.get(url)
        if r.status_code != 200:
            endGame = input("There was a problem retrieving the question. \n Press enter to try again or type quit to exit.")
        else:
            data = json.loads(r.text)
            question = data['results'][0]['question']
            answers = data['results'][0]['incorrect_answers']
            correct_answer = data['results'][0]['correct_answer']
            answers.append(correct_answer)
            random.shuffle(answers)

            answer_number = 1
            print(html.unescape(question) + "\n")
            for answer in answers:
                print(str(answer_number) + " - " + html.unescape(answer))
                answer_number += 1

            valid_answer = False
            while valid_answer == False:
                user_answer = input("\nType the number of the correct answer: ")
                try: 
                    user_answer = int(user_answer)
                    if user_answer <= 0 or user_answer > len(answers):
                        print("Invalid answer. Please, try again.")
                    else:
                        valid_answer = True
                except:
                    print("Invalid answer. Use numbers only!")
            user_answer = answers[user_answer - 1] # Array starts with 0!    
            
            if correct_answer == user_answer:
                print("\nCongratulations! You answered correctly. The right answer is " + correct_answer + "!")
                score_correct += 1
            else:
                print("\nSorry, your answer is incorrect. The correct answer is " + correct_answer + "!")
                score_incorrect += 1
            endGame = input("\nType enter to continue or type quit to exit.\n")
            
    print("\nYour score: " + str(score_correct) + " of correct answers and " + str(score_incorrect) + " of incorrect answers.")
    return

if __name__ == "__main__":
    main()
