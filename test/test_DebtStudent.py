# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DebtStudent import DebtStudent
import pytest


class TestDebtStudent:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
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

        result = 2

        return data, result

    def test_init(self, input_data: tuple[DataType, int]):
        debt = DebtStudent(input_data[0])

        assert debt.data == input_data[0]

    def test_calc(self, input_data: tuple[DataType, int]):
        result = DebtStudent(input_data[0]).calc()

        assert result == input_data[1]
