import unittest
import chemistry_easy

class testChemistryEasy(unittest.TestCase):

	def test1(self):
		t1=['Spenglerium','Ee']  #true
		self.assertTrue(chemistry_easy.checkValidity(t1[0], t1[1]))

	def test2(self):
		t2=['Zeddemorium', 'Zr'] #true
		self.assertTrue(chemistry_easy.checkValidity(t2[0], t2[1]))

	def test3(self):
		t3=['Venkmine', 'Kn' ]   #true
		self.assertTrue(chemistry_easy.checkValidity(t3[0], t3[1]))

	def test4(self):
		t4=['Stantzon', 'Zt']    #false
		self.assertFalse(chemistry_easy.checkValidity(t4[0], t4[1]))

	def test5(self):
		t5=['Melintzum', 'Nn']   #false
		self.assertFalse(chemistry_easy.checkValidity(t5[0], t5[1]))

	def test6(self):
		t6=['Tullium', 'Ty']     #false
		self.assertFalse(chemistry_easy.checkValidity(t6[0], t6[1]))

	def test7(self):
		t7=['Tullium', 'T']      #false
		self.assertFalse(chemistry_easy.checkValidity(t7[0], t7[1]))

	def test8(self):
		t8=['Tullium', 'Tyw']    #false
		self.assertFalse(chemistry_easy.checkValidity(t8[0], t8[1]))


unittest.main()