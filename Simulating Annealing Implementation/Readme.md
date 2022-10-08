# Hunt and Hunter problem with Simulating Annealing 

In this problem we have a list of hunt and hunter animals that said us which animal hunt another and then we should sort a list that a hunter and hunt are in a right situation ( if animal 2 hunt 4 so 2 must become sooner in our list )

## Description

For example we have this list
<p>1 2</p>
<p>3 1</p>
<p>3 2</p>
<p>4 1</p>
<p>4 2</p>
<p>4 3</p>
So it means our output must be like this : 4 3 1 2

### How simulating annealing algorithm work:
* at first we should finding the objective function
* then we find a predictive neighbour of a random index
* then we should check objective function of this two data sest
* if the neighbour has better objective function we should swap the solution set by neighbour set
* and we continuous until the T value become zero
## Getting Started

### Dependencies

* It's need some python notebook like jupyter or google colab

### Installing

* install<a href="https://jupyter.org/"> jupyter notebook</a>
* or using <a href="https://colab.research.google.com/">google colab</a>

### Executing program

* use the run butten or (ctrl + Enter) in each code bocks
* run sequentially

## Authors

ex. Amirmahdi Abootalebi [Linkdin](https://www.linkedin.com/in/amirmahdi-abootalebi/)
