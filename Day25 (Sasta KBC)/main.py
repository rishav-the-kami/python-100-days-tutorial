# Im not gonna add 15 questions ;-;

price = 0

question_contents = [
    {
        "question": "Q1) What does \"Kono Dio Da\" mean?",
        "options": ["A) Good Grief", "B) THATS ME, DIO!!", "C) I don't know", "D) Shut up"],
        "answer": "B",
        "price": 1000
    },
    {
        "question": "Q2) What does \"Yare Yare\" mean?",
        "options": ["A) Good Grief", "B) THATS ME, DIO!!", "C) I don't know", "D) Shut up"],
        "answer": "A",
        "price": 2000
    },
    {
        "question": "Q3) Capital of Thailand",
        "options": ["A) Bangdick", "B) Bangpusi", "C) Bangkok", "D) Bangcock"],
        "answer": "C",
        "price": 3000
    }
]

def print_options(question):
    for i in enumerate(question["options"]):
        if(i[0] == 2):
            print()
            print(i[1], end="\t")
        else:
            print(i[1], end="\t")
    print()


def check_correct(question, choice):
    global price

    if(i["answer"] == choice.upper()):
        price = question["price"]
        print(f"Correct answer: you now have ${price}")
        return True
    else:
        print(f"Incorrect answer. You are leaving with ${price}")
        return False


for i in question_contents:
    print(i["question"])
    print_options(i)
    choice = input("Enter A, B, C or D: ")
    is_over = check_correct(i, choice)
    if not is_over:
        break


if price == 3000:
    print("You Won weeeeeee")