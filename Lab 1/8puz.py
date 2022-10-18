# to run ==> python3 8puz.py --fPath Part2/S1.txt --alg h2
"""
    @Author Polina Semenova
"""
import getopt
import signal
from search import *
import datetime


def main(argv):
    """Main method to run the program
    gets the path and algorithm from the user
    executes the desired algorithm on the given puzzle
    saves the information about the run to a file"""
    file = ''
    algorithm = ''

    opts, args = getopt.getopt(argv, "f:a:", ["fPath=", "alg="])
    for opt, arg in opts:
        if opt in ("-f", "--fPath"):
            file = arg
        if opt in ("-a", "--alg"):
            algorithm = arg

    with open(file) as f:
        input_file = f.read()
        input_problem = input_file.split()

    problem = []
    for i in input_problem:
        if i != '_':
            problem.append(int(i))
        else:
            problem.append(0)

    puzzle = EightPuzzle(tuple(problem))

    if not puzzle.check_solvability(tuple(problem)):
        f = open("Part2Output.txt", "a")
        f.write("File: " + file + " -- Algorithm: " + algorithm + "\nThe inputted puzzle is not solvable:\n")
        f.write(input_file)
        f.write("-----------\n")
        f.close()
        print("The inputted puzzle is not solvable:")
        print(input_file)
        return

    def signal_handler():
        raise Exception("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(900)  # 15 min
    try:
        start = datetime.datetime.now()
        node = run_algorithm(algorithm, puzzle)
        end = datetime.datetime.now()
    except Exception:
        write_result2(file=file, algorithm=algorithm)
        print("Total nodes generated:  <<??>> Total time taken: >15 min Path length: Timed out. Path: Timed out.")
        return

    timediff = (end - start).total_seconds()

    print("Total nodes generated:", puzzle.total_nodes)
    print("Total time taken:", int(timediff), "sec", int((timediff - int(timediff)) * 1000), "microSec")
    print("Path length:", len(node.solution()))
    print("Path:", node.solution())

    if file.find("Part2") != -1:
        write_result2(puzzle, file, algorithm, node, timediff)
    else:
        write_result3(puzzle, file, algorithm, timediff)


def run_algorithm(algorithm, puzzle):
    """Function to run the desired algorithm"""
    node = None
    if algorithm.upper() == 'BFS':
        node = breadth_first_graph_search(puzzle)
    elif algorithm.upper() == 'IDS':
        node = iterative_deepening_search(puzzle)
    elif algorithm.lower() == 'h1':
        node = astar_search(puzzle)
    elif algorithm.lower() == 'h2':
        node = astar_search(puzzle, puzzle.h2)
    elif algorithm.lower() == 'h3':
        node = astar_search(puzzle, puzzle.h3)
    return node


def write_result2(puzzle="<<??>>", file="", algorithm="", node="Timed out.", timediff=">15 min"):
    """Helper function to save the Part2 puzzle outputs to a file"""
    f = open("Part2Output.txt", "a")
    f.write("File: " + file + " -- Algorithm: " + algorithm)
    if puzzle != "<<??>>":
        f.write("\nTotal nodes generated: " + str(puzzle.total_nodes))
    else:
        f.write("\nTotal nodes generated: " + puzzle)

    f.write("\nTotal time taken: ")

    if timediff != ">15 min":
        f.write(str(int(timediff)) + " sec " + str(int((timediff - int(timediff)) * 1000)))
    else:
        f.write(timediff)

    if node != "Timed out.":
        f.write("\nPath length: " + str(len(node.solution())))
        f.write("\nPath: " + str(node.solution()))
    else:
        f.write("\nPath length: " + str(node))
        f.write("\nPath: " + str(node))
    f.write("\n-----------\n")
    f.close()


def write_result3(puzzle="<<??>>", file="", algorithm="", timediff=">15 min"):
    """Helper function to save the Part3 puzzle output to a file"""
    f = open("Part3OutputInfo.txt", "a")
    f.write("File: " + file + " - Algorithm: " + algorithm)
    if puzzle != "<<??>>":
        f.write("\nTotal nodes generated: " + str(puzzle.total_nodes))
    else:
        f.write("\nTotal nodes generated: " + puzzle)
    f.write("\nTotal time taken: ")
    if timediff != ">15 min":
        f.write(str(int(timediff)) + " sec " + str(int((timediff - int(timediff)) * 1000)))
    else:
        f.write(timediff)
    f.write("\n-----------\n")
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
