# Password Complexity Analyzer

A Python-based script to evaluate the complexity of a password and provide actionable feedback to improve its strength. This tool helps ensure better security practices by guiding users to create stronger passwords.

## Features

- **Length Check**: Encourages passwords of at least 8 characters, with optimal security at 12+ characters.
- **Character Diversity**:
  - Checks for uppercase and lowercase letters.
  - Ensures inclusion of numbers and special characters.
- **Common Weakness Detection**:
  - Identifies common, easily guessable passwords (e.g., "123456", "password").
  - Flags repeated characters or patterns.
- **Scoring and Feedback**: Rates password strength as "Weak," "Moderate," or "Strong" and provides tips for improvement.

## How It Works

1. Input a password to analyze.
2. The script evaluates the password based on:
   - Length
   - Use of uppercase and lowercase letters
   - Inclusion of digits and special characters
   - Avoidance of common patterns or weak passwords
3. The script returns:
   - A strength rating (Weak, Moderate, Strong)
   - A score out of 6
   - Suggestions to improve password security

## Requirements

- Python 3.x
- No additional libraries are required.

## Usage

1. Clone or download this repository.
	```bash
	git clone https://github.com/PavinDas/PasswordChecker
	```
2. Run the script:

    ```bash
    python3 passwordChecker.py
    ```

3. Enter the password you want to analyze when prompted.
4. Review the strength rating, score, and feedback provided.

## Example Output

```plaintext
Enter a password to analyze: Example@123

Password Strength:  Strong
Score:  6 / 6
```

## If Improvements Needed

```
Enter a password to analyze: weakpass

Password Strength:  Weak
Score:  2 / 6
Suggestions to improve your password:
 - Add at least one uppercase letter.
 - Include at least one special character (e.g., !, @, #).
 - Use a longer password with at least 8 characters.


```
