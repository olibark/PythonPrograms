# Music Machine

This simple Python script displays a text-based visualization for a `.wav` audio file.

It does **not** play audio. It analyses the waveform and shows an ASCII bar whose
length follows the loudness of the music. Pitch is estimated using a basic zero
crossing method and a very naive tempo estimate counts peaks above a threshold.

## Usage

```bash
python visualize.py path/to/song.wav
```

Make sure you run the script inside a real terminal because it uses the
`curses` module for updating the display.
