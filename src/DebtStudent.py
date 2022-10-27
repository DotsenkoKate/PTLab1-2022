from Types import DataType


class DebtStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0

        for key in self.data:
            debt = False
            print(key)
            for subject in self.data[key]:
                if subject[1] < 61:
                    if not debt:
                        count += 1
                    debt = True
        return count
