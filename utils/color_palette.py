label_colors = {
            'Domain': '#636EFA',
            'Whois_Phone': '#EF553B',
            'Whois_Email': '#00CC96',
            'Whois_Name': '#AB63FA',
            'IP': '#FFA15A',
            'IP_C': '#5fab28',
            'Cert': '#19D3F3',
            'ASN': '#FF6692'
        }


def reduce_brightness(hex_color, factor=0.5):
    """
    输入一个十六进制的RGB色彩值，返回其变灰的颜色
    """
    if '#' in hex_color:
        hex_color = hex_color.lstrip('#')
    # Convert hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Reduce brightness
    r_new = int(r * factor)
    g_new = int(g * factor)
    b_new = int(b * factor)

    # Ensure values are within valid range (0-255)
    r_new = min(max(r_new, 0), 255)
    g_new = min(max(g_new, 0), 255)
    b_new = min(max(b_new, 0), 255)

    # Convert RGB back to hex
    return '#{:02x}{:02x}{:02x}'.format(r_new, g_new, b_new)