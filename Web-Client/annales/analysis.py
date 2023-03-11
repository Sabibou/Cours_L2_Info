# I got a file called "rep.md" with questions and answers

# Questions are in the form of:
# > **Question X**

# List of answers in a dictionary, and count occurences

with open("rep.md", "r") as f:
    lines = f.readlines()

    answers = {}

    for line in lines:
        if line.startswith("> **"):
            line = line[4:-3]
            if line in answers:
                answers[line] += 1
            else:
                answers[line] = 1
    
    # Rank answers by occurences
    answers = sorted(answers.items(), key=lambda x: x[1], reverse=True)

    # # Print answers in file (with a nice format)
    # with open("answers.txt", "w") as f:
    #     for answer in answers:
    #         f.write(f"- [{answer[1]}] \t {answer[0]}\n\n")
    # print numbers of answers
    print(sum([x[1] for x in answers]))