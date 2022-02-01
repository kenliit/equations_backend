import random


'''
questions format:
0 - question id
1 - question
2 - answers
3 - correct answer
'''
questions = (
    (0, "2 + 2 * 4 =", [16, 10, 8, 12], 1),
    (1, "3 * 5 + 8 =", [23, 18, 20, 26], 0),
    (2, "9 / 9 * 2 =", [15, 18, 36, 2], 3),
    (3, "3 + 6 + 18 + 24 =", [44, 51, 80, 66], 1)
)


def question_picker():
    ran_int = random.randint(0, len(questions)-1)
    return {
        "id": ran_int,
        "question": questions[ran_int][1],
        "choices": questions[ran_int][2]
    }


def verify_answer(question_id, answer):
    if not isinstance(question_id, int) or question_id < 0 or question_id > len(questions):
        return {
            "error": "Question id is invalid!"
        }
    if not isinstance(answer, int) or answer not in questions[question_id][2]:
        return {
            "error": "Answer is not exist!"
        }
    if questions[question_id][2][questions[question_id][3]] == answer:
        return {
            "yes": "Your answer is correct."
        }
    else:
        return {
            "no": "Answer is wrong."
        }
