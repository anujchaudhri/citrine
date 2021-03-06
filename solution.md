The challenge problem is to generate sample vectors in an 'n-dimensional' unit hypercube with arbitrary number of constraints that effectively cover the whole space.

For this problem, I chose a simple strategy that involves arbitrarily generating sample 'n-dimensional' vectors in a unit hypercube using the 'Latin Hypercube Sampling-LHS' statistical method and choosing vectors from these that satisfy the constraints. 

1. Given the dimensionality of the space and the constraints file, the code generates ten times the number of samples in each run using the LHS method.
2. The sample vectors are then tested against the given constraints from the constraints file and sorted based on whether they satisfy all the constraints or not.
3. The vectors that satisfy the constraints are stored separately.
4. The process is repeated till the desired number of samples are obtained.

The algorithm is quite efficient for low dimensional spaces with arbitrary number of constraints (mixture.txt, example.txt and formulation.txt)

It takes less than a hundreth of a second to generate outputs for input files-mixture.txt and example.txt and less than 20 seconds for formulation.txt. The generated samples cover the space very effectively as can be seen by plotting the output vectors. For higher dimensional spaces, for ex. 4-dim space, generate plots using 2 coordinates at a time. It needs to be pointed out that the algorithm has not been very efficient in generating samples for alloy.txt in the stipulated time frame of 5 minutes and remains a work in progress in that regard. 
