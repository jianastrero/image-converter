## 🖼️ 🔀 🖼️ Image Converter script in Python
Convert images to other formats using Python

## 📝 Description:
This script converts images to other formats using Python. It uses the Pillow library to convert images.

## How to use:
```bash
python image_converter.py --input_dir <input_dir> \
                          --output_dir <output_dir> \
                          --format <output_format> \
                          --quality <output_quality> \
                          --size <output_size> \
                          --recursive <True/False> \
                          --overwrite <True/False>
```

## Parameters
| Parameter      | Default  | Description                                                          |
|:---------------|:---------|:---------------------------------------------------------------------|
| `--input_dir`  | `input`  | Input directory where the images are located                         |
| `--output_dir` | `output` | Output directory where the converted images will be saved            |
| `--format`     | `png`    | Output format of the converted images                                |
| `--quality`    | `100`    | Output quality of the converted images                               |
| `--size`       | `0`      | Output size of the converted images. 0 means it will retain its size |
| `--recursive`  | `False`  | Recursively convert images in subdirectories                         |
| `--overwrite`  | `False`  | Overwrite existing files in the output directory                     |

## 📝 Notes:
- The script will create the output directory if it doesn't exist.
- The script will not overwrite existing files in the output directory by default.
- The script will not convert images in subdirectories by default.
