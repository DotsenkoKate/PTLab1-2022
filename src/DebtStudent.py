from Types import DataType

ResultType = dict[str, float]


class DebtStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> ResultType:
        count = 0

        for key in self.data:
            debt = False
            for subject in self.data[key]:
                if subject[1] < 61:
                    if not debt:
                        count += 1
                    debt = True
        return count
