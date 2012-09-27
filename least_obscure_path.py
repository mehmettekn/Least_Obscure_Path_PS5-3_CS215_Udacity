"""This program is the solution to PS5-3 of CS215 at Udacity.com"""

""" This program calculates least obscure path between two nodes.
It reads and generates graphs from imdb files. Obscurity scores assigned movies
are multiplicative inverse of money the movie made. The program finds the least
obscure path between two actors based on the movies actors appeared in. The program
uses an implementation of dijkstra algoritm to find the least obscure path."""


import csv
import heapq
from priority_dictionary import priority_dict

"""An implementation of dijkstra algorithm to find the least obscure path"""

def dijkstra(G,v):
    obscr_so_far = priority_dict()
    obscr_so_far[v] = 0
    final_obscr = {}
    obscr = {}
    obscr[v] = 0
    while len(final_obscr) < len(G) and len(obscr_so_far) != 0:
        w = obscr_so_far.pop_smallest()
        # lock it down!
        final_obscr[w] = obscr[w]
        
        for x in G[w]:
            if x not in final_obscr:
                new_obscr = max(final_obscr[w], G[w][x])
                if x not in obscr:
                    obscr[x] = new_obscr
                    obscr_so_far[x] = new_obscr
                elif new_obscr < obscr[x]:
                    obscr[x] = new_obscr
                    obscr_so_far[x] = new_obscr
    return final_obscr

""" Function used to make links."""

def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	G[node1][node2] = 1	
	if node2 not in G:
		G[node2] = {}
	G[node2][node1] = 1
	return G

""" Function used to make score links. Only creates an edge
    if the existing edge has a greater score. """

def make_scored_link(G, node1, node2, scores, common):
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1000
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1000
    if scores[common] < G[node1][node2]:
        G[node1][node2] = scores[common]
        G[node2][node1] = scores[common]
        
print 'Initializing...'    

tsv = csv.reader(open('C:\Users\owner\Documents\GitHub\Least_Obscure_Path_PS5-3_CS215_Udacity\imdb-1.tsv'),delimiter = '\t')
movies, actors, imdb_graph = {}, {}, {}

print 'Scanning data...'
index = 1
for entry in tsv:
    actor, movie, year = entry
    #actor,movie, year = 
    if movie not in movies: movies[movie] = {}
    if actor not in actors: actors[actor] = {}
    imdb_graph = make_link(imdb_graph, actor, movie)

print 'Calculating obscurity scores...'

tsv2 = csv.reader(open('C:\Users\owner\Documents\GitHub\Least_Obscure_Path_PS5-3_CS215_Udacity\imdb-weights.tsv'),delimiter = '\t')

movies_scores = {}
for entry in tsv2:
    movie, year, money = entry
    money = float(money)
    movies_scores[movie] = money

print 'Generating actor-actor graph and assigning obscurity scores...'

actorG = {}
done = set()
for actor1 in actors:
    done.add(actor1)
    for movie in imdb_graph[actor1]:
        for actor2 in imdb_graph[movie]:
            if actor2 not in done:
                make_scored_link(actorG, actor1, actor2, movies_scores, movie)


test = {(u'Ali, Tony', u'Allen, Woody'): 0.5657,
        (u'Auberjonois, Rene', u'MacInnes, Angus'): 0.0814,
        (u'Avery, Shondrella', u'Dorsey, Kimberly (I)'): 0.7837,
        (u'Bollo, Lou', u'Jeremy, Ron'): 0.4763,
        (u'Byrne, P.J.', u'Clarke, Larry'): 0.109,
        (u'Couturier, Sandra-Jessica', u'Jean-Louis, Jimmy'): 0.3649,
        (u'Crawford, Eve (I)', u'Cutler, Tom'): 0.2052,
        (u'Flemyng, Jason', u'Newman, Laraine'): 0.139,
        (u'French, Dawn', u'Smallwood, Tucker'): 0.2979,
        (u'Gunton, Bob', u'Nagra, Joti'): 0.2136,
        (u'Hoffman, Jake (I)', u'Shook, Carol'): 0.6073,
        ('Kamiki, Ry\xc3\xbbnosuke', u'Thor, Cameron'): 0.3644,
        (u'Roache, Linus', u'Dreyfuss, Richard'): 0.6731,
        (u'Sanchez, Phillip (I)', u'Wiest, Dianne'): 0.5083,
        (u'Sheppard, William Morgan', u'Crook, Mackenzie'): 0.0849,
        (u'Stan, Sebastian', u'Malahide, Patrick'): 0.2857,
        (u'Tessiero, Michael A.', u'Molen, Gerald R.'): 0.2056,
        (u'Thomas, Ken (I)', u'Bell, Jamie (I)'): 0.3941,
        (u'Thompson, Sophie (I)', u'Foley, Dave (I)'): 0.1095,
        (u'Tzur, Mira', u'Heston, Charlton'): 0.3642}





counter = 0

print 'Processing the test case...'

for x,y in test:
        obscr_values = {}
        obscr_values = dijkstra(actorG, x)
        print obscr_values[y], test[(x,y)]
        if obscr_values[y] != test[(x,y)]:
                counter += 1

print counter, ' times a wrong answer was generated.'



answer = {(u'Boone Junior, Mark', u'Del Toro, Benicio'): None,
          (u'Braine, Richard', u'Coogan, Will'): None,
          (u'Byrne, Michael (I)', u'Quinn, Al (I)'): None,
          (u'Cartwright, Veronica', u'Edelstein, Lisa'): None,
          (u'Curry, Jon (II)', u'Wise, Ray (I)'): None,
          (u'Di Benedetto, John', u'Hallgrey, Johnathan'): None,
          (u'Hochendoner, Jeff', u'Cross, Kendall'): None,
          (u'Izquierdo, Ty', u'Kimball, Donna'): None,
          (u'Jace, Michael', u'Snell, Don'): None,
          (u'James, Charity', u'Tuerpe, Paul'): None,
          (u'Kay, Dominic Scott', u'Cathey, Reg E.'): None,
          (u'McCabe, Richard', u'Washington, Denzel'): None,
          (u'Reid, Kevin (I)', u'Affleck, Rab'): None,
          (u'Reid, R.D.', u'Boston, David (IV)'): None,
          (u'Restivo, Steve', u'Preston, Carrie (I)'): None,
          (u'Rodriguez, Ramon (II)', u'Mulrooney, Kelsey'): None,
          (u'Rooker, Michael (I)', u'Grady, Kevin (I)'): None,
          (u'Ruscoe, Alan', u'Thornton, Cooper'): None,
          (u'Sloan, Tina', u'Dever, James D.'): None,
          (u'Wasserman, Jerry', u'Sizemore, Tom'): None}


def generate_answer(answer):
    for x, y in answer:
        obscr_values = {}
        obscr_values = dijkstra(actorG, x)
        answer[(x, y)] = obscr_values[y]
    return answer

print 'Answer to PS5-3 is being generated...'

print generate_answer(answer)






