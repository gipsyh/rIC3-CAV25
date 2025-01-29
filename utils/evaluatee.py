import os
from typing import Dict, Optional, Union


class Evaluatee:
    TIMEOUT = 3600

    def __init__(self, file: os.PathLike, name: Optional[str] = None):
        self.name = (
            name if name is not None else os.path.splitext(os.path.basename(file))[0]
        )
        self.data: Dict[str, float] = {}
        self.timeout = set()
        self.memout = set()
        with open(file, "r") as file:
            for line in file:
                case, time = line.strip().split()
                case = case.rsplit("/", 1)[-1]
                case = case.rsplit(".", 1)[0] if "." in case else case
                if time == "Timeout":
                    self.timeout.add(case)
                elif time == "Failed":
                    self.memout.add(case)
                else:
                    time = float(time)
                    if time > self.TIMEOUT:
                        self.timeout.add(case)
                    else:
                        self.data[case] = time

    def __getitem__(self, key):
        return self.data.get(key)

    def cases(self) -> list[str]:
        return list(self.data.keys() | self.timeout | self.memout)

    def num_solved(self) -> int:
        return len(self.data)

    def num_failed(self) -> int:
        return len(self.timeout) + len(self.memout)

    def num_total(self) -> int:
        return self.num_solved() + self.num_failed()

    def par2(self) -> float:
        return round(
            (sum(self.data.values()) + self.num_failed() * 2 * self.TIMEOUT)
            / self.num_total(),
            2,
        )

    def summary(self):
        print(
            self.name,
            "{}/{}".format(self.num_solved(), self.num_total()),
            "par2: {:.2f}".format(self.par2()),
        )
