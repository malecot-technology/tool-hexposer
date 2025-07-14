# Hexposer

**Hexposer** is a command-line tool that generates a clean, vertical color palette image from a list
of hexadecimal color codes. Each swatch is labeled with its corresponding hex code, rotated
vertically for compact, stylish presentation.

Perfect for designers, developers, and anyone who wants to visualize or share a color palette in a
quick, consistent way.

## Features

- Generates a PNG image with labeled color swatches.
- Automatically adjusts text color (black or white) for readability.
- Supports up to 16 colors per palette.
- Compact vertical text layout.

## Requirements

- Python 3.9+
- [pycairo](https://pycairo.readthedocs.io/en/latest/)

## Usage

```bash
./hexposer.py <font> <color1> <color2> ... <colorN> [-o OUTPUT]
```

### Arguments

- `<font>`: Font family name (e.g. `Arial`, `Roboto`, `Helvetica`).
- `<color>`: Hexadecimal color codes (e.g. `#FF0000`). Between **2** and **16** colors allowed.
- `-o`, `--output`: (Optional) Output filename (default: `output.png`).

### Example

```bash
./hexposer.py Roboto "#000091" "#FFFFFF" "#E1000F" -o palette.png
```

## Notes

- Make sure the font you specify is installed on your system.
- Color codes must be valid 6-digit hexadecimal strings starting with `#` (e.g. `#00ffcc`).
- The generated image has a fixed height of 512px and each color bar is 128px wide.

## License

This project is licensed under either of:

* [Apache License, Version 2.0](LICENSE-APACHE)
* [MIT license](LICENSE-MIT)
