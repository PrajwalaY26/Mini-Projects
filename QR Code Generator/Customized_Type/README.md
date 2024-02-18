# Customized_Type QR Code Generator

This is the Customized_Type version of the QR Code Generator. This version allows you to generate a customized QR code with specific parameters.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The Customized_Type QR Code Generator requires the following Python libraries:

- qrcode
- PIL (Pillow)

You can install these libraries using pip:

```bash
pip install qrcode[pil]
pip install pillow
```

### Usage

To use the Customized_Type QR Code Generator, simply run the script.

This script generates a QR code that encodes the URL "https://github.com/PrajwalaY26". The QR code is saved as an image file named "Prajwala_GiTHub.png". The QR code is customized with a black fill color, a white background, and rounded modules.

After running the script, the image file will be automatically created in the same folder as the script.

## Exploring More

You can modify the script to generate a QR code for any data you want. Simply replace "https://github.com/PrajwalaY26" with the data you want to encode in the QR code. You can also customize the fill color, background color, and module shape by changing the parameters in the `make_image` function.

## License

This project is licensed under the MIT License - see the ```LICENSE.md``` file for details
