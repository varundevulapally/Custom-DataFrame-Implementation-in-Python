import csv 

class DataFrame:
    def _init_(self):
        self.frame = {}

    def read_csv(self, filename, names=None, delimiter=","):
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=delimiter)
                data = list(reader)

                if names is not None:
                    columns = names
                else:
                    columns = data.pop(0)  # First row as column names

                self.frame = {col: [] for col in columns}

                for row in data:
                    for col, value in zip(columns, row):
                        self.frame[col].append(value)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def head(self, rows=5):
        print(" | ".join(self.frame.keys()))
        print("-" * 50)
        for index in range(min(rows, len(next(iter(self.frame.values()))))):
            print(" | ".join(f"{str(self.frame[col][index]):<15}" for col in self.frame.keys()))

    def tail(self, rows=5):
        print(" | ".join(self.frame.keys()))
        print("-" * 50)
        total_rows = len(next(iter(self.frame.values())))
        for index in range(max(0, total_rows - rows), total_rows):
            print(" | ".join(f"{str(self.frame[col][index]):<15}" for col in self.frame.keys()))

    def getColumn(self, column):
        if column in self.frame:
            return self.frame[column]
        raise KeyError(f"Column '{column}' does not exist.")

    def getColumns(self, columns):
        return {col: self.frame[col] for col in columns if col in self.frame}

    def addColumn(self, column_name, values):
        if len(values) != len(next(iter(self.frame.values()))):
            raise ValueError("Length of values does not match the number of rows.")
        self.frame[column_name] = values