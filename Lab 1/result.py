"""File to parse the output for Part3 from Part3OutputInfo.txt file
average the run time and nodes explored information and print it out to the console"""
with open('Part3OutputInfo.txt') as f:
    lines = f.readlines()
    out = {
        "L8": {
            "BFS": {"time": 0, "nodes": 0},
            "IDS": {"time": 0, "nodes": 0},
            "h1": {"time": 0, "nodes": 0},
            "h2": {"time": 0, "nodes": 0},
            "h3": {"time": 0, "nodes": 0}
        },
        "L15": {
            "BFS": {"time": 0, "nodes": 0},
            "IDS": {"time": 0, "nodes": 0},
            "h1": {"time": 0, "nodes": 0},
            "h2": {"time": 0, "nodes": 0},
            "h3": {"time": 0, "nodes": 0}
        },
        "L24": {
            "BFS": {"time": 0, "nodes": 0},
            "IDS": {"time": 0, "nodes": 0},
            "h1": {"time": 0, "nodes": 0},
            "h2": {"time": 0, "nodes": 0},
            "h3": {"time": 0, "nodes": 0}
        }
    }

    for line in lines:
        if line.find("Algorithm") != -1:
            line = line[line.find("L"):]
            level = line[:line.find("/")]
            line = line[line.find("Algorithm:") + 11:]
            algo = line[:line.find(" Total")]
            line = line[line.find(":"):]
            if line.find("<<??>>") != -1:
                nodes = -1
            else:
                nodes = int(line[line.find(" "):line.find("Total")].strip())
            line = line[line.find("taken: ") + 7:]
            if line.find(">") == -1:
                line = line.split(" sec ")
                time = int(line[0]) * 1000
                time += int(line[1].strip("\\"))
            else:
                time = -1

            cur_time = out[level][algo]["time"]
            cur_nodes = out[level][algo]["nodes"]
            out[level][algo]["time"] = int(cur_time) + time
            out[level][algo]["nodes"] = int(cur_nodes) + nodes

    for cur in out:
        for alg in ["BFS", "IDS", "h1", "h2", "h3"]:
            cur_time = out[cur][alg]["time"]
            cur_nodes = out[cur][alg]["nodes"]
            if int(cur_time) > -1 and int(cur_nodes) > -1:
                out[cur][alg]["time"] = int(cur_time) / 20
                out[cur][alg]["nodes"] = int(cur_nodes) / 20
            else:
                out[cur][alg]["time"] = -10
                out[cur][alg]["nodes"] = -10

    print(out)

