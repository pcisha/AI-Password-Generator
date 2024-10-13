import random
import string

## @author: prachi.shah
## @date: 9-10-2024

# Define character sets for different levels
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()-_+="  # Common symbols for added security


def get_character_pool(complexity: str) -> str:
    """
    Returns the character pool based on the complexity level.

    Args:
        complexity (str): Complexity level, can be 'easy', 'medium', 'hard', or 'extra-hard'.

    Returns:
        str: Character pool to select characters from based on complexity.

    Raises:
        ValueError: If an invalid complexity level is provided.
    """
    if complexity == "easy":
        return LOWERCASE_LETTERS
    elif complexity == "medium":
        return LOWERCASE_LETTERS + UPPERCASE_LETTERS
    elif complexity == "hard":
        return LOWERCASE_LETTERS + UPPERCASE_LETTERS + NUMBERS + SYMBOLS
    elif complexity == "extra-hard":
        return LOWERCASE_LETTERS + NUMBERS + SYMBOLS + UPPERCASE_LETTERS
    else:
        raise ValueError("Invalid complexity level. Choose from 'easy', 'medium', 'hard', or 'extra-hard'.")


def ensure_required_characters_hard(password: list, length: int, complexity: str) -> None:
    """
    Ensures that the password has at least one character from each required set in 'hard' complexity.

    Args:
        password (list): The list of characters forming the password.
        length (int): Length of the password.
        complexity (str): Complexity level of the password.
    """
    if complexity == "hard":
        required_char_types = [LOWERCASE_LETTERS, UPPERCASE_LETTERS, NUMBERS, SYMBOLS]
        for char_set in required_char_types:
            if not any(char in char_set for char in password):
                password[random.randint(0, length - 1)] = random.choice(char_set)


def ensure_required_characters_extra_hard(password: list, length: int, complexity: str) -> None:
    """
    Ensures that the password has at least one character from each required set in 'extra-hard' complexity.

    Args:
        password (list): The list of characters forming the password.
        length (int): Length of the password.
        complexity (str): Complexity level of the password.
    """
    if complexity == "extra-hard":
        required_char_types = [LOWERCASE_LETTERS, NUMBERS, SYMBOLS, UPPERCASE_LETTERS]
        for char_set in required_char_types:
            if not any(char in char_set for char in password):
                password[random.randint(0, length - 1)] = random.choice(char_set)


def generate_password(length: int, complexity: str = "medium") -> str:
    """
    Generates a password based on specified length and complexity.

    Args:
        length (int): The length of the password.
        complexity (str): Complexity level: "easy", "medium", "hard", or "extra-hard".

    Returns:
        str: A secure password of the desired length and complexity.

    Raises:
        ValueError: If length is less than 6 or if an invalid complexity is provided.
    """
    if length < 6:
        raise ValueError("Password length should be at least 6 for security.")

    character_pool = get_character_pool(complexity)
    password = []

    while len(password) < length:
        next_char = random.choice(character_pool)

        # Avoid consecutive identical characters
        if len(password) > 0 and password[-1] == next_char:
            continue

        # Avoid consecutive sequences like "aaa" or "111"
        if len(password) >= 2 and password[-2] == password[-1] == next_char:
            continue

        password.append(next_char)

    # Ensure complexity requirements in 'hard' mode
    ensure_required_characters_hard(password, length, complexity)

    # Ensure complexity requirements in 'extra-hard' mode
    ensure_required_characters_extra_hard(password, length, complexity)

    return ''.join(password)


# Password Generator
if __name__ == "__main__":
    try:
        print("Passwords generated are below:")
        print("Easy:", generate_password(10, "easy"))
        print("Medium:", generate_password(12, "medium"))
        print("Hard:", generate_password(14, "hard"))
        print("Extra Hard:", generate_password(20, "extra-hard"))
    except ValueError as e:
        print("Error:", e)
