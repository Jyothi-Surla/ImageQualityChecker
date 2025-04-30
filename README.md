# Image Quality Checker

This is a Python-based tool that automatically checks image quality based on:
- **Blurriness** (Laplacian variance)
- **Brightness** (to detect underexposure or overexposure)

It supports batch processing of all `.jpg` and `.png` files inside a folder.

## Features
- Detects blurry images using Laplacian variance
- Flags underexposed and overexposed images
- Skips non-image files
- Saves:
  - A full batch report: `batch_quality_report.json`
  - One individual report per image in `/reports/` folder

## How to Use
1. Add images (`.jpg`, `.png`) to the `images/` folder
2. Run the script:
   ```bash
   python image_checker.py

## Technologies
- Python 3.10+
- OpenCV
- NumPy
- JSON

## Example Output

```json
{
  "image_path": "images/sample1_blurry.jpg",
  "is_blurry": true,
  "blur_score": 1.75,
  "exposure_status": "Good",
  "brightness": 174.94,
  "quality": "Low"
}
