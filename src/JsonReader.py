# -*- coding: utf-8 -*-
from DataReader import DataReader
from Types import DataType

import json


class JsonReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return {name: [(subject, score) for subject, score in scores.items()]
                for name, scores in data.items()}