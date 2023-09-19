# Torrent to Mega Cloud Uploader

This Python script downloads torrents, saves them to Google Drive, compresses them into a zip file, and uploads them to Mega Cloud. It utilizes the libtorrent library to manage torrents, the Google Colab environment for cloud storage, and the mega.py library for interacting with Mega Cloud.

## Prerequisites

Before using this script, ensure you have the following prerequisites in place:

- Google Colab account for cloud storage.
- Required Python libraries installed in your environment:
  - libtorrent
  - mega.py

You can install these libraries using the following commands:

```bash
!apt install python3-libtorrent
!pip install mega.py
```

# Usage

1. Open Google Colab and create a new notebook or use an existing one.
2. Copy and paste the code from the provided script into a code cell in your Colab notebook.
3. Replace the `magnet` variable with the magnet link of the torrent you want to download.
5. Provide email and password to log into mega cloud.
4. Mount your Google Drive by running the following code in another Colab cell:

```python
from google.colab import drive
drive.mount('/content/drive')
```

1. Run the code cell with your script. It will download the torrent, save it to your Google Drive, compress it into a zip file, and upload it to Mega Cloud.
2. You will be prompted to log in to your Mega Cloud account. Provide your email and password when prompted.
3. Once logged in, the script will upload the zip file to Mega Cloud and display a success message.
4. After the upload is complete, the script will clean up by deleting the original torrent file and the zip file from your Google Drive.

## Important Notes

- This script is designed to run in a Google Colab environment. Ensure you have sufficient storage space on Google Drive for downloaded torrents.
- Mega Cloud login credentials are required. You will need to provide your Mega Cloud email and password.
- Please use this script responsibly and ensure that you have the necessary rights and permissions to download and share the content you are working with.

## Acknowledgments
- [libtorrent](https://github.com/arvidn/libtorrent)
- [mega.py](https://github.com/odwyersoftware/mega.py)