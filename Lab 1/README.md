# Lab 1 - CS 472
Author: Polina Semenova <br>

Contains Breath First Search (BFS), Iterative Deepening Search (IDS), and A* search with 3 different heuristics. 

The project runs the search algorithms on an 8-Puzzle Game to find the optimal path for the solution. 
# Structure of the Project
Python Files:
* 8puz.py
  * Main file to compile program
* node.py
  * Code from https://github.com/aimacode/aima-python
  * implemented h2 and h3 methods for the heuristics
* search.py
  * Code from https://github.com/aimacode/aima-python
  * contains the search algorithms
* result.py
  * the code to analyze the average runtime and nodes explored 
  * if the output time and nodes are -1, this means that the algorithm timed out at 15 min and the result could not be computed

Folders:
* Part2
* Part3

Text Files:
* notSolvable.txt
  * contains a puzzle that cannot be solved
* Part2Output.txt
  * contains the information for all the puzzles in part 2 with the correct algorithm information 
* Part3Output.txt
  * contains the table for average run time (microseconds) and average number of nodes explored
  * contains the observations for the performance of the different algorithms
* Part3OutputInfo.txt
  * contains the information for all the puzzles in part 3

## Compile/Run Guide
To Run the Part2 or Part3 files uncomment the desired  line in the `run.sh` file and then run the following commands:

    chmod +x run.sh
    ./run.sh

To run individual text files:
- The algorithms allowed are: (BFS/IDS/h1/h2/h3)


    python3 8puz.py --fPath 140173.txt --alg BFS

To reproduce the average time and nodes explored, run the above `./run.sh` command on all the Part3 puzzles to save them to the appropriate file then run:

    python3 result.py

to get the averages of the output. 