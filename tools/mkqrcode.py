#!/usr/bin/env python3

import argparse
import logging
import re

from pyzbar.pyzbar import decode
from PIL import Image

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer

# Create a dedicated logger
lgr = logging.getLogger(__name__)

def sanitize_filename(filename):
    sanitized = re.sub(r'[^\w]', '_', filename)
    return sanitized

def validate_compression_qualities(qualities):
    valid_qualities = {'L', 'M', 'Q', 'H'}
    if not all(q in valid_qualities for q in qualities):
        raise ValueError(f"Invalid compression qualities specified. Use any combination of: {', '.join(valid_qualities)}.")
    return qualities

def main(text, input_image, output_image, compression_qualities):
    lgr.debug(f"Processing text: {text}")
    kws = {}

    if input_image:
        lgr.debug(f"Embedding image: {input_image}")
        kws['embeded_image_path'] = input_image

    for q in compression_qualities:
        compress_quality = getattr(qrcode.constants, f'ERROR_CORRECT_{q}')
        
        qr = qrcode.QRCode(error_correction=compress_quality)
        qr.add_data(text)
        
        img = qr.make_image(image_factory=StyledPilImage, 
                            module_drawer=GappedSquareModuleDrawer(),
                            **kws)
        img.save(output_image)
        lgr.debug(f"Saved QR code image to: {output_image}")

        decoded = decode(Image.open(output_image))
        
        if len(decoded) != 1:
            lgr.debug(f"With error correction {q} got {len(decoded)} results.")
            continue

        decoded_data = decoded[0]
        lgr.debug(f"DEBUG: error correction {q} - quality: {decoded_data.quality}")

        if decoded_data.quality < 0.5:
            lgr.warning(f"With error correction {q} got too low quality {decoded_data.quality}.")
            continue

        text_decoded = decoded_data.data.decode()
        if text_decoded != text:
            lgr.warning(f"With error correction {q} decoded text does not match: {text_decoded!r} instead of {text!r}")
            continue
        
        lgr.info(f"Successfully decoded text: {text_decoded!r} encoded with compress quality {q}. File {output_image}")
        break
    else:
        lgr.error(f"Neither of error correction levels was good enough. File {output_image} might be unreadable.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and decode QR codes.")
    parser.add_argument("text", help="Text to encode in the QR code.")
    parser.add_argument("-i", "--input-image", help="Path to the input image (optional).")
    parser.add_argument("-o", "--output-image", help="Path to the output image (optional).")
    parser.add_argument("-c", "--compression-qualities", default="LMQH",
                        help="Compression qualities (default: LMQH). Choose any combination of L, M, Q, H.")
    parser.add_argument("-l", "--log-level", default="INFO", help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).")

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=args.log_level.upper(), format='%(asctime)s - %(levelname)s - %(message)s')

    # Validate compression qualities
    try:
        compression_qualities = validate_compression_qualities(args.compression_qualities)
    except ValueError as e:
        lgr.error(e)
        exit(1)

    # Sanitize output filename
    output_filename = args.output_image if args.output_image else f"{sanitize_filename(args.text)}.png"

    main(args.text, args.input_image, output_filename, compression_qualities)
