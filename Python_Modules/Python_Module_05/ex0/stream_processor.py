from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

    @abstractmethod
    def validate(self, data):
        pass

    def format_output(self, result):
        print(f"Output: {result}")


class NumericProcessor(DataProcessor):

    def process(self, data):
        print (f"Processing data: {data}")
        sum_data = 0
        try:
            for value in data:
                num = int(value)
                sum_data += num
        except:
            return("Invalid data was given")
        else :
            count_data = len(data)
            return(f"Processed {count_data} numeric values, sum={sum_data}, avg={sum_data/len(data)}")
            
    def validate(self, data):
        return(isinstance(data, list))


class TextProcessor(DataProcessor):

    def process(self, data):
        print(f"Processing data: {data}")
        return (f"Processed text: {len(data)} characters, {len(data.split())} words")
    
    def validate(self, data):
        return (isinstance(data, str))


class LogProcessor(DataProcessor):
    def process(self, data):
        print(f"Processing data: {data}")
        splited = data.split(":")
        return(f"[ALERT] {splited[0]} level detected:{splited[1]}")
        
    
    def validate(self, data):
        return(isinstance(data, str))



if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric = NumericProcessor()
    print("Initializing Numeric Processor...")
    output = numeric.process([1, 2, 3, 4, 5])
    if numeric.validate([1, 2, 3, 4, 5]):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data not verified")
    numeric.format_output(output)

    text = TextProcessor()
    print("\nInitializing Numeric Processor...")
    output = text.process("Hello Nexus World")
    if text.validate("Hello Nexus World"):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data not verified")
    text.format_output(output)

    log = LogProcessor()
    print("\nInitializing Log Processor...")
    output = log.process("ERROR: Connection timeout")
    if log.validate("Hello Nexus World"):
        print("Validation: Log data verified")
    else:
        print("Validation: Text data not verified")
    log.format_output(output)

