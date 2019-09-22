from firebase_utils import firebase_message, firebase_initialise
import sys
from os import environ
import datetime

series_title = environ.get('sonarr_series_title')
season_number = environ.get('sonarr_release_seasonnumber')
episode_number = environ.get('sonarr_release_episodenumbers')
episode_title = environ.get('sonarr_release_episodetitles')
release_quality = environ.get('sonarr_release_quality')

firebase_initialise.initialise_admin()

# Send notification
title = "Sonarr - Episode Grabbed"
body = "%s - %sx%s - %s [%s]" % (series_title, season_number, episode_number, episode_title, release_quality)
category = "tv"
date_time = datetime.datetime.now()
notification = firebase_message.Notification(title, body, category, date_time)
firebase_message.send_and_save(notification)