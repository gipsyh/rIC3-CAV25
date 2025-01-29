import matplotlib.pyplot as plt
from scipy.stats import gmean
from evaluatee import Evaluatee
import math
import numpy as np


def cal_ticks(max_val):
    loc = [0.1, 1]
    lab = ["0.1", "1"]
    exp = 1
    now = 10
    while now < max_val:
        lab.append(r"$10^" + str(exp) + "$")
        loc.append(now)
        now *= 10
        exp += 1
    lab.append("TO")
    loc.append(max_val)
    return loc, lab


def scatter_single(fg, x: Evaluatee, y: Evaluatee):
    X = []
    Y = []
    num_x = 0
    num_y = 0
    speedup = []
    for case in x.cases():
        xt, yt = x[case], y[case]
        if xt is None and yt is None:
            continue
        bsdp = xt is None or yt is None
        xt = x.TIMEOUT if xt is None else max(xt, 0.1)
        yt = y.TIMEOUT if yt is None else max(yt, 0.1)
        X.append(xt)
        Y.append(yt)
        if xt <= 3 and yt <= 3:
            continue
        if not bsdp:
            # if yt > xt:
            #     print(f"{case} {yt} > {xt}")
            speedup.append(yt / xt)
        if xt < yt:
            num_x += 1
        elif xt > yt:
            num_y += 1

    print(num_x, num_y)
    gm = gmean(speedup)
    print(1 / gm)
    fg.scatter(X, Y, marker="x", s=25, linewidths=1)
    fg.set_aspect("equal")
    fg.set_xscale("log")
    fg.set_yscale("log")
    fg.set_xlabel(x.name, fontsize=12)
    fg.set_ylabel(y.name, fontsize=12)
    fg.yaxis.set_label_coords(-0.11, 0.5)
    fg.set_xlim(0.1, x.TIMEOUT * 1.2)
    fg.set_ylim(0.1, y.TIMEOUT * 1.2)
    fg.plot([0, x.TIMEOUT], [0, y.TIMEOUT], color="grey", linestyle="dashed")
    # fg.plot([0, x.TIMEOUT], [0, y.TIMEOUT * gm], linestyle='dashed', color="#721454")
    loc, lab = cal_ticks(x.TIMEOUT)
    fg.set_xticks(loc, lab)
    fg.set_yticks(loc, lab)


def scatter(evaluatee: list[Evaluatee], plot_x=4, output="scatter.png"):
    plot_x = 3
    plot_y = int(math.ceil((len(evaluatee) - 1) / plot_x))
    fig, ax = plt.subplots(plot_y, plot_x, figsize=(4 * plot_x, 4 * plot_y))
    if isinstance(ax[0], list) or isinstance(ax[0], np.ndarray):
        ax = [x for sub_ax in ax for x in sub_ax]
    for e, subax in zip(evaluatee[1:], ax):
        scatter_single(subax, evaluatee[0], e)
    plt.tight_layout()
    fig.show()
    fig.savefig(output, dpi=400)


if __name__ == "__main__":
    import sys

    evaluatee = []
    for file in sys.argv[1:]:
        evaluatee.append(Evaluatee(file))
    scatter(evaluatee)
