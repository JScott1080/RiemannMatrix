# src/python/personality.py

from __init__ import load_personalities

def load_personality(persona):
    personalities = load_personalities()
    return personalities.get(persona, {})

if __name__ == "__main__":
    # Example usage (for illustration purposes)
    persona = 'AMY'
    personality_traits = load_personality(persona)
    print(f"Personality traits for {persona}: {personality_traits}")
