#!/usr/bin/env python3
import argparse
import cairo
import re
import math


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", hex_color):
        raise ValueError(f"Invalid color code: {hex_color}")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    return r, g, b


def get_best_text_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return (0, 0, 0) if luminance > 0.5 else (1, 1, 1)


def render_palette(font, colors, output_file):
    bar_width = 128
    width = bar_width * len(colors)
    height = 512
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    font_slant = cairo.FONT_SLANT_NORMAL
    font_weight = cairo.FONT_WEIGHT_NORMAL
    for index, hex_color in enumerate(colors):
        rgb = hex_to_rgb(hex_color)
        x = index * bar_width
        ctx.rectangle(x, 0, bar_width, height)
        ctx.set_source_rgb(*rgb)
        ctx.fill()
        ctx.save()
        ctx.select_font_face(font, font_slant, font_weight)
        font_size = 24
        ctx.set_font_size(font_size)
        text = hex_color.upper()
        xb, yb, tw, th, xa, ya = ctx.text_extents(text)
        text_rgb = get_best_text_color(hex_color)
        ctx.set_source_rgb(*text_rgb)
        ctx.translate(x + bar_width / 2, height / 2)
        ctx.rotate(-math.pi / 2)
        ctx.move_to(-tw / 2, th / 2)
        ctx.show_text(text)
        ctx.restore()
    surface.write_to_png(output_file)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a color palette image from hex codes with vertical text."
    )
    parser.add_argument("font", help="Font family name (e.g., 'Roboto')")
    parser.add_argument(
        "colors", nargs="+", help="List of hex color codes (e.g., #FF0000)"
    )
    parser.add_argument(
        "--output", "-o", default="output.png", help="Output PNG file name"
    )
    args = parser.parse_args()
    if len(args.colors) < 2:
        parser.error("Please provide at least 2 colors.")
    if len(args.colors) > 16:
        parser.error("Please provide no more than 16 colors.")
    try:
        [hex_to_rgb(c) for c in args.colors]
    except ValueError as err:
        parser.error(str(err))
    render_palette(args.font, args.colors, args.output)


if __name__ == "__main__":
    main()
