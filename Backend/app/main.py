import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from fastapi import FastAPI


app = FastAPI()

#Credenciales de Spotify

@app.get("/")
def inicio():
    return "Hola"