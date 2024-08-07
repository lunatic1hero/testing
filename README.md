import requests
import bencodepy
import hashlib

def get_torrent_info(info_hash):
    url = f'https://your-torrent-metadata-service/{info_hash}'
    response = requests.get(url)
    
    if response.status_code == 200:
        torrent_data = bencodepy.decode(response.content)
        info_dict = torrent_data[b'info']
        
        if b'name' in info_dict:
            file_name = info_dict[b'name'].decode('utf-8')
            print(f"File Name: {file_name}")
        else:
            print("No file name found in torrent info.")
    else:
        print(f"Failed to fetch torrent metadata for info_hash {info_hash}")

# Example usage:
info_hash = 'your_info_hash_here'  # Replace with the actual info_hash from Wireshark
get_torrent_info(info_hash)

