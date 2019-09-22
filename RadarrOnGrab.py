from firebase_utils import firebase_message, firebase_initialise
import sys
from os import environ
import datetime

movie_title = environ.get('radarr_movie_title')
release_quality = environ.get('radarr_release_quality')

firebase_initialise.initialise_admin()

# Send notification
title = "Radarr - Movie grabbed"
body = "%s [%s]" % (movie_title, release_quality)
category = "movie"
date_time = datetime.datetime.now()
notification = firebase_message.Notification(title, body, category, date_time)
firebase_message.send_and_save(notification)