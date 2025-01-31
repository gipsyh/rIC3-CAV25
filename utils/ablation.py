from evaluatee import Evaluatee
from analyze import analyze


ric3 = Evaluatee("./result/rIC3-ic3.txt")
ric3_ms = Evaluatee("./result/rIC3-ic3-ms.txt")
ric3_ctg = Evaluatee("./result/rIC3-ic3-ctg.txt")
ric3_inn = Evaluatee("./result/rIC3-ic3-inn.txt")
ric3_la = Evaluatee("./result/rIC3-ic3-la.txt")

evaluatee = [
    ric3,
    ric3_ms,
    ric3_ctg,
    ric3_inn,
    ric3_la,
]
analyze(evaluatee)
