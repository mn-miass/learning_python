from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id):
        self.id = stream_id
    
    @abstractmethod
    def process_batch(self, data_batch):
        pass
    
    def filter_data(self, data_batch, criteria=None):
        return data_batch
    
    def get_stats(self):
        return {"stream_id": self.id, "type": "unknown"}


class SensorStream(DataStream):
    def process_batch(self, data_batch):
        try:
            name = "temp"
            sum = 0
            data = self.filter_data(data_batch, name)
            if len(data) == 0:
                raise ValueError(f"{name} not found in the data")
            for element in data:
                name, value = element.split(":")
                value = float(value)
                sum += value
            return (f"Sensor analysis: {len(data_batch)} readings processed, avg {name}: {sum/len(data)}°C")
        except ValueError as e:
            if "temp" in e.args[0]:
                return(e.args[0])
            return("The data is not valid")

    def filter_data(self, data_batch, criteria=None):
        if criteria is None:
            return data_batch
        result = []
        for data in data_batch:
            if data.startswith(criteria):
                result.append(data)
        return result
    
    def get_stats(self):
        return {"stream_id": self.id, "type": "Environmental Data"}


class TransactionStream(DataStream):
    def process_batch(self, data_batch):
        pass

    def filter_data(self, data_batch, criteria=None):
        pass
    
    def get_stats(self):
        pass

class EventStream(DataStream):
    pass


class StreamProcessor():
    pass

if __name__ == "__main__":
    pass