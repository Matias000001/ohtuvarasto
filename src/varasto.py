class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = max(tilavuus, 0.0)

        if alku_saldo < 0.0:
            self.saldo = 0.0  # Nollataan virheellinen saldo
        else:
            self.saldo = min(alku_saldo, tilavuus)

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return  # Ei lisätä virheellistä määrää
        self.saldo = min(self.saldo + maara, self.tilavuus)

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0  # Ei oteta virheellistä määrää
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan
        self.saldo -= maara
        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
