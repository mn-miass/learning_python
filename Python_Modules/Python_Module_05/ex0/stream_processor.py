from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            sum_data = 0
            if self.validate(data) is False:
                raise ValueError("Validation: Numeric data verification"
                                 " failed")
            for element in data:
                sum_data += element
            return (f"Processed {len(data)} numeric values, "
                    f"sum={sum_data}, avg={sum_data/len(data)}")

        except ValueError as e:
            print(e)
            return ("The data was not valid")

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, list) is False:
                return False
            for element in data:
                if isinstance(element, int) is False:
                    raise ValueError
            return True
        except ValueError:
            return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if self.validate(data) is False:
                raise ValueError("Validation: Text data verification failed")
            words = data.split()
            return (f"{len(data)} characters, {len(words)} words")
        except ValueError as e:
            print(e)
            return ("The data was not valid")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return (f"Output: Processed text: {result}")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if self.validate(data) is False:
                raise ValueError("Validation: Log entry failed")
            msg = data.split(":")
            if msg[0] != "ERROR" and msg[0] != "INFO":
                raise ValueError("Validation: Log entry failed")
            if msg[0] == "ERROR":
                return (f"[ALERT] {msg[0]} level detected:{msg[1]}")
            elif msg[0] == "INFO":
                return (f"[INFO] {msg[0]} level detected:{msg[1]}")

        except ValueError as e:
            print(e)
            return ("The data was not valid")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return (f"Output {result}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    numeric = NumericProcessor()
    if numeric.validate(data):
        print("Validation: Numeric data verified")
    s = numeric.process(data)
    s = numeric.format_output(s)
    print(s)
    print()

    print("Initializing Text Processor...")
    data = "Hello Nexus World"
    print(f"Processing data: {data}")
    text = TextProcessor()
    if text.validate(data):
        print("Validation: Text data verified")
    s = text.process(data)
    s = text.format_output(s)
    print(s)
    print()

    print("Initializing Log Processor...")
    data = "ERROR: Connection timeout"
    print(f"Processing data: {data}")
    log = LogProcessor()
    if log.validate(data):
        print("Validation: Log entry verified")
    s = log.process(data)
    s = log.format_output(s)
    print(s)
    print()

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    s1 = numeric.process([1, 2, 3])
    s2 = text.process("Hello World")
    s3 = log.process("INFO: System ready")

    print(f"Result 1: {s1}")
    print(f"Result 2: {s2}")
    print(f"Result 3: {s3}")
