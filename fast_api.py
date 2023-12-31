from fastapi import FastAPI

app = FastAPI()

def count_vowels_consonants(text: str):
    vowels = 0
    consonants = 0
    words = len(text.split())
    vowel_set = set("aeiouAEIOU")

    for char in text:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    return {"vowels": vowels, "consonants": consonants, "words": words}

@app.get("/analyze/{text}")
def analyze_text(text: str):
    result = count_vowels_consonants(text)
    return result
