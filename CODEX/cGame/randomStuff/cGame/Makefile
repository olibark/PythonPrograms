CC=gcc

all: guess

# build terminal version
guess: guess.c
	$(CC) guess.c -o guess

# build GUI version (requires GTK 3)
# run `make gui` or `make guess_gui` to build it

guess_gui: guess_gui.c
	$(CC) guess_gui.c -o guess_gui $(shell pkg-config --cflags --libs gtk+-3.0)

gui: guess_gui

clean:
	rm -f guess guess_gui

.PHONY: all gui clean