import sys

if __name__ == "__main__":
    data = {}
    for file in sys.argv[1:]:
        print(file)
        with open(file, 'r') as f:
            for line in f:
                case, time = line.strip().split()
                if case.endswith("aag"):
                    case = case[:-4]
                if case.endswith("aig"):
                    case = case[:-4]
                if case.endswith("btor2"):
                    case = case[:-6]
                case = case.split('/')[-1]
                if case in data:
                    data[case].append(time)
                else:
                    data[case] = [time]
    with open("merge-result", 'w') as result:
        keys = sorted(data.keys())
        for key in keys:
            if len(data[key]) == len(sys.argv[1:]):
                output = f"{key} "
                output += " ".join(str(element) for element in data[key])
                result.write(output + '\n')
