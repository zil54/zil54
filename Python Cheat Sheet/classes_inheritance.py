import math
import sys


class ImproperTriangleRepresentation(Exception):
	def __init__(self):
		print ("One of the triangle properties wasn't satisfied - not a valid representation of triangle")
		

class ImproperEqTriangleRepresentation(Exception):
	def __init__(self):
		print ("All sides equality of the equilateral triangle hasn't been satisfied - not a valid representation of eq. triangle ")



class Triangle:
	def __init__(self, side1, side2, side3):
		try:
			self.side1 = side1
			self.side2 = side2
			self.side3 = side3
			if (self.side1 + self.side2 <= self.side3) or (self.side3 + self.side2 <= self.side1) or (self.side3 + self.side1 <= self.side3):
				raise ImproperTriangleRepresentation
		except:
			sys.exit()
	
	def calc_perimeter(self):
		print (self.side1 + self.side2 + self.side3)
		
	def calc_area(self):
		tempS = (self.side1 + self.side2 + self.side3)/2
		area = (math.sqrt(tempS * (tempS - self.side1) * (tempS - self.side2) * (tempS - self.side3)))
		print (area)
		
class EqTriangle(Triangle):
	def __init__(self, side1, side2, side3):
		try:
			super().__init__(side1, side2, side3)
			if (self.side1 != self.side3) or (self.side1 != self.side2) or (self.side2 != self.side3):
				raise ImproperEqTriangleRepresentation
		except:
			sys.exit()
	
	def calc_perimeter(self):
		print (self.side1 * 3)
		
	def calc_area(self):
		super().calc_area()
			
triangle = Triangle(3,4,5)
triangle.calc_perimeter()
triangle.calc_area()
triangle2 = EqTriangle(8,8,8)
triangle2.calc_perimeter()
triangle3 = EqTriangle(8,8,9)
triangle3.calc_perimeter()


				
	



 



