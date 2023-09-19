!apt install python3-libtorrent
!pip install mega.py
import libtorrent as lt
import os
import shutil
import sys
import time
from google.colab import drive
from mega.mega import Mega

# PROVIDE TORRENT MAGNET
magnet = ""

drive.mount('/content/drive')
torrent_dir = f'drive/MyDrive/Torrent'

ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
params = lt.parse_magnet_uri(magnet)
params.save_path = torrent_dir
handle = ses.add_torrent(params)
s = handle.status()


print(f'STARTING {s.name}...')
while not s.is_seeding:
    s = handle.status()
    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
        s.num_peers, s.state), end=' ')
    # alerts = ses.pop_alerts()
    # for a in alerts:
    #     if a.category() & lt.alert.category_t.error_notification:
    #         print(a)
    sys.stdout.flush()
    time.sleep(1)
torrent_name = s.name
print(f'{s.name} COMPLETED')

print('CONVERTING TORRENT INTO ZIP...')
torrent_zip_path = f'{torrent_dir}/{torrent_name}'
shutil.make_archive(base_name=torrent_zip_path,
                    format='zip',
                    root_dir=f'{torrent_dir}/{torrent_name}')
print('CONVERSION SUCCESSFUL')

print('LOGGING INTO MegaCloud...')
#PROVIDE EMAIL AND PASSWORD TO LOG INTO MEGA CLOUD
email = ''
password = ''
mega = Mega()
m = mega.login(email, password)
print('LOGGED IN SUCCESSFULLY')

print(f'UPLOADING TO MEGA CLOUD')
mega_dir = f'Torrent/{torrent_name}'

if m.find(mega_dir) is None:
  m.create_folder(mega_dir)

mega_dir = m.find(mega_dir)
m.upload(f'{torrent_zip_path}.zip', dest=mega_dir[0])
print(f'{torrent_name} UPLOADED SUCCESSFULLY')

shutil.rmtree(f'{torrent_dir}/{torrent_name}')
os.remove(f'{torrent_dir}/{torrent_name}.zip')
