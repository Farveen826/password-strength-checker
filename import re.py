import re

def check_password(password: str):
    """Return (strength_score, suggestions_list)."""
    strength = 0
    suggestions = []

    # length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Increase length to at least 8 characters (12+ recommended)")

    # uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    # lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    # digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add at least one number")

    # special characters
    if re.search(r"[@$!%*?&#\-_+=]", password):
        strength += 1
    else:
        suggestions.append("Add at least one special character like @ $ ! % * ? & # - _ + =")

    return strength, suggestions

def rating_from_score(score: int):
    if score <= 2:
        return "Weak"
    if 3 <= score <= 4:
        return "Medium"
    return "Strong"

def main():
    pw = input("Enter a password to check: ")
    score, suggestions = check_password(pw)
    rating = rating_from_score(score)

    print("\nPassword rating:", rating)
    print("Score:", score, "/ 6")
    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("-", s)
    else:
        print("\nGood job! Your password meets common strength criteria.")

if __name__ == "__main__":
    main()
