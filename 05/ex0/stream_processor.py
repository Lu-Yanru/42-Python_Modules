from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class that defines the common processing interface."""
    @abstractmethod
    def process(self: "DataProcessor", data: Any) -> str:
        pass

    @abstractmethod
    def validate(self: "DataProcessor", data: Any) -> bool:
        pass

    def format_output(self: "DataProcessor", result: str) -> str:
        """Default formatting that can be overritten."""
        return result


class NumericProcessor(DataProcessor):
    """Specilized class for processing numeric data."""
    def __init__(self: "NumericProcessor") -> None:
        """Instantiates an empty list to store the data."""
        self.data: list[int | float] = []

    def process(self: "NumericProcessor", data: Any) -> str:
        """Process a list of numerics."""
        if self.validate(data) is False:
            return "Not numeric data!"
        self.data = data
        return "Numeric data verified"

    def validate(self: "NumericProcessor", data: Any) -> bool:
        """Validate data type is a list of numeric."""
        if isinstance(data, list) is False:
            return False
        for num in data:
            if not isinstance(num, (int, float)):
                return False
        return True

    def format_output(self: "NumericProcessor", result: str) -> str:
        """Formate output of processing numeric data."""
        if len(self.data) == 0:
            return result
        count = len(self.data)
        total = sum(self.data)
        avg = total / count
        return (f"Processed {count} numeric values, "
                f"sum={total}, avg={avg:.1f}")


class TextProcessor(DataProcessor):
    """Specilized class for processing text data."""
    def __init__(self: "TextProcessor") -> None:
        """Instantiates an empty str to store the data."""
        self.data: str = ""

    def process(self: "TextProcessor", data: Any) -> str:
        """Process a str."""
        if self.validate(data) is False:
            return "Not text data!"
        self.data = data
        return "Text data verified"

    def validate(self: "TextProcessor", data: Any) -> bool:
        """Validate data type is a str."""
        return isinstance(data, str)

    def format_output(self: "TextProcessor", result: str) -> str:
        """Formate output of processing text data."""
        if self.data == "":
            return result
        count = len(self.data)
        words = len(self.data.split(" "))
        return (f"Processed text: "
                f"{count} characters, {words} words")


class LogProcessor(DataProcessor):
    """Specilized class for processing text data."""
    def __init__(self: "LogProcessor") -> None:
        """Instantiates an empty str to store the data."""
        self.data: str = ""

    def process(self: "LogProcessor", data: Any) -> str:
        """Process a str."""
        if self.validate(data) is False:
            return "Not Log data!"
        self.data = data
        return "Log entry verified"

    def validate(self: "LogProcessor", data: Any) -> bool:
        """Validate data type is a str and it starts with ERROR or INFO."""
        if isinstance(data, str) is False:
            return False
        if data[:5] == "ERROR" or data[:4] == "INFO":
            return True
        return False

    def format_output(self: "LogProcessor", result: str) -> str:
        """Formate output of processing text data."""
        if self.data == "":
            return result
        if self.data[:5] == "ERROR":
            return ("[ALERT] ERROR level detected: "
                    f"{self.data[7:]}")
        elif self.data[:4] == "INFO":
            return ("[INFO] INFO level detected: "
                    f"{self.data[6:]}")
        return result


def main() -> None:
    """Testing data processors."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    num_dat = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_dat}")
    num_proc = NumericProcessor()
    print(f"Validation: {num_proc.process(num_dat)}")
    print(f"Output: {num_proc.format_output("")}")

    print("\nInitializing Text Processor...")
    str_dat = "Hello Nexus World"
    print(f"Processing data: {str_dat}")
    str_proc = TextProcessor()
    print(f"Validation: {str_proc.process(str_dat)}")
    print(f"Output: {str_proc.format_output("")}")

    print("\nInitializing Log Processor...")
    log_dat = "ERROR: Connection timeout"
    print(f"Processing data: {log_dat}")
    log_proc = LogProcessor()
    print(f"Validation: {log_proc.process(log_dat)}")
    print(f"Output: {log_proc.format_output("")}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    dataset = [
        [1, 2, 3],
        "Hello Nexus!",
        "INFO: System ready"
    ]
    i = 1
    for processor, data in zip(processors, dataset):
        processor.process(data)
        print(f"Result {i}: {processor.format_output("")}")
        i += 1

    print("\nFoundation system online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
