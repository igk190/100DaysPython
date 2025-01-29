class QuizBrain():

    def __init__(self, q_list): # question bank will go into here
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_number_to_display = self.question_number + 1
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{q_number_to_display}: {current_question.text} True/False?").lower()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}\n")

    def get_final_score(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{len(self.question_list)}")








# When we initialize one attribute with a default value, we don't need to add an input to the Class

"""-- Learnings --
1. Whatever index I show a question at, I add +1 to what's printed to the user (because index starts at 0).
2. Angela defined a variable to store the current Q. This makes the code cleaner to read.
3. In next_question() method, we get the current question, and store it in a var. After that, we're safe to
add 1 to self.question_number.
4. With the still_has_questions() method, I checked if list > questions. If true, return false. Otherwise, return true.
Then I added another While-loop with "should_continue" set to True. But we"re already using a boolean in the method.
No need to do double the work. Switching what we're checking so we get True as long as there are Qs suffices.
5. We can simplify the still_has_question() method by ONLY returning the expression.
"""