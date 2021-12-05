# Problem #221
# Harvey's Shot
# Harvey is set on a mission to test his luck. 
# To test a person’s luck there is a circular room which is marked with 180 points with numbers 1,2,3,⋯,180
# written on them on the circumference equidistant from the adjacent points. 
# Harvey stands at the point 1 on the boundary with a gun in his hand. 
# He shoots the gun aiming inside the circle at any of the marked points from 2 to 90 (90 included). 
# Assuming an elastic collision between the bullet and the wall the bullet reflects as soon as it touches any point on the circumference.
# If the bullet reaches the point 1 it hits Harvey and he dies.
# The bullet stops when it reaches a point where the number written on it is smaller than that of the number written on the point 
# from which it was reflected.
# Given that Harvey chooses the point where he shoots randomly, let the probability that Harvey dies in the game be mn (m and n are coprime). 
# Enter your answer as m⋅n.

results = {}
for i in range(1,90):
	pos = 1
	working = True
	while working:
		newPos = pos + i
		if newPos > 180:
			newPos = newPos - 180
		if newPos == 1:
			print("{},{},{}: {}".format(i,pos,newPos,False))
			working = False
			results[i] = False
		else:
			if newPos < pos:
				print("{},{},{}: {}".format(i,pos,newPos,True))
				results[i] = True
				working = False
		pos = newPos

print("{}:{} => {}".format(
	len([k for k,v in results.items() if v == False]),
	len(results.values()),
	len([k for k,v in results.items() if v == False]) * len(results.values())))
