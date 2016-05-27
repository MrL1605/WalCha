import subprocess

version_details = subprocess.Popen("gnome-session --version", shell=True, stdout=subprocess.PIPE).stdout.read()
try:
    gnome_session_version = int(version_details.split(" ")[1].split(".")[0])
    assert gnome_session_version == 3, "Gnome Session not of supported version - " + str(gnome_session_version)
    resolution_details = subprocess.Popen("xdpyinfo  | grep 'dimensions:'", shell=True, stdout=subprocess.PIPE).stdout.read()
    resolution_details = map(int, resolution_details.split(" ")[6].split("x"))
    print "Your screen resolution - " + str(resolution_details[0]) + " x " + str(resolution_details[1])
except IndexError:
    print "Gnome Session not of supported version"
    exit()




