# Convert a colour HEX code to RGB(0..1), RGB(0..255), and HSV (using two different methods)

# import colorsys (a built-in module).
import colorsys

# Validate the hexadecimal color code.
def sanitize_hex_color(hex_color):
    hex_color = hex_color.upper().replace("#", "")
    if not all(c in "0123456789ABCDEF" for c in hex_color):
        raise ValueError("Invalid hex color code: contains invalid characters")
    if len(hex_color) not in [3, 6]:
        raise ValueError("Invalid hex color code: length should be 3 or 6")
    return hex_color

# Convert the hexadecimal color code to RGB.
def hex_to_rgb(hex_color):
    hex_color = sanitize_hex_color(hex_color)
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return (r, g, b)

# Convert RGB to HSV.
def rgb_to_hsv1(rgb_color):
    r, g, b = rgb_color
    M = max(r, g, b)
    m = min(r, g, b)
    C = M - m

    if C == 0:
        H = 0
    elif M == r:
        H = ((g - b) / C) % 6
    elif M == g:
        H = (b - r) / C + 2
    else:
        H = (r - g) / C + 4

    H *= 60
    V = M * 100  # Adjust the V value to be in the range [0, 100]
    S = (C / M) * 100 if M != 0 else 0 # Adjust the S value to be in the range [0, 100]

    return (H, S, V)

# Request the user to enter a hexadecimal color code.
while True:
    user_input = input("Enter a hexadecimal color code: ")
    # Use a try-except block to validate the user input.
    try:
        rgb_std = hex_to_rgb(user_input)
        rgb_dec = tuple(round(i / 255, 6) for i in rgb_std)
        hsv_color1 = rgb_to_hsv1(rgb_dec)

        # need to use the unpacking operator (*) because colorsys.rgb_to_hsv takes three separate arguments (R, G, B)
        # instead of a single tuple of three values (R, G, B)
        # https://stackoverflow.com/questions/16346841/unpacking-a-tuple-in-python
        # The function signature is: colorsys.rgb_to_hsv(r, g, b)
        hsv_color2 = colorsys.rgb_to_hsv(*rgb_dec)

        # Multiply HSV_2 values by 360, 100, and 100, respectively
        h2, s2, v2 = hsv_color2
        hsv_color2_scaled = (h2 * 360, s2 * 100, v2 * 100)

        # Print the results.
        print(f"Hexadecimal RGB: {user_input}")
        print(f"Decimal RGB: {rgb_dec}")
        print(f"Standard RGB: {rgb_std}")
        print(f"HSV_1: {hsv_color1}")
        print(f"HSV_2 (raw): {hsv_color2}")
        print(f"HSV_2 (scaled): {hsv_color2_scaled}")
        break
    # Handle the exception.
    except ValueError as e:
        print(e)
