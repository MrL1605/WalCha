import Image, ImageDraw
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

start_time = time.time()
img = Image.new("RGB", resolution_details, "#FFFFFF")
draw = ImageDraw.Draw(img)
for coord_i in range(resolution_details[0]):
    for coord_j in range(resolution_details[1]):
        r, g, b = rint(0, 255), rint(0, 255), rint(0, 255)
        draw.point((coord_i, coord_j), fill=(int(r), int(g), int(b)))

img.save("out.png", "PNG")
subprocess.Popen(
    "gsettings set org.gnome.desktop.background picture-uri file:///home/lalit/Linktogit_things/WalCha/out.png",
    shell=True)
end_time = time.time()
print "Image created and set as wallpaper in " + str(end_time - start_time) + " sec"
