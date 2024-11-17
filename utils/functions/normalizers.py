# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from unidecode import unidecode


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ NORMALIZE EMAIL
# └─────────────────────────────────────────────────────────────────────────────────────


def normalize_email(email: str) -> str:
    """Normalizes an email address"""

    # Remove special characters from the email
    email = unidecode(email)

    # Lowercase the email
    email = email.lower()

    # Remove spaces from the email
    email = email.replace(" ", "")

    # Strip the email
    email = email.strip()

    # Return normalized email
    return email
