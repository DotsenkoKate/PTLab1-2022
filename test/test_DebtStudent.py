# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DebtStudent import DebtStudent
import pytest

RatingsType = dict[str, float]


class TestDebtStudent:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data = {
            'Иванов Иван Иванович': [
                ('геометрия', 60),
                ('физика', 70),
                ('программирование', 81)
            ], 'Петров Петр Петрович': [
                ('математика', 100),
                ('история', 87),
                ('социология', 91)
            ], 'Васильев Василий Васильевич': [
                ('математика', 100),
                ('физика', 100),
                ('английский', 100)
            ], 'Сидоров Сидор Сидорович': [
                ('информатика', 56),
                ('математика', 55),
                ('основы ооп', 95)
            ]
        }

        result = [3]

        return data, result


def test_init(self, input_data: tuple[DataType, RatingsType]):
    debt = DebtStudent(input_data[0])

    assert debt.data == input_data[0]


def test_calc(self, input_data: tuple[DataType, RatingsType]):
    result = DebtStudent(input_data[0]).calc()

    assert result == input_data[1]
