
"""
Static Bakery Menu QR Code Generator

Requirements:
    py -m pip install "qrcode[pil]"

Run:
    py generate_static_qr.py

Output:
    bakery_menu_qr.png
    bakery_menu_qr.svg
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import qrcode.image.svg


# Your published bakery menu URL
MENU_URL = "https://kovankrd.github.io/bakery-menu/"


# QR Code settings
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H
BOX_SIZE = 20
BORDER = 4


# Create QR Code
qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECTION,
    box_size=BOX_SIZE,
    border=BORDER
)

qr.add_data(MENU_URL)
qr.make(fit=True)


# Generate rounded PNG QR Code
png_image = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    fill_color="black",
    back_color="white"
)

png_image.save("bakery_menu_qr.png")


# Generate SVG QR Code
svg_image = qrcode.make(
    MENU_URL,
    image_factory=qrcode.image.svg.SvgPathImage
)

svg_image.save("bakery_menu_qr.svg")


# Success message
print("\nStatic QR codes generated successfully!")
print("---------------------------------------")
print("PNG: bakery_menu_qr.png")
print("SVG: bakery_menu_qr.svg")
print("Menu URL:", MENU_URL)
print("---------------------------------------")
print("Remember to test both QR codes before printing.")
