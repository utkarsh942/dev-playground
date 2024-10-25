class PasswordChecker:
    def __init__(self):
        self.min_length = 8
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def check_strength(self, password):
        """
        Bug: The function doesn't properly check for the presence of numbers
        It only checks if there's a digit in the first position
        """
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= self.min_length:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
        
        # Check for uppercase
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Password should contain at least one uppercase letter")
        
        # Bug: Incorrect number checking
        if password[0].isdigit():  # Bug is here - only checks first character
            score += 1
        else:
            feedback.append("Password should contain at least one number")
        
        # Check for special characters
        if any(c in self.special_chars for c in password):
            score += 1
        else:
            feedback.append("Password should contain at least one special character")
        
        strength = {
            0: "Very Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong"
        }
        
        return {
            "score": score,
            "strength": strength[score],
            "feedback": feedback
        }

# Usage Example
if __name__ == "__main__":
    checker = PasswordChecker()
    test_password = "2weakpass"
    result = checker.check_strength(test_password)
    print(f"Password Strength: {result['strength']}")
    print("Feedback:", "\n".join(result['feedback']))