import cv2
import numpy as np
import json
import os

def is_blurry(image, threshold=100.0):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return lap_var < threshold, lap_var

def is_under_or_over_exposed(image, low_thresh=50, high_thresh=200):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)
    if avg_brightness < low_thresh:
        return "Underexposed", avg_brightness
    elif avg_brightness > high_thresh:
        return "Overexposed", avg_brightness
    else:
        return "Good", avg_brightness

def check_image_quality(image_path):
    if not os.path.exists(image_path):
        return {"error": "File does not exist."}

    image = cv2.imread(image_path)
    blurry, blur_score = is_blurry(image)
    exposure_status, brightness = is_under_or_over_exposed(image)
    # Determine overall quality
    is_low_quality = blurry or exposure_status != "Good"


    result = {
        "image_path": image_path,
        "is_blurry": bool(blurry),
        "blur_score": float(blur_score),
        "exposure_status": str(exposure_status),
        "brightness": float(brightness),
        "quality": "Low" if is_low_quality else "Good"
    }

    return result

import glob

if __name__ == "__main__":
    image_folder = "images"
    image_paths = glob.glob(os.path.join(image_folder, "*"))

    all_results = []

    for path in image_paths:
        # Skip non-image files (e.g., .txt, .docx)
        if not (path.lower().endswith(".jpg") or path.lower().endswith(".png")):
            print(f"Skipped (not an image): {path}")
            continue

        result = check_image_quality(path)

        # Convert NumPy types
        result["is_blurry"] = bool(result.get("is_blurry", False))
        result["blur_score"] = float(result.get("blur_score", 0))
        result["brightness"] = float(result.get("brightness", 0))
        result["exposure_status"] = str(result.get("exposure_status", "Unknown"))

        all_results.append(result)
        print(f"Checked: {path}")

        # Save individual report
        base_name = os.path.splitext(os.path.basename(path))[0]
        report_path = f"reports/{base_name}_report.json"
        os.makedirs("reports", exist_ok=True)
        with open(report_path, "w") as f:
            json.dump(result, f, indent=4)

    # Save full batch report
    with open("batch_quality_report.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print("\nBatch report saved to batch_quality_report.json")

