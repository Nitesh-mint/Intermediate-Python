'''
Insertion sort compares itself to the left element.
We start at the second index comparing itself to the first index.
HERE. 41 is compared to 31
'''

array = [31, 41, 59, 26, 41, 58]
j = 1
array_size = (len(array))
for i in range(1, array_size):
	current = array[i] #second element i.e 41
	j = i - 1 # first element i.e 31

	while j>=0 and array[j] > current:
		array[j+1] = array[j]
		j-=1
	array[j+1] = current
# print(array)


class Fraction:
    def __init__(self, num1, num2):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both numbers should be integer")
        self.num1 = num1
        self.num2 = num2
    def print(self):
        print(self.num1,self.num2)

    def __str__(self):
        return str(self.num1) + " and " +  str(self.num2)

    def __add__(self, fraction):
        num1_add = self.num1 + fraction.num1
        num2_add = self.num2 + fraction.num2
        return num1_add
f = Fraction(5, 6)
f_str = Fraction('5', '6')
f1 = Fraction(5, 4)
