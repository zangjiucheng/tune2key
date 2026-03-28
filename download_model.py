import os
import sys
import time
import urllib.request

def _format_size(num_bytes):
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f}{unit}"
        size /= 1024


def _make_progress_hook(start_time):
    bar_width = 30

    def _hook(block_count, block_size, total_size):
        downloaded = block_count * block_size
        elapsed = max(time.time() - start_time, 1e-6)
        speed = downloaded / elapsed

        if total_size > 0:
            downloaded = min(downloaded, total_size)
            progress = downloaded / total_size
            filled = int(bar_width * progress)
            bar = "=" * filled + "-" * (bar_width - filled)
            percent = int(progress * 100)
            message = (
                f"\r[{bar}] {percent:3d}% "
                f"{_format_size(downloaded)}/{_format_size(total_size)} "
                f"{_format_size(speed)}/s"
            )
        else:
            message = (
                f"\rDownloaded {_format_size(downloaded)} "
                f"at {_format_size(speed)}/s"
            )

        sys.stdout.write(message)
        sys.stdout.flush()

    return _hook


# Function to download a model
def download(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"Downloading -> {output_path}")
    start_time = time.time()
    urllib.request.urlretrieve(url, output_path, reporthook=_make_progress_hook(start_time))
    sys.stdout.write("\n")
    print(f"Downloaded to {output_path}")

# URL of the model to download
model_url = 'https://zenodo.org/record/4034264/files/CRNN_note_F1%3D0.9677_pedal_F1%3D0.9186.pth?download=1'
model_output_path = 'src/model/CRNN_note_F1=0.9677_pedal_F1=0.9186.pth'

# URL of sf2 soundfont
sf2_url = 'https://drive.usercontent.google.com/download?id=1JZhVj0SDoz-JQ72QFbnmoIIEk4kUjcSR&export=download'
sf2_output_path = 'src/resources/GeneralUser-GS.sf2'

def check_exists(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0

# Download the model
if not check_exists(model_output_path):
    download(model_url, model_output_path)
if not check_exists(sf2_output_path):
    download(sf2_url, sf2_output_path)