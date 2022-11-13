def main():
    print("""
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    """)
    
    question_array = [
    """1. I feel that I am a person of worth, at least on an equal plane with others.""",
    """2. I feel that I have a number of good qualities.""",
    """3. All in all, I am inclined to feel that I am a failure.""",
    """4. I am able to do things as well as most other people.""",
    """5. I feel I do not have much to be proud of.""",
    """6. I take a positive attitude toward myself.""",
    """7. On the whole, I am satisfied with myself.""",
    """8. I wish I could have more respect for myself.""",
    """9. I certainly feel useless at times.""",
    """10. At times I think I am no good at all."""]
    total_score = 0
    for i in range(len(question_array)):
        if (i + 1 == 1) or (i + 1 == 2) or (i + 1 == 4) or (i +1 == 6) or (i + 1 == 7):
            print (question_array[i])
            total_score += pos_score_calc(input('Enter D, d, a, or A: '))
        
        elif (i + 1 == 3) or (i + 1 == 5) or (i + 1 == 8) or (i + 1 == 9) or (i + 1 == 10):
            print (question_array[i])
            total_score += neg_score_calc(input('Enter D, d, a, or A: '))
    
    print(f"Your score is {total_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

# Pos Score Questions (numbers 1, 2, 4, 6, 7)
def pos_score_calc(letter):
    if letter == 'D':
        return 0
    elif letter == 'd':
        return 1
    elif letter == 'a':
        return 2
    elif letter == 'A':
        return 3

# Neg Score Questions (numbers 3, 5, 8, 9, 10)
def neg_score_calc(letter):
    if letter == 'D':
        return 3
    elif letter == 'd':
        return 2
    elif letter == 'a':
        return 1
    elif letter == 'A':
        return 0
        
main()