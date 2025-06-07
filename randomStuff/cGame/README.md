# cGame GUI

This folder contains a simple number guessing game in C.

- `guess.c` - terminal version
- `guess_gui.c` - GTK-based GUI version

## Building

To build the GUI version you need GTK 3 development libraries.

```
# compile terminal version
gcc guess.c -o guess

# compile GUI version (requires gtk3)
gcc guess_gui.c -o guess_gui $(pkg-config --cflags --libs gtk+-3.0)
```

Run `./guess_gui` to play using the GUI.
