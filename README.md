# QR Code Generator

A Python script that generates a QR code from a URL using the `qrcode` library, saved as a PNG image.

## What it does

Takes a URL as input and outputs a scannable QR code image — used here to generate codes linking to my portfolio site, LinkedIn, and GitHub.

## How to run it

1. Install dependencies:
   ```
   pip3 install qrcode --break-system-packages
   pip3 install Pillow --break-system-packages
   ```
2. Run the script:
   ```
   python3 QRProject.py
   ```
3. Enter a URL when prompted. The QR code saves as a PNG in the same folder.

## Example

Input: `https://eneshadedwards.com`
Output: a QR code image that scans to that link.

## What I learned

First hands-on Python practice project — covers control flow (if/elif/else, for, while), functions with parameters and return values, working with an external library, and debugging real errors (indentation, missing dependencies, file path issues).
