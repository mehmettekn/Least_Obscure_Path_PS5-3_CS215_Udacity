This program is the solution to PS5-3 of CS215 at Udacity.com

This program calculates least obscure path between two nodes.
It reads and generates graphs from imdb files. Obscurity scores assigned movies
are multiplicative inverse of money the movie made. The program finds the least
obscure path between two actors based on the movies actors appeared in. The program
uses an implementation of dijkstra algoritm to find the least obscure path.

priority_dict class was used to  implement heaps efficiently. The class makes it
possible to update the dictionary key values in constant time. The class was taken from
the url given below.

http://code.activestate.com/recipes/522995/