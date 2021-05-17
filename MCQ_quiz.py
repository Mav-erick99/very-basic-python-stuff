from question import question

question_prompts = (
    "what color is an apple ? \n a) red\n b) purprle\n c) black\n\n",
    "what color is a banana ? \n a) grey\n b) pink\n c) yellow\n\n",
    "what color is an avacado ? \n a) magenta\n b) blue\n c) green\n\n"
)

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("you got " + str(score) + " out of " + str(len(questions)) + " right")
run_test(questions)