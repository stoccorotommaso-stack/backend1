from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# Creiamo l'istanza della nostra applicazione
app = FastAPI()

# CONFIGURAZIONE CORS: Permette al Front-end (GitHub Pages) di comunicare con questo server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In futuro potrai mettere l'URL specifico della tua GitHub Page
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Una lista di citazioni per il nostro esempio
quotes = [
    "Non funziona? Hai provato a spegnere e riaccendere?",
    "Il codice non mente, i commenti a volte sì.",
    "Prima risolvi il problema, poi scrivi il codice.",
    "Un bug è solo una feature che non ha ancora trovato il suo scopo.",
    "Il miglior modo di predire il futuro è implementarlo.",
    "Software is eating the world."
]

# Rotta principale (Home) per capire se il server è vivo
@app.get("/")
def read_root():
    return {"status": "online", "message": "Benvenuto nell'API di test!"}

# Rotta che restituisce una citazione casuale
@app.get("/quote")
def get_quote():
    return {"message": random.choice(quotes)}
