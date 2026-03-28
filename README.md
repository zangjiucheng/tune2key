# Tune2Key (CLI)

CLI tool for converting `.mp3` / `.mid` to MIDI, sheet PDF, and MP3 outputs.

## Quick Start

```sh
git clone https://github.com/yourusername/tune2key.git
cd tune2key
pip install -r requirements.txt
python download_model.py
```

Optional one-step setup:

```sh
./setup.sh
```

## Commands

```sh
python -m tune2key --help
python -m tune2key process /absolute/path/to/song.mp3
python -m tune2key process /absolute/path/to/song.mid --name my_song
python -m tune2key status my_song
python -m tune2key demos
```


## Output

Outputs are written to `src/resources/`:

- `midi/<name>.mid`
- `sheet/<name>.pdf`
- `mp3/<name>.mp3`
- `simple_sheet/<name>_simple.mid`
- `simple_sheet/<name>_simple.pdf`
- `simple_sheet/<name>_simple.mp3`

`src/resources` subfolders are auto-created if missing.

## Notes

- Supported input: `.mp3`, `.opus`, `.mid`
- `.pdf` input is not implemented yet
- MuseScore is required: `mscore --version`

## License

MIT. See [LICENSE](LICENSE).
