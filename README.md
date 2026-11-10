*This project has been created as part of the 42 curriculum by samalves.*

# Arachnida

## Description

Arachnida is a project from the 42 Cybersecurity Piscine. It contains two command-line programs for working with web images:

- **Spider** downloads supported images from a website and can recursively follow same-host page links.
- **Scorpion** displays image creation-date information and EXIF metadata from image files.

The goal is to practise web requests, HTML parsing, file handling, and image metadata inspection.

## Instructions

### Requirements

- Python 3
- Pillow, used by Scorpion to read images and EXIF metadata

Spider uses Python's standard library. No compilation is required.

If Pillow is not available in the Python environment, install it where package installation is permitted:

```bash
python3 -m pip install Pillow
```

Make the programs executable if necessary:

```bash
chmod +x spider scorpion
```

### Spider

```bash
./spider URL [-r] [-l [N]] [-p [PATH]]
```

Examples:

```bash
./spider https://example.com
./spider https://example.com -r -l 2 -p ./images
```

Without `-r`, Spider processes only the starting page. With `-r`, it follows same-host links. The default recursion depth is `5`, and the default output directory is `./data/`. Supported image extensions are `.jpg`, `.jpeg`, `.png`, `.gif`, and `.bmp`.

### Scorpion

```bash
./scorpion IMAGE [IMAGE ...]
```

Example:

```bash
./scorpion photo.jpg logo.png
```

Scorpion reports errors for missing, unreadable, unsupported, or invalid image files and continues with the remaining inputs.

## Resources

- 42 Arachnida subject: Spider and Scorpion project requirements.
- [Python `argparse`](https://docs.python.org/3/library/argparse.html) — command-line arguments.
- [Python `html.parser`](https://docs.python.org/3/library/html.parser.html) — HTML parsing.
- [Python `urllib`](https://docs.python.org/3/library/urllib.html) — web requests and URL handling.
- [Python `pathlib`](https://docs.python.org/3/library/pathlib.html) — filesystem paths.
- [Pillow Image documentation](https://pillow.readthedocs.io/en/stable/reference/Image.html) — image opening and EXIF access.

### Use of AI

AI assistance was used to explain Python concepts, discuss implementation approaches, help reason about debugging output, and draft this README. The student implemented and tested the programs and is responsible for reviewing and understanding the submitted code.

## Project Structure and Technical Choices

The repository contains the `spider` and `scorpion` Python programs and this README. Spider uses the built-in HTML parser and URL/file-handling modules. Scorpion uses Pillow for image decoding and EXIF metadata access.
