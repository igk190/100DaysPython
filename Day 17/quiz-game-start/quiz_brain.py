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


# Learnings: 1. Whatever index I show a question at, I add +1 to what's printed
# 2. angela defined var to store the current Q. Which makes code cleaner to read.
#3. in next_question method, we get the current question and store it in a var. AFter that, we're safe to
# add 1 to self.question_number anyway
#4 with the still_has_questions method, I checked if list > questions, if true, return false. Otherwise, return true.
# and added another While loop should continue that I set to true. But we"re alrady using a boolean in the method.
# no need to do double the work. Switching what we're checking so we get true as long as there are Qs suffices.
#5. we can simplify the still_has_question method by JUST returning the expression