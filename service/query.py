
from service.query_checker import UserQuery


class QueryService(UserQuery):
    def get_result(self):
        gen1 = self._read_file()
        result1 = self._run_cmd(self.cmd1, self.value1, gen1)
        if self.cmd2:
            gen2 = iter(result1)
            result2 = self._run_cmd(self.cmd2, self.value2, gen2)
            return result2
        return result1

    def _run_cmd(self, cmd, value, gen):
        if cmd == "filter":
            return list(filter(lambda x: value in x, gen))
        if cmd == "map":
            return list(map(lambda x: x.split(" ")[int(value)], gen))
        if cmd == "unique":
            return list(set(x for x in gen))
        if cmd == "sort":
            if value == "asc":
                return sorted(list(x for x in gen), reverse=False)
            return sorted(list(x for x in gen), reverse=True)
        if cmd == "limit":
            i = 0
            result = []
            while i < value:
                result.append(next(gen))
                i += 1
            return result

    def _read_file(self):
        with open(self.file_name) as f:
            while True:
                try:
                    line = next(f)
                except StopIteration:
                    break
                yield line
