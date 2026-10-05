class Emosi:
    def __init__(self, nilai):
        self.nilai = nilai

    def tentukan_label(self):
        if self.nilai >= 0.6:
            return "senang"
        elif self.nilai <= 0.3:
            return "sedih"
        else:
            return "netral"
