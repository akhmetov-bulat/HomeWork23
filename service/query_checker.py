import os.path

from constants import BASE_DIR, DATA_DIR


class UserQuery:
    def __init__(self, user_query_dict):
        self.file_name = user_query_dict["file_name"]
        self.cmd1 = user_query_dict["cmd1"]
        self.cmd2 = user_query_dict["cmd2"]
        self.value1 = user_query_dict["value1"]
        self.value2 = user_query_dict["value2"]

    @property
    def file_name(self):
        return self._file_name

    @property
    def cmd1(self):
        return self._cmd1

    @property
    def cmd2(self):
        return self._cmd2

    @property
    def value1(self):
        return self._value1

    @property
    def value2(self):
        return self._value2

    @file_name.setter
    def file_name(self, value):
        if value == "":
            raise ValueError("File name is empty")
        file_path = os.path.join(DATA_DIR, value)
        if not os.path.exists(file_path):
            raise ValueError("File name is wrong")
        self._file_name = file_path

    @cmd1.setter
    def cmd1(self, value):
        if value == "":
            raise ValueError("no command")
        elif value not in ("filter", "map", "unique", "sort", "limit"):
            raise ValueError("Command name is wrong")
        self._cmd1 = value

    @value1.setter
    def value1(self, value):
        if self.cmd1 == "filter":
            if value == "":
                raise ValueError("Query value cannot be blank")
        if self.cmd1 == "map":
            if value not in ["0","1","2","3","4"]:
                raise ValueError("No such column")
        if self.cmd1 == "unique":
            if value != "":
                raise ValueError("Query value must be blank")
        if self.cmd1 == "sort":
            if value not in ["asc", "desc"]:
                raise ValueError("Query must be 'asc', 'desc'" )
        if self.cmd1 == "limit":
            if not isinstance(value, int):
                raise ValueError("Query must be Integer")
        self._value1 = value

    @cmd2.setter
    def cmd2(self, value):
        if value != "":
            if value not in ("filter", "map", "unique", "sort", "limit"):
                raise ValueError("Command name is wrong")
        self._cmd2 = value

    @value2.setter
    def value2(self, value):
        if self.cmd2 != "":
            if self.cmd2 == "filter" and value == "":
                raise ValueError("Query value cannot be blank")
            if self.cmd2 == "map" and value not in [1, 2, 3, 4, 5]:
                raise ValueError("No such column")
            if self.cmd2 == "unique" and value != "":
                raise ValueError("Query value must be blank")
            if self.cmd2 == "sort" and value not in ["asc", "desc"]:
                raise ValueError("Query must be 'asc', 'desc'")
            if self.cmd2 == "limit" and not isinstance(value, int):
                raise ValueError("Query must be Integer")
            self._value2 = value
        else:
            self._value2 = ""
