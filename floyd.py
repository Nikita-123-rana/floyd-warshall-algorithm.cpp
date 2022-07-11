V = 4
INF = 99999
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	for k in range(V):
  for i in range(V):
			for j in range(V):
				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	printSolution(dist)
def printSolution(dist):
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%7s" % ("INF"),end=" ")
			else:
				print ("%7d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()
			10
	(0)------->(3)
		|		 /|\
	5 |		 |
		|		 | 1
	\|/		 |
	(1)------->(2)
			3		
graph = [[0, 5, INF, 10],
		[INF, 0, 3, INF],
		[INF, INF, 0, 1],
		[INF, INF, INF, 0]
		]
