Script for quickly setting up python tests for a small library of algorithm problems.

Requires `fzf`, `python3`, and `nvim`.

After cloning this repo, run the following commands (this presumes `~/bin` is on your path):

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ln -s $(pwd)/practice ~/bin
```

Usage:
Run `practice` on the command line; choose the algorithm problem you want to practice.
