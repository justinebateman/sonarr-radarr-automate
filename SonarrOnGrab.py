from firebase_utils import firebase_message, firebase_initialise
import sys
from os import environ

series_title = environ.get('sonarr_series_title')
season_number = environ.get('sonarr_release_seasonnumber')
episode_number = environ.get('sonarr_release_episodenumbers')
episode_title = environ.get('sonarr_release_episodetitles')
release_quality = environ.get('sonarr_release_quality')

firebase_initialise.initialise_admin()

firebase_message.send_firebase("Sonarr - Episode Grabbed", "%s - %sx%s - %s [%s]" % (series_title, season_number, episode_number, episode_title, release_quality))