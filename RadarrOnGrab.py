from firebase_utils import firebase_message, firebase_initialise
import sys
from os import environ

movie_title = environ.get('radarr_movie_title')
release_quality = environ.get('radarr_release_quality')

firebase_initialise.initialise_admin()

firebase_message.send_firebase("Radarr - Movie Grabbed", "%s [%s]" % (movie_title, release_quality))