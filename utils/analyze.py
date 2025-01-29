import pandas as pd
from evaluatee import Evaluatee


def analyze(evaluatee: list[Evaluatee]):
    data = []
    unique = {e: [] for e in evaluatee}
    best = {e: [] for e in evaluatee}
    for case in evaluatee[0].cases():
        res = [e[case] for e in evaluatee]
        if res.count(None) == len(res) - 1:
            for e in evaluatee:
                if e[case] is not None:
                    unique[e].append(case)

        res = [x for x in res if x is not None]
        if not res:
            continue

        min_res = min(res)
        min_count = res.count(min_res)

        if min_count == 1:
            for e in evaluatee:
                if e[case] == min_res:
                    best[e].append(case)
    for e in evaluatee:
        data.append(
            {
                "Name": e.name,
                "Solved": e.num_solved(),
                "TO": len(e.timeout),
                "MO": len(e.memout),
                "Total": e.num_total(),
                "PAR-2": e.par2(),
                "Unique": len(unique[e]),
                "Best": len(best[e]),
            }
        )

    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    import sys
    evaluatee = []
    for file in sys.argv[1:]:
        evaluatee.append(Evaluatee(file))
    analyze(evaluatee)
