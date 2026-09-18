# NATO Encoder/Decoder

A small Python CLI that turns plain text into the NATO phonetic alphabet (Alfa, Bravo, Charlie...) and back again.

I built this as a learning project while getting more comfortable with Python, especially dictionaries, string handling, and regular expressions. If you're also learning, feel free to poke around the code, break it, and see what happens.

## What it does

- **Encode**: type a word or sentence, get back its NATO phonetic spelling.
- **Decode**: paste NATO phonetic words back in, get the original letters out.

Example:

```
Enter your choice
1.(To encode), 2.(To decode), 3.(To Exit): 1
Enter your message: Hi
The original version: Hi
The encoded version: HotelIndia
```

## Getting started

Requirements: Python 3.13 or newer.

This project uses [uv](https://docs.astral.sh/uv/) for dependency management, since it's already set up with a `pyproject.toml` and `uv.lock`.

```bash
uv sync
uv run main.py
```

If you'd rather use plain pip:

```bash
pip install humre
python main.py
```

Once it's running, you'll get a simple menu:

1. Encode a message
2. Decode a message
3. Exit

A couple of notes on how it behaves right now:

- When encoding, stick to letters only. Contractions and punctuation (like "let's") aren't handled.
- When decoding, make sure the NATO words are separated by spaces.

## Project structure

- `main.py`: the CLI loop, asks what you want to do and calls into `utils.py`.
- `natoPhonetic.py`: the letter-to-NATO-word mapping (`Nato` dict).
- `utils.py`: the actual encoding/decoding logic.

## About the regex

The decoder needs to split a run of concatenated NATO words (like `HotelIndia`) back into `Hotel` and `India`. Instead of hand-writing a regular expression, this project uses [**humre**](https://github.com/asweigart/humre) by [Al Sweigart](https://github.com/asweigart).

Humre lets you build a pattern out of readable function calls instead of regex symbols, so instead of squinting at something like `[A-Z][a-z]*`, you get:

```python
pattern = chars('A-Z') + zero_or_more(chars('a-z'))
```

which reads almost like English: a capital letter, followed by zero or more lowercase letters. I found it a genuinely fun way to write regex without having to memorize regex syntax, and wanted to give credit where it's due. Go check out the library, it's great for anyone (beginner or not) who finds regex intimidating.

## Why this might be useful if you're new to Python

This is a tiny codebase, so it's easy to read end to end in a few minutes. If you're learning, a few things worth looking at:

- How a dictionary is used to map letters to words (and reversed to map words back to letters) in `natoPhonetic.py` and `utils.py`.
- Basic string methods: `.split()`, `.upper()`, `.join()`.
- A simple `while True` menu loop in `main.py`.
- A real (if small) example of using a regex library to parse text.

Feel free to fork it, extend it, or use it as a reference for your own first CLI project.

## License

MIT, see [LICENSE](LICENSE).
