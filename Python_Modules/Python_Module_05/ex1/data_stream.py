from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    error_count = 0
    large_transaction = 0

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.reading = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for element in data_batch:
                name, value = element.split(":")
                float(value)
                self.reading += 1

            data_need = "temp"
            data_sum = 0

            data = self.filter_data(data_batch, data_need)
            if data == []:
                self.error_count += 1
                return (f"Sensor analysis: {len(data_batch)} readings "
                        f"processed, No {data_need} was found\n")

            for element in data:
                name, value = element.split(":")
                data_sum += float(value)
            self.last_avg = data_sum / len(data)
            self.processed_count += 1
            sen = f"Sensor analysis: {len(data_batch)} readings processed"
            f", avg={data_need} {self.last_avg}"
            if data_need == "temp":
                sen = sen + "°C"
            return sen + "\n"
        except ValueError:
            DataStream.error_count += 1
            return ("INVALID VALUE WAS GIVEN")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            data = []
            if criteria is None:
                return data
            if isinstance(criteria, str) is False:
                raise ValueError("The criteria isn't valid")
            for element in data_batch:
                if criteria + ":" in element:
                    data.append(element)
            return data
        except ValueError as e:
            print(e)
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Sensor", "count": self.reading, "act": "reading",
                "stream_id": self.stream_id, "type": "Environmental Data"}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.operations = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for element in data_batch:
                name, value = element.split(":")
                if name != "buy" and name != "sell":
                    raise ValueError("Only buy and Sell are allowed")
                value = int(value)

            if len(data_batch) > 3:
                DataStream.large_transaction += 1

            data_buy = self.filter_data(data_batch, "buy")
            data_sell = self.filter_data(data_batch, "sell")

            if data_buy == [] or data_sell == []:
                self.error_count += 1
                raise ValueError

            net = 0
            for data in data_buy:
                name, value = data.split(":")
                net += int(value)
                self.operations += 1

            for data in data_sell:
                name, value = data.split(":")
                net -= int(value)
                self.operations += 1

            sen = f"Transaction analysis: {len(data_batch)} "
            "operations, net flow: "
            if net >= 0:
                sen += f"+{net} units"
            else:
                sen += f"{net} units"

            return sen + "\n"

        except ValueError as e:
            print(e)
            return "INVALID VALUE WAS GIVEN"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        try:
            data = []
            if criteria is None:
                return data
            if isinstance(criteria, str) is False:
                raise ValueError("The criteria isn't valid")
            for element in data_batch:
                if criteria + ":" in element:
                    data.append(element)
            return data
        except ValueError as e:
            print(e)
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Transaction", "count": self.operations,
                "act": "operations",
                "stream_id": self.stream_id, "type": "Financial Data"}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.events_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data_error = self.filter_data(data_batch, "error")
            self.events_count += len(data_batch)
            if data_error[0] == "hh":
                self.error_count += 1
                raise ValueError
            if len(data_error) == 0:
                sen = f"Event analysis: {len(data_batch)} events, "
                "no error detected"
            else:
                DataStream.error_count += 1
                sen = f"Event analysis: {len(data_batch)} events, "
                f"{len(data_error)} error detected"
            return sen + "\n"
        except ValueError:
            return "INVALID VALUE WAS GIVEN\n"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        try:
            data = []
            if criteria is None:
                return data
            if isinstance(criteria, str) is False:
                raise ValueError("The criteria isn't valid")
            for element in data_batch:
                if isinstance(element, str) is False:
                    raise ValueError("INVALID VALUE WAS GIVEN\n")
                if criteria == element:
                    data.append(element)
            return data
        except ValueError as e:
            if e.args[0] != "INVALID VALUE WAS GIVEN\n":
                print(e)
            return ["hh"]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"name": "Event", "count": self.events_count, "act": "events",
                "stream_id": self.stream_id, "type": "System Events"}


class StreamProcessor():
    counter = 0

    def __init__(self, list_obj: list[str], list_data: list[str]) -> None:
        self.list_obj = list_obj
        self.list_data = list_data
        self.batch = StreamProcessor.counter
        StreamProcessor.counter += 1

    def process_streams_ununified(self) -> None:
        i = 0
        try:
            while i < len(self.list_data):
                stats = self.list_obj[i].get_stats()
                print(f"Initializing {stats['name']} Stream...")
                print(f"Stream ID: {stats['name']}, Type: {stats['type']}")
                print(f"Processing {stats['name']} batch: {self.list_data[i]}")
                msg = self.list_obj[i].process_batch(self.list_data[i])
                print(msg)
                i += 1

        except IndexError:
            print("limit was exceeded")

    def process_streams_unified(self) -> None:
        print("Processing mixed stream types through unified interface...\n")
        print(f"Batch {self.batch} Results:")

        i = 0
        while i < len(self.list_obj):
            list_obj[i].process_batch(list_data[i])
            value = list_obj[i].get_stats()
            print(f"- {value['name']} data: {value['count']} "
                  f"{value['act']} processed")
            i += 1
        print()

    def filter_stream(self) -> None:
        print("Stream filtering active: High-priority data only")
        print(f"Filtered results: {DataStream.error_count} "
              f"critical sensor alerts,"
              f" {DataStream.large_transaction} large transaction\n")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_a = SensorStream("SENSOR_001")
    transaction_a = TransactionStream("TRANS_001")
    event_a = EventStream("EVENT_001")

    list_obj = [sensor_a, transaction_a, event_a]
    list_data = [["tmp:22.5", "humidity:65", "pressure:1013"],
                 ["buy:100", "sell:150", "buy:75"],
                 ["login", "error", "logout"]]

    process_a = StreamProcessor(list_obj, list_data)
    process_a.process_streams_ununified()

    print("=== Polymorphic Stream Processing ===")

    sensor_b = SensorStream("SENSOR_002")
    transaction_b = TransactionStream("TRANS_002")
    event_b = EventStream("EVENT_002")

    list_obj = [sensor_b, transaction_b, event_b]
    list_data = [["tmp:22.5", "pressure:1013"],
                 ["buy:100", "sell:150", "buy:75", "sell:32"],
                 ["login", "error", "logout"]]

    process_b = StreamProcessor(list_obj, list_data)
    process_b.process_streams_unified()
    process_b.filter_stream()
    print("All streams processed successfully. Nexus throughput optimal.")
