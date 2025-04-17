# generate_secret.py

import secrets

# Generate a 32-byte URL-safe token
secret_key = secrets.token_urlsafe(32)

# Print the secret key
print(secret_key)
