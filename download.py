import os
import urllib.request

# Function to download a model
def download(url, output_path):
    urllib.request.urlretrieve(url, output_path)
    print(f"Downloaded to {output_path}")

# URL of the model to download
model_url = 'https://zenodo.org/record/4034264/files/CRNN_note_F1%3D0.9677_pedal_F1%3D0.9186.pth?download=1'
model_output_path = 'server/model/CRNN_note_F1=0.9677_pedal_F1=0.9186.pth'

# URL of sf2 soundfont
sf2_url = 'https://drive.usercontent.google.com/download?id=1JZhVj0SDoz-JQ72QFbnmoIIEk4kUjcSR&export=download'
sf2_output_path = 'server/resources/GeneralUser-GS.sf2'

def check_exists(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0

# Download the model
if not check_exists(model_output_path):
    download(model_url, model_output_path)
if not check_exists(sf2_output_path):
    download(sf2_url, sf2_output_path)