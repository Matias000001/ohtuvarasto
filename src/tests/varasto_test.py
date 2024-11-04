import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_nollataan(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_negatiivisella_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_negatiivisella_palauttaa_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_yli_saldon_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")
