# cGame GUI

This folder contains a simple number guessing game in C.

- `guess.c` - terminal version
- `guess_gui.c` - GTK-based GUI version

## Building

You can use the included `Makefile` for a simpler build process:

```
make        # build the terminal version (./guess)
make gui    # build the GUI version (requires GTK 3)
make clean  # remove generated binaries
```

If you prefer to compile manually, use:

```
# terminal version
gcc guess.c -o guess

# GUI version (requires gtk3)
gcc guess_gui.c -o guess_gui $(pkg-config --cflags --libs gtk+-3.0)
```

Run `./guess_gui` to play using the GUI.