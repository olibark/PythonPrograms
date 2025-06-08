# PythonPrograms

This repository contains various experiments and sample programs.

## Browser Game

A simple Snake game is included under `HTML/snake`. Open `index.html` in a web browser to play.

## Cleaning up tracked files

If you update `.gitignore` and want Git to stop tracking existing files that should now be ignored, run:

```bash
git rm -r --cached .
```

This removes the files from the repository while leaving them on disk. After running the command, commit the deletions.

