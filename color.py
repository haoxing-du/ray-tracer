def clamp(x, mi, ma):
    return max(mi, min(ma, x))

def write_color(pixel_color, samples_per_pixel):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z
    # divide the color by the number of samples
    scale = 1 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale
    # write the translated [0, 255] value of each color component
    print(str(round(255 * clamp(r, 0, 1))) + ' ' + 
          str(round(255 * clamp(g, 0, 1))) + ' ' + 
          str(round(255 * clamp(b, 0, 1))))