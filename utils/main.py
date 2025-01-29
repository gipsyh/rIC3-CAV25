from evaluatee import Evaluatee
from plot import plot
from scatter import scatter
from analyze import analyze


ric3 = Evaluatee("./result/rIC3-ic3.txt")
abc = Evaluatee("./result/ABC-pdr.txt")
ic3ref = Evaluatee("./result/IC3ref.txt")
nuxmv_cav23 = Evaluatee("./result/nuXmv-cav23.txt")
avr = Evaluatee("./result/AVR-ic3sa.txt")
avy = Evaluatee("./result/Avy.txt")
pono_ic3ia = Evaluatee("./result/Pono-ic3ia.txt")
pono_ic3sa = Evaluatee("./result/Pono-ic3sa.txt")

evaluatee = [
    ric3,
    nuxmv_cav23,
    abc,
    avy,
    ic3ref,
    avr,
    pono_ic3ia,
    pono_ic3sa,
]
analyze(evaluatee)
plot(evaluatee)
scatter(evaluatee[:4])

ric3_portfolio = Evaluatee("./result/rIC3-portfolio.txt")
abc_superprove = Evaluatee("./result/ABC-superprove.txt")
pavy = Evaluatee("./result/Pavy.txt")
avr_portfolio = Evaluatee("./result/AVR-portfolio.txt")
pono_portfolio = Evaluatee("./result/Pono-portfolio.txt")

evaluatee = [ric3_portfolio, abc_superprove, pavy, avr_portfolio, pono_portfolio]
analyze(evaluatee)
plot(evaluatee, output="portfolio-plot.png")
scatter(evaluatee[:4], output="portfolio-scatter.png")
