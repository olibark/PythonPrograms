import sys
import wave
import audioop
import curses
import time

CHUNK_SIZE = 1024
BEAT_THRESHOLD = 1000


def compute_pitch(data, width, sample_rate):
    """Estimate pitch using zero crossing rate."""
    num_samples = len(data) // width
    if num_samples < 2:
        return 0.0
    zero_crossings = 0
    prev = audioop.getsample(data, width, 0)
    for i in range(1, num_samples):
        cur = audioop.getsample(data, width, i)
        if (cur >= 0 and prev < 0) or (cur <= 0 and prev > 0):
            zero_crossings += 1
        prev = cur
    return (zero_crossings * sample_rate) / (2 * num_samples)


def visualize(path):
    wf = wave.open(path, 'rb')
    sample_rate = wf.getframerate()
    width = wf.getsampwidth()
    channels = wf.getnchannels()

    beats = 0
    start = time.time()

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    try:
        while True:
            data = wf.readframes(CHUNK_SIZE)
            if not data:
                break
            if channels > 1:
                mono = audioop.tomono(data, width, 1, 1)
            else:
                mono = data

            amp = audioop.rms(mono, width)
            if amp > BEAT_THRESHOLD:
                beats += 1

            pitch = compute_pitch(mono, width, sample_rate)
            elapsed = time.time() - start
            bpm = beats / (elapsed / 60) if elapsed > 0 else 0

            stdscr.clear()
            stdscr.addstr(0, 0, f"File: {path}")
            stdscr.addstr(1, 0, f"Amplitude: {amp}")
            stdscr.addstr(2, 0, f"Pitch: {pitch:.1f} Hz")
            stdscr.addstr(3, 0, f"Tempo: {bpm:.1f} BPM")
            bar = int(min(amp / 500, 50))
            stdscr.addstr(5, 0, "#" * bar)
            stdscr.refresh()
            time.sleep(CHUNK_SIZE / sample_rate)
    finally:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        wf.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize.py <audio.wav>")
        return
    visualize(sys.argv[1])


if __name__ == "__main__":
    main()
