import re

def check_password_complexity(password):
    complexity_score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        complexity_score += 2
    elif len(password) >= 8:
        complexity_score += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        complexity_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        complexity_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        complexity_score += 1
    else:
        feedback.append("Include at least one number.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        complexity_score += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #).")
    
    # Check for common weaknesses
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "welcome"]
    if password.lower() in common_passwords or re.match(r"(.)\1{2,}", password):
        feedback.append("Avoid common passwords or repeated characters.")
    
    # Provide final feedback
    if complexity_score >= 6:
        strength = "Strong"
    elif complexity_score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return {"strength": strength, "score": complexity_score, "feedback": feedback}


# Example usage
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    result = check_password_complexity(password)
    print("\nPassword Strength: ", result["strength"])
    print("Score: ", result["score"], "/ 6")
    if result["feedback"]:
        print("Suggestions to improve your password:")
        for suggestion in result["feedback"]:
            print(" -", suggestion)
