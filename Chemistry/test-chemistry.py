import unittest
import chemistry_easy
import chemistry_intermediate as intermediate

class testChemistryEasy(unittest.TestCase):

    def test1Spenglerium(self):
        t1=['Spenglerium','Ee']  #true
        self.assertTrue(chemistry_easy.checkValidity(t1[0], t1[1]))

    def test2Zeddemorium(self):
        t2=['Zeddemorium', 'Zr'] #true
        self.assertTrue(chemistry_easy.checkValidity(t2[0], t2[1]))

    def test3Venkmine(self):
        t3=['Venkmine', 'Kn' ]   #true
        self.assertTrue(chemistry_easy.checkValidity(t3[0], t3[1]))

    def test4Stantzon(self):
        t4=['Stantzon', 'Zt']    #false
        self.assertFalse(chemistry_easy.checkValidity(t4[0], t4[1]))

    def test5Melintzum(self):
        t5=['Melintzum', 'Nn']   #false
        self.assertFalse(chemistry_easy.checkValidity(t5[0], t5[1]))

    def test6Tullium(self):
        t6=['Tullium', 'Ty']     #false
        self.assertFalse(chemistry_easy.checkValidity(t6[0], t6[1]))

    def test7tooShort(self):
        t7=['Tullium', 'T']      #false
        self.assertFalse(chemistry_easy.checkValidity(t7[0], t7[1]))

    def test8tooLong(self):
        t8=['Tullium', 'Tyw']    #false
        self.assertFalse(chemistry_easy.checkValidity(t8[0], t8[1]))

class testChemistryMedium(unittest.TestCase):
    def testNeon(self):
        self.assertEqual(intermediate.preferredSymbol('Neon'), 'Eo')

unittest.main()