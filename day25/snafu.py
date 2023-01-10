snafu_values = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


class SNAFU:
    def __init__(self, snafu):
        self.snafu = snafu

    def snafu_to_digital(self):
        digital_value = 0
        reverse = self.snafu[::-1]
        for i in range(len(reverse)):
            digital_value += 5**i * snafu_values[reverse[i]]
        return digital_value
