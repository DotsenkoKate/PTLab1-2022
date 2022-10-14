from Types import DataType

RatingType = dict[str, float]


class DebtStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> RatingType:
        count = 0

        for key in self.data:
            debt = False
            for subject in self.data[key]:
                if subject[1] < 61:
                    if not debt:
                        count += 1
                    debt = True
        return count
