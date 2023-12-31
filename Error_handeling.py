from fastapi import FastAPI, HTTPException

app = FastAPI()
@app.get("/analyze/{text}")
def analyze_text(text: str):
    try:
        if not text.isalpha():
            raise HTTPException(status_code=400, detail=" Text should only contain alphabetic characters ")

        if any(char.isdigit() for char in text):
            raise HTTPException(status_code=400, detail="Text should not contain numeric characters ")
        
        vowels = sum(1 for char in text if char.lower() in "aeiou")
        consonants = len(text) - vowels
        words = len(text.split())

        return {"vowels": vowels, "consonants": consonants, "words": words}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
