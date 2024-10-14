HEX_BASE = 16


def hex_to_rgb(colour_code):
    # "#1E90FF"
    rgb = []
    for i in range(1, 7, 2):
        rgb.append(int(colour_code[i:i + 2], HEX_BASE))
    return rgb


print(hex_to_rgb("#1E90FF"))
