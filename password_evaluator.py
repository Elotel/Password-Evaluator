import re
import random
import string

def evaluate_password(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    length = len(password)
    if length < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    elif length >= 8 and length <= 12:
        score += 1
        feedback.append("Good length (8-12 characters).")
    else:
        score += 2
        feedback.append("Excellent length (>12 characters).")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Add lowercase letters for better strength.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Add uppercase letters for better strength.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Add numbers for better strength.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Add special characters for better strength.")

    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def generate_ideal_password():
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*(),.?:{}|<>"
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest to reach length 14
    all_chars = lowercase + uppercase + digits + special
    for _ in range(10):  # 14 - 4 = 10 more characters
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

def main():
    while True:
        password = input("Enter a password to evaluate (or 'quit' to exit): ")
        if password.lower() == 'quit':
            print("Exiting password evaluator.")
            break
        
        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        result = evaluate_password(password)
        print("\nPassword Strength Evaluation:")
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}/6")
        print("Feedback:")
        for comment in result['feedback']:
            print(f"- {comment}")
        
        # Generate ideal password if strength is Weak or Moderate
        if result['strength'] in ["Weak", "Moderate"]:
            ideal_password = generate_ideal_password()
            print("\nSuggested Strong Password:")
            print(ideal_password)
            # Evaluate the generated password to confirm strength
            ideal_result = evaluate_password(ideal_password)
            print(f"Generated Password Strength: {ideal_result['strength']}")
            print(f"Generated Password Score: {ideal_result['score']}/6")
        
        print()

if __name__ == "__main__":
    main()