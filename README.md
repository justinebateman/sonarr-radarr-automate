# sonarr-radarr-automate
Custom scripts for [Sonarr](https://sonarr.tv/) and [Radarr](https://radarr.video/) grabs and post processing

Uses https://github.com/justinebateman/firebase_utils to send Firebase Cloud Messaging push notifications to an Android app

Uses https://github.com/mdhiggins/sickbeard_mp4_automator to convert files to mp4 after download

Notifications are sent:
- On grab
- When file conversion begins
- When file conversion is complete

Notifications are stored in a Firebase Cloud Firestore collection with a date timestamp and a category eg. "movie", "tv" so they can be queried and filtered. This allows for display of the full notification history if required