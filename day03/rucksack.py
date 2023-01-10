class RuckSack:
    def __init__(self, contents):
        self.contents = contents
        self.compartiment1_contents = self.contents[: (int(len(self.contents) / 2))]
        self.compartiment2_contents = self.contents[(int(len(self.contents) / 2)) :]

    def in_both_compartiments(self):
        common = list(
            set(self.compartiment1_contents) & set(self.compartiment2_contents)
        )
        return common[0]
