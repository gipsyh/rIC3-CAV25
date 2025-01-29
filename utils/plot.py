import matplotlib.pyplot as plt
from evaluatee import Evaluatee
import sys


def plot_single(fg, e: Evaluatee, line=None):
    data = list(e.data.values())
    data = sorted(data)
    X = []
    Y = []
    for t in range(0, e.TIMEOUT + 1, 30):
        X.append(t)
        Y.append(sum(1 for d in data if d <= t))

    fg.plot(
        X,
        Y,
        label=e.name,
        linestyle=line,
        linewidth=1.3,
        markerfacecolor="none",
    )


def plot(evaluatee: list[Evaluatee], output = "plot.png"):
    fig, (ax1) = plt.subplots(1, 1, figsize=(8, 3.8))
    line = [
        "-",
        "-.",
        ":",
        (0, (3, 3)),
        (0, (5, 5)),
        (0, (3, 5, 1, 5)),
        (0, (7, 7)),
        (0, (3, 1, 1, 1, 1, 1)),
    ]
    if len(line) < len(evaluatee):
        line.extend([None] * (len(evaluatee) - len(line)))
    for e, l in zip(evaluatee, line):
        plot_single(ax1, e, l)
    max_sol = max(e.num_solved() for e in evaluatee)
    min_sol = min(e.num_solved() for e in evaluatee)
    ax1.set_xlabel("Time(s)")
    ax1.set_ylabel("Cases Solved")
    ax1.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", frameon=False)
    ax1.set_ylim(min_sol * 0.5, max_sol + 20)
    plt.subplots_adjust(right=0.7)
    plt.show()
    plt.savefig(output, dpi=400)


if __name__ == "__main__":
    evaluatee = []
    for file in sys.argv[1:]:
        evaluatee.append(Evaluatee(file))
    plot(evaluatee)
