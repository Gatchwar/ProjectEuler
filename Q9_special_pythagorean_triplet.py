# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

N = 1000  # cap N at 1000 since x+y+z=1000 therefore x < y < z < 1000
for x in range(1, N):
    y = x + 1
    z = y + 1
    while z <= N:
        while z**2 < x**2 + y**2: 
            z += 1
        if z**2 == x**2 + y**2:
            if x+y+z == 1000:
                print("x:{}, y:{}, z:{}, xyz:{}".format(x, y, z, x*y*z))
        y += 1
