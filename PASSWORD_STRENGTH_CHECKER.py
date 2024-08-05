import re

def calculate_password_strength(password):
    length_score = len(password) >= 8
    digit_score = bool(re.search(r"\d", password))
    lowercase_score = bool(re.search(r"[a-z]", password))
    uppercase_score = bool(re.search(r"[A-Z]", password))
    special_char_score = bool(re.search(r"[@$!%*_?&#]", password))

    scores = [length_score, digit_score, lowercase_score, uppercase_score, special_char_score]
    strength_score = sum(scores)
    
    feedback = [
        "Password must be at least 8 characters long.",
        "Password must contain at least one digit.",
        "Password must contain at least one lowercase letter.",
        "Password must contain at least one uppercase letter.",
        "Password must contain at least one special character (@$!%*_?&#)."
    ]

    for i, score in enumerate(scores):
        if not score:
            print(feedback[i])

    return strength_score

def main():
    while True:
        password = input("Enter your password: ")
        strength = calculate_password_strength(password)
        
        if strength <= 2:
            print("Weak password. Please try again.")
        elif 3 <= strength <= 4:
            print("Moderate password. Please try again.")
        else:
            print("Strong password. Password accepted.")
            break

if __name__ == "__main__":
    main()
