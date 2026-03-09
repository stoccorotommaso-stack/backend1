from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Configura il CORS per permettere a GitHub Pages di comunicare con Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In produzione metterai l'indirizzo della tua GitHub Page
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    "Non funziona? Hai provato a spegnere e riaccendere?",
    "Il codice non mente, i commenti a volte sì.",
    "Prima risolvi il problema, poi scrivi il codice.",
    "Un bug è solo una feature che non ha ancora trovato il suo scopo."
]

@get("/")
def read_root():
    return {"status": "online"}

@get("/quote")
def get_quote():
    return {"message": random.choice(quotes)}
