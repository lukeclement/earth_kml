import numpy as np


def fly_to(spin_string, target_long, target_lat, target_alt, target_head, target_tilt, target_range, duration, fly_type):
    command = [
        "\n",
        "<gx:FlyTo>",  # 1
        "<gx:flyToMode>",  # 2
        "<gx:duration>",  # 3
        "<LookAt>",  # 4
        "<longitude>",  # 5
        "<latitude>",  # 6
        "<altitude>",  # 7
        "<heading>",  # 8
        "<tilt>",  # 9
        "<range>",  # 10
        "<gx:altitudeMode>",  # 11
        "</gx:altitudeMode>",
        "</range>",
        "</tilt>",
        "</heading>",
        "</altitude>",
        "</latitude>",
        "</longitude>",
        "</LookAt>",
        "</gx:duration>",
        "</gx:flyToMode>",
        "</gx:FlyTo>"
    ]
    spin_string += command[1]
    spin_string += command[0]
    spin_string += command[3] + str(duration) + command[-3]
    spin_string += command[0]
    spin_string += command[2] + fly_type + command[-2]
    spin_string += command[0]
    spin_string += command[4]
    spin_string += command[0]
    spin_string += command[5] + str(target_long) + command[-5]
    spin_string += command[0]
    spin_string += command[6] + str(target_lat) + command[-6]
    spin_string += command[0]
    spin_string += command[7] + str(target_alt) + command[-7]
    spin_string += command[0]
    spin_string += command[8] + str(target_head) + command[-8]
    spin_string += command[0]
    spin_string += command[9] + str(target_tilt) + command[-9]
    spin_string += command[0]
    spin_string += command[10] + str(target_range) + command[-10]
    spin_string += command[0]
    spin_string += command[11] + "clampToGround" + command[-11]
    spin_string += command[0]
    spin_string += command[-4]
    spin_string += command[0]
    spin_string += command[-1]
    return spin_string


def boilerplate(input_string, start, name):
    command = [
        "\n",
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",  # 1
        "<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" xmlns:kml=\"http://www.opengis.net/kml/2.2\" xmlns:atom=\"http://www.w3.org/2005/Atom\">",  # 2
        "<gx:Tour>",        # 3
        "<name>",           # 4
        "<gx:Playlist>",    # 5
        "</gx:Playlist>",
        "</name>",
        "</gx:Tour>",
        "</kml>",
        "</>"
    ]
    if start:
        input_string += command[1]
        input_string += command[0]
        input_string += command[2]
        input_string += command[0]
        input_string += command[3]
        input_string += command[0]
        input_string += command[4] + name + command[-4]
        input_string += command[0]
        input_string += command[5]
    else:
        input_string += command[-5]
        input_string += command[0]
        input_string += command[-3]
        input_string += command[0]
        input_string += command[-2]
    return input_string


def main():
    kml_string = boilerplate("", True, "First test")
    places = [
        [48.208056, 16.359167],
        [50.846667, 4.364722],
        [42.694456, 23.332893],
        [45.816111, 15.974444],
        [50.088056, 14.403889],
        [55.676111, 12.579722],
        [59.435600, 24.737200],
        [60.172500, 24.933333],
        [48.848333, 2.337222],
        # [52.518611, 13.376111],
        # [37.975278, 23.736944],
        # [47.507222, 19.045833],
        # [64.146667, -21.940278],
        # [53.341667, -6.254722],
        # [41.899167, 12.474167],
        # [56.951111, 24.105000],
        # [54.691111, 25.261944],
        # [49.610556, 6.133056],
        # [52.079600, 4.313000],
        # [59.913056, 10.740000],
        # [52.225278, 21.028333],
        # [38.712500, -9.153611],
        # [44.427222, 26.087500],
        # [44.811300, 20.465800],
        # [48.141944, 17.097222],
        # [46.051667, 14.501111],
        # [40.416389, -3.696667],
        # [59.327500, 18.067500],
        # [46.946667, 7.444167],
        # [39.911667, 31.851111],
        [51.499167, -0.124722]
    ]
    kml_string = fly_to(kml_string, -0.7597786997275657, 51.28449237591324, 0, 0, 0, 500, 0, "bounce")
    kml_string += "<gx:Wait><gx:duration>1.0</gx:duration></gx:Wait>"
    kml_string = fly_to(kml_string, 14.92793776004848, 51.08660503761194, 0, 0, 0, 3500000, 2, "bounce")
    kml_string += "<gx:Wait><gx:duration>1.0</gx:duration></gx:Wait>"
    total_duration = 5
    for index, place in enumerate(places):
        target_lat = place[0]
        target_long = place[1]
        target_alt = 0
        tilt = 70
        target_range = 500
        resolution = 1
        duration = total_duration/(360//resolution)
        spin_string = ""
        spin_string = fly_to(spin_string, target_long, target_lat, target_alt, 0, 0, target_range, 2, "bounce")
        tilt_time = 0.05
        for i in range(360//resolution):
            heading = resolution * i
            zero_to_one = (resolution / 360) * i
            cos_func = np.cos(zero_to_one * 1/(tilt_time*2) * np.pi)
            if zero_to_one < tilt_time*2 or zero_to_one + tilt_time*2 > 1:
                mid_tilt = tilt * (1 - (cos_func + 1)/2)
            else:
                mid_tilt = tilt
            # mid_tilt = tilt * (1 - ((np.cos( * np.pi) + 1)/2))
            # mid_tilt = tilt * (resolution / 360) * i
            # mid_tilt = tilt
            spin_string = fly_to(spin_string, target_long, target_lat, target_alt, heading, mid_tilt, target_range, duration, "smooth")
        kml_string += spin_string
        kml_string += "\n"
    kml_string = boilerplate(kml_string, False, "First test")
    file_to_write = open("Sovos_main.kml", 'w')
    file_to_write.write(kml_string)
    file_to_write.close()


if __name__ == '__main__':
    main()
