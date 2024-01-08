#  MIT License
#
#  Copyright (c) 2024 Jian James Astrero
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from PIL import Image
import PIL
import os
import glob
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert images to a specific format')

    parser.add_argument('--input_dir', type=str, default='input', help='Input directory')
    parser.add_argument('--output_dir', type=str, default='output', help='Output directory')
    parser.add_argument('--format', type=str, default='png', help='Output format')
    parser.add_argument('--quality', type=int, default=100, help='Output quality')
    parser.add_argument('--size', type=int, default=0, help='Output size')
    parser.add_argument('--recursive', type=bool, default=False, help='Recursive mode')
    parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite mode')

    return parser.parse_args()


def convert_image(input_path, output_path, format, quality, size):
    try:
        img = Image.open(input_path)
        img = img.resize((size, size), PIL.Image.LANCZOS)
        img.save(output_path, format=format, quality=quality)
    except Exception as e:
        print(e)


def main():
    args = parse_arguments()

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    format = args.format.lower()
    quality = max(0, min(args.quality, 100))
    size = max(0, args.size)
    recursive = bool(args.recursive)
    overwrite = bool(args.overwrite)

    if not os.path.exists(input_dir):
        print('Input directory does not exist')
        return

    if not os.path.exists(output_dir):
        os.makedirs(args.output_dir)

    if recursive:
        input_paths = glob.glob(os.path.join(input_dir, '**', '*.*'), recursive=True)
    else:
        input_paths = glob.glob(os.path.join(input_dir, '*.*'))

    for input_path in input_paths:
        input_path = os.path.abspath(input_path)
        output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
        output_path = os.path.splitext(output_path)[0] + '.' + format
        output_dir = os.path.dirname(output_path)

        if size == 0:
            size = max(Image.open(input_path).size)

        if os.path.exists(output_path) and not overwrite:
            continue

        convert_image(input_path, output_path, format, quality, size)
        print(f'Converted: {output_path} ({size}x{size}) (quality: {quality}) (format: {format})')


if __name__ == "__main__":
    main()
