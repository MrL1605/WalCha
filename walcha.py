import Image
import ImageDraw
from random import randint as rint
import subprocess
import time

resolution_details = []
try:
    version_details = subprocess.Popen("gnome-session --version", shell=True, stdout=subprocess.PIPE).stdout.read()
    gnome_session_version = int(version_details.split(" ")[1].split(".")[0])
    assert gnome_session_version == 3, "Gnome Session not of supported version - " + str(gnome_session_version)
    resolution_details = subprocess.Popen("xdpyinfo  | grep 'dimensions:'", shell=True,
                                          stdout=subprocess.PIPE).stdout.read()
    resolution_details = map(int, resolution_details.split(" ")[6].split("x"))
    print "Your screen resolution - " + str(resolution_details[0]) + " x " + str(resolution_details[1])
except IndexError:
    print "Not a Linux User, are you?"
    exit()


def get_one_color():
    return tuple(color_swatch[rint(1, len(color_swatch) - 1)])


def draw_circle():
    coord_a0 = rint(10, int(11 * resolution_details[0] / 12))
    coord_a1 = rint(10, int(11 * resolution_details[0] / 12))
    diameter = rint(80, 350)
    coord_b0 = coord_a0 + diameter
    coord_b1 = coord_a1 + diameter
    center_coord = tuple([coord_a0, coord_a1, coord_b0, coord_b1])
    draw.ellipse(center_coord, fill=get_one_color())


def draw_rectangle():
    coord_a0 = rint(10, int(11 * resolution_details[0] / 12))
    coord_a1 = rint(10, int(11 * resolution_details[1] / 12))
    x_change = rint(80, 500)
    y_change = rint(80, 500)
    if x_change > y_change:
        y_change, x_change = x_change, y_change
    coord_b0 = coord_a0 + x_change
    coord_b1 = coord_a1 + y_change
    center_coord = tuple([coord_a0, coord_a1, coord_b0, coord_b1])
    draw.rectangle(center_coord, fill=get_one_color())


start_time = time.time()
color_swatch = [[rint(200, 255), rint(200, 255), rint(200, 255)]]
img = Image.new("RGB", resolution_details, tuple(color_swatch[0]))
draw = ImageDraw.Draw(img)

color_swatch = [[rint(20, 180), rint(20, 180), rint(20, 180)]]

# Create a random color swatch to choose colors from
for i in range(rint(5, 20)):
    last_color = list(color_swatch[-1])
    r_index = rint(0, 2)
    # Change only one component and small change, so that color are of one tone
    last_color[r_index] = last_color[r_index] + rint(5, 40)
    last_color[r_index] %= 255
    color_swatch.append(last_color)

print "Color Swatch", color_swatch

for _ in range(rint(5, 10)):
    if rint(0, 1) == 0:
        print "Drawing a Circle"
        draw_circle()
    else:
        print "Drawing a Rectangle"
        draw_rectangle()

img.save("out.png", "PNG")
# subprocess.Popen(
#         "gsettings set org.gnome.desktop.background picture-uri file:///home/lalit/Linktogit_things/WalCha/out.png",
#         shell=True)
end_time = time.time()
print "Image created and set as wallpaper in " + str(end_time - start_time) + " sec"
