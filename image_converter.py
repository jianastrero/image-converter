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
    parser.add_argument('--size', type=int, default=512, help='Output size')
    parser.add_argument('--mode', type=str, default='RGB', help='Output mode')
    parser.add_argument('--recursive', type=bool, default=False, help='Recursive mode')
    parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite mode')

    return parser.parse_args()


def main():
    args = parse_arguments()


if __name__ == "__main__":
    main()
