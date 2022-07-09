def write_color(pixel_color):
    # truncate to interval [0,1]
    pixel_color.x = max(0, min(pixel_color.x, 1))
    pixel_color.y = max(0, min(pixel_color.y, 1))
    pixel_color.z = max(0, min(pixel_color.z, 1))
    print(str(round(255 * pixel_color.x)) + ' ' + 
          str(round(255 * pixel_color.y)) + ' ' + 
          str(round(255 * pixel_color.z)))