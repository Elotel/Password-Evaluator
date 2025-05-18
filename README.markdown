# Password Strength Evaluator

This Python script evaluates the strength of a user-provided password and classifies it as **Weak**, **Moderate**, or **Strong** based on specific criteria. If the password is Weak or Moderate, it generates a strong password sample to help users improve their password security.

## Features

- **Password Evaluation**:
  - Assesses passwords based on:
    - **Length**: <8 characters (0 points), 8-12 characters (1 point), >12 characters (2 points)
    - **Character Types**: Presence of lowercase letters, uppercase letters, numbers, and special characters (1 point each)
  - Assigns a score out of 6 and classifies the password:
    - **Weak**: Score ≤ 2
    - **Moderate**: Score 3-4
    - **Strong**: Score ≥ 5
  - Provides detailed feedback on how to improve the password.

- **Strong Password Generation**:
  - If the password is Weak or Moderate, generates a 14-character strong password that includes:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least one special character
  - Ensures the generated password is randomized and achieves a Strong rating.

- **User-Friendly Interface**:
  - Prompts users to input passwords.
  - Displays strength, score, feedback, and (if applicable) a suggested strong password.
  - Allows continuous testing until the user types 'quit'.

## Requirements

- Python 3.x
- Standard libraries: `re`, `random`, `string`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Elotel/password-evaluator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-evaluator
   ```

## Usage

1. Run the script:
   ```bash
   python password_evaluator.py
   ```
2. Enter a password when prompted or type 'quit' to exit.
3. View the evaluation results, including strength, score, and feedback.
4. If the password is Weak or Moderate, a strong password sample will be generated and evaluated.

### Example Output

```
Enter a password to evaluate (or 'quit' to exit): pass
Password Strength Evaluation:
Strength: Weak
Score: 1/6
Feedback:
- Password is too short (minimum 8 characters).
- Contains lowercase letters.
- Add uppercase letters for better strength.
- Add numbers for better strength.
- Add special characters for better strength.

Suggested Strong Password:
kJ#9mP2nL5x@Qz
Generated Password Strength: Strong
Generated Password Score: 6/6

Enter a password to evaluate (or 'quit' to exit): quit
Exiting password evaluator.
```

## File Structure

- `password_evaluator.py`: The main Python script containing the password evaluation and generation logic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License

Author: Elotel-Milano
