"""
Generates a randomized order character look up string
"""
import random

# All available characters to use to generate a session id
characters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"

# Converts string into list of each individual character
characters = [*characters]

# Randomly shuffles the list in place
random.shuffle(characters)

# Generates new random look up string
print("".join(characters))
