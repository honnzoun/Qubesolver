from sys import exit as Die
try:
    import sys
except ImportError as err:
    Die(err)


class ColorDetection:

    def get_color_name(self, hsv):
        (h, s, v) = hsv
        if h < 15 and v < 100:
            return 'red'
        if h <= 10 and v > 100:
            return 'orange'
        elif h <= 30 and s <= 100:
            return 'white'
        elif h <= 40:
            return 'yellow'
        elif h <= 85:
            return 'green'
        elif h <= 130:
            return 'blue'

        return 'white'

    def name_to_rgb(self, name):
        color = {
            'red': (0,0,255),
            'orange': (0,165,255),
            'blue': (255,0,0),
            'green': (0,255,0),
            'white': (255,255,255),
            'yellow': (0,255,255)
        }
        return color[name]

    def average_hsv(self, roi):
        h = 0
        s = 0
        v = 0
        num = 0
        for y in range(len(roi)):
            if y % 10 == 0:
                for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
        h /= num
        s /= num
        v /= num
        return (int(h), int(s), int(v))


ColorDetector = ColorDetection()
