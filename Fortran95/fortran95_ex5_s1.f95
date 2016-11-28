! Script 1

real:: n, sum=0, product=1, square_sum=0, sum_square=0

do 1, 10
	print * , 'Please enter the next number:'
	write * , n
	sum = sum + n
	product = product * n
	square_sum = square_sum + n ** 2
	sum_square = sum ** 2
end do

print * , 'sum = ', sum
print * , 'product = ', product
print * , 'sum of squares = ', square_sum
print * , 'square of sums = ', sum_square

end