import unittest

"""
The class is a representation of a point of x/y coordinate map
"""


class Point:
	def __init__(self, x=0, y=0):
		"""
		The constructor
		:param x:
		:param y:
		"""
		self.x = Point._validate_coordinate(x)
		self.y = Point._validate_coordinate(y)

	def __str__(self):
		"""
		String representation of the Point object
		:return: String
		"""
		return "({}, {})".format(self.x, self.y)

	@staticmethod
	def _validate_coordinate(coordinate_value):
		"""
		Validate that the coordnate is valid (integer)
		Throw an error otherwise
		:param coordinate_value:
		:return: int
		"""
		if isinstance(coordinate_value, int):
			return coordinate_value
		else:
			raise TypeError("Coordinate value can only be an integer.")


"""
The class is a representation of a line
"""


class Line:
	def __init__(self, starting_point, ending_point):
		"""
		The constructor
		:param starting_point:
		:param ending_point:
		"""
		self.starting_point = starting_point
		self.ending_point = ending_point

	def length(self):
		"""
		Return the line length
		:return: int
		"""
		s = self.starting_point
		e = self.ending_point
		return (s.x-e.x)**2 + (s.y-e.y)**2

	def __str__(self):
		"""
		The string representation of the object
		:return:
		"""
		return "{} {}".format(str(self.starting_point), str(self.ending_point))


if __name__ == '__main__':

	class LineTest(unittest.TestCase):

		def test_line_can_be_initialized(self):
			"""
			Test that Line class can be initialized
			:return:
			"""
			start_point = Point()
			end_point = Point(10, 15)
			target_line = Line(start_point, end_point)
			self.assertEqual(str(target_line), "(0, 0) (10, 15)")

		def test_line_can_calculate_the_length(self):
			"""
			Test that the line length can be calculated
			:return:
			"""
			start_point = Point()
			end_point = Point(10, 15)
			target_line = Line(start_point, end_point)
			self.assertEqual(target_line.length(), 325)

		def test_line_length_can_be_calculated_for_zero(self):
			"""
			Test that line with 0 length can be calculated
			:return:
			"""
			start_point = Point()
			end_point = Point()
			target_line = Line(start_point, end_point)
			self.assertEqual(target_line.length(), 0)

		def test_line_can_be_represented_as_a_string(self):
			"""
			Test that the line can be represented as a string
			:return:
			"""
			start_point = Point()
			end_point = Point(10, 15)
			target_line = Line(start_point, end_point)
			self.assertEqual(str(target_line), "(0, 0) (10, 15)")


	unittest.main()


	# class PointTest(unittest.TestCase):
	#
	# 	def test_default_values_in_point(self):
	# 		"""
	# 		Test that point can be initialized with default values
	# 		:return:
	# 		"""
	# 		target_point = Point()
	# 		self.assertEqual(target_point.x, 0)
	# 		self.assertEqual(target_point.y, 0)
	#
	# 	def test_x_overwrite(self):
	# 		"""
	# 		Test that point can be initialized with x coordinate overwrite
	# 		:return:
	# 		"""
	# 		target_point = Point(10)
	# 		self.assertEqual(target_point.x, 10)
	# 		self.assertEqual(target_point.y, 0)
	#
	# 	def test_y_overwrite(self):
	# 		"""
	# 		Test that point can be initialized with y coordinate overwrite
	# 		:return:
	# 		"""
	# 		target_point = Point(10, 20)
	# 		self.assertEqual(target_point.x, 10)
	# 		self.assertEqual(target_point.y, 20)
	#
	# 	def test_user_cannot_initialize_with_non_integers_x(self):
	# 		"""
	# 		Test that user cannot initialize the class with non-integers passed to the constructor for X
	# 		:return:
	# 		"""
	# 		self.assertRaises(TypeError, Point, "foo")
	#
	# 	def test_user_cannot_initialize_with_non_integers_y(self):
	# 		"""
	# 		Test that user cannot initialize the class with non-integers passed to the constructor for Y
	# 		:return:
	# 		"""
	# 		self.assertRaises(TypeError, Point, "foo", 31.1)