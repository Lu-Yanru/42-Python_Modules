from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """An abstract base class with core streaming functionality."""
    def __init__(self: "DataStream", stream_id: str) -> None:
        """Initalize an DataStream instance with an id and a list of data."""
        self.id = stream_id
        self.data: List[Any] = []

    @abstractmethod
    def process_batch(self: "DataStream", data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(self: "DataStream", data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Default way to filter data based on criteria."""
        return data_batch

    def get_stats(self: "DataStream") -> Dict[str, Union[str, int, float]]:
        """Default way to return stream statictics."""
        return {"stream_id": self.id, "count": len(self.data)}


class SensorStream(DataStream):
    """Specialized class for sensor stream."""
    def __init__(self: "SensorStream", stream_id: str) -> None:
        """Initialize an SensorStream instance with an id."""
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.id}, Type: Environmental Data")

    def process_batch(self: "SensorStream", data_batch: List[Any]) -> str:
        """Process a batch of sensor data."""
        # Validate data_batch and store in object
        if isinstance(data_batch, List) is False:
            raise TypeError("ERROR: Sensor data "
                            "is not correctly formatted!")

        if len(data_batch) == 0:
            raise ValueError("ERROR: Sensor data is empty!")

        mandatory_keys = ["temp", "humidity", "pressure"]
        for reading in data_batch:
            # Check if each reading is a dict
            if isinstance(reading, Dict) is False:
                raise TypeError("ERROR: Sensor data not corretly formatted!")
            # Check if dict has all the mandatory keys
            for key in mandatory_keys:
                if key not in reading:
                    raise KeyError("ERROR: "
                                   "Sensor data not corretly formatted!")
            for key, value in reading.items():
                # Check if all the present keys are mandatory
                if key not in mandatory_keys:
                    raise KeyError("ERROR: "
                                   "Sensor data not corretly formatted!")
                # Check if values are int or float
                if isinstance(value, (int, float)) is False:
                    raise TypeError("ERROR: "
                                    "Sensor data not corretly formatted!")

        self.data = data_batch

        # Format first sensor reading
        res = "Processing sensor batch: "
        first = data_batch[0]
        temp1 = first["temp"]
        hum1 = first["humidity"]
        press1 = first["pressure"]
        res += f"[temp:{temp1}, humidity:{hum1}, pressure:{press1}]"
        return res

    def filter_data(self: "SensorStream", data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        self.process_batch(data_batch)
        if len(self.data) == 0:
            raise ValueError("ERROR: Sensor data is invalid!")

        filtered: List[Any] = []
        if criteria == "high":
            for reading in self.data:
                temp = reading["temp"]
                if temp > 20:
                    filtered.append(temp)
            return filtered

        return data_batch

    def get_stats(self: "SensorStream") -> Dict[str, Union[str, int, float]]:
        """Get sensor stats"""
        if len(self.data) == 0:
            raise ValueError("ERROR: Sensor data is invalid!")

        res: Dict[str, Union[str, int, float]] = {
            "count": 0,
            "avg_temp": 0.0
        }
        count = len(self.data)
        total_temp = 0.0
        res["count"] = count
        for reading in self.data:
            total_temp += reading["temp"]
        res["avg_temp"] = total_temp / count
        return res


class TransactionStream(DataStream):
    """Specialzed class for transactions stream."""
    def __init__(self: "TransactionStream", stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.id}, Type: Financial Data")

    def process_batch(self: "TransactionStream", data_batch: List[Any]) -> str:
        """Process a batch of transaction data."""
        # Validate data_batch and store in object
        if isinstance(data_batch, List) is False:
            raise TypeError("ERROR: Transaction data "
                            "is not correctly formatted!")

        if len(data_batch) == 0:
            raise ValueError("ERROR: Transaction data is empty!")

        mandatory_keys = ["buy"]
        optional_keys = ["sell"]
        for reading in data_batch:
            # Check if each reading is a dict
            if isinstance(reading, Dict) is False:
                raise TypeError("ERROR: "
                                "Transaction data not corretly formatted!")
            # Check if dict has all the mandatory keys
            for key in mandatory_keys:
                if key not in reading:
                    raise KeyError("ERROR: "
                                   "Transaction data not corretly formatted!")
            for key, value in reading.items():
                # Check if all the present keys are mandatory
                if key not in mandatory_keys and key not in optional_keys:
                    raise KeyError("ERROR: "
                                   "Transaction data not corretly formatted!")
                # Check if values are int or float
                if isinstance(value, int) is False:
                    raise ValueError("ERROR: Transaction data "
                                     "not corretly formatted!")

        self.data = data_batch

        # Format first transaction reading
        res = "Processing transaction batch: "
        first = data_batch[0]
        buy = first["buy"]
        if "sell" in first.keys():
            sell = first["sell"]
            res += f"[buy:{buy}, sell:{sell}]"
        else:
            res += f"[buy:{buy}]"
        return res

    def filter_data(self: "TransactionStream", data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        self.process_batch(data_batch)
        if len(self.data) == 0:
            raise ValueError("ERROR: Transaction data is invalid!")

        filtered: List[Any] = []
        if criteria == "large":
            for reading in self.data:
                for value in reading.values():
                    if value > 80:
                        filtered.append(reading)
                        break
            return filtered

        return data_batch

    def get_stats(self: "TransactionStream") \
            -> Dict[str, Union[str, int, float]]:
        """Get sensor stats"""
        if len(self.data) == 0:
            raise ValueError("ERROR: Transaction data is invalid!")

        res: Dict[str, Union[str, int, float]] = {
            "count": 0,
            "net": 0
        }
        count = len(self.data)
        total_buy = 0
        total_sell = 0
        res["count"] = count
        for reading in self.data:
            total_buy += reading["buy"]
            if "sell" in reading.keys():
                total_sell += reading["sell"]
        res["net"] = total_buy - total_sell
        return res


class EventStream(DataStream):
    """Specialzed class for event stream."""
    def __init__(self: "EventStream", stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.id}, Type: System Events")

    def process_batch(self: "EventStream", data_batch: List[Any]) -> str:
        """Process a batch of system event data."""
        # Validate data_batch and store in object
        if isinstance(data_batch, List) is False:
            raise TypeError("ERROR: System event data "
                            "is not correctly formatted!")

        if len(data_batch) == 0:
            raise ValueError("ERROR: System event data is empty!")

        for event in data_batch:
            if isinstance(event, str) is False:
                raise TypeError("ERROR: System event data "
                                "is not correctly formatted!")

        self.data = data_batch

        # Format all events
        res = "Processing event batch: ["
        i = 0
        count = len(self.data)
        for event in self.data:
            res += event
            if i < count - 1:
                res += ", "
            i += 1
        res += "]"
        return res

    def filter_data(self: "EventStream", data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        self.process_batch(data_batch)
        if len(self.data) == 0:
            raise ValueError("ERROR: System event data is invalid!")

        filtered: List[Any] = []
        if criteria == "error":
            for event in self.data:
                if event.lower() == "error":
                    filtered.append(event)
            return filtered

        return data_batch

    def get_stats(self: "EventStream") \
            -> Dict[str, Union[str, int, float]]:
        """Get sensor stats"""
        if len(self.data) == 0:
            raise ValueError("ERROR: System event data is invalid!")

        errors = self.filter_data(self.data, "error")
        res: Dict[str, Union[str, int, float]] = {
            "count": len(self.data),
            "error": len(errors)
        }
        return res


class StreamProcessor:
    """Handle any stream type."""
    def __init__(self: "StreamProcessor") -> None:
        """
        Instantiate a stream processor
        with an empty list of data streams.
        """
        self.streams: List[DataStream] = []

    def set_streams(self: "StreamProcessor",
                    streams: List[DataStream]) -> None:
        """Add a list of data streams to the stream processor."""
        if isinstance(streams, List) is False:
            raise TypeError("ERROR: Invalid list of data stream!")
        for stream in streams:
            if isinstance(stream, DataStream) is False:
                raise TypeError("ERROR: Invalid list of data stream!")
            self.streams.append(stream)

    def process_all(self: "StreamProcessor",
                    data_batches: List[List[Any]]) -> None:
        """Process all data stream types."""
        for data in data_batches:
            for stream in self.streams:
                try:
                    stream.process_batch(data)
                    stats = stream.get_stats()
                    if isinstance(stream, SensorStream):
                        print(f"- Sensor data: {stats["count"]} "
                              "readings processed")
                    elif isinstance(stream, TransactionStream):
                        print(f"- Transaction data: {stats["count"]} "
                              "operations processed")
                    elif isinstance(stream, EventStream):
                        print(f"- Event data: {stats["count"]} "
                              "events processed")
                    break
                except (TypeError, KeyError, ValueError):
                    continue

    def filter_all(self: "StreamProcessor", data_batches: List[List[Any]],
                   criteria: List[str]) -> None:
        """Filter all data stream types."""
        message = "Filtered results: "

        i = 0
        length = len(data_batches)
        for data in data_batches:
            for stream in self.streams:
                try:
                    stream.process_batch(data)
                    if isinstance(stream, SensorStream):
                        res = stream.filter_data(data, criteria[0])
                        message += f"{len(res)} ciritcal sensor alters"
                    elif isinstance(stream, TransactionStream):
                        res = stream.filter_data(data, criteria[1])
                        message += f"{len(res)} large transaction"
                    elif isinstance(stream, EventStream):
                        res = stream.filter_data(data, criteria[2])
                        message += f"{len(res)} system errors"
                    if i < length - 1:
                        message += ", "
                    break
                except (TypeError, KeyError, ValueError):
                    continue
            i += 1
        print(message)


def main() -> None:
    """Test data stream classes and stream processor."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_dat = [{"temp": 22.5,  "humidity": 65, "pressure": 1013},
                  {"temp": 23.0,  "humidity": 63, "pressure": 1010}]
    sensor_stream = SensorStream("SENSOR_001")
    try:
        print(sensor_stream.process_batch(sensor_dat))
    except (TypeError, KeyError, ValueError) as e:
        print(e)
    try:
        sensor_stats = sensor_stream.get_stats()
        print(f"Sensor analysis: {sensor_stats["count"]} readings processed, "
              f"avg temp: {sensor_stats["avg_temp"]:.1f}°C")
    except ValueError as e:
        print(e)

    print("")
    transaction_dat = [{"buy": 100, "sell": 150},
                       {"buy": 75, "sell": 60},
                       {"buy": 50}]
    transaction_stream = TransactionStream("TRANS_001")
    try:
        print(transaction_stream.process_batch(transaction_dat))
    except (TypeError, KeyError, ValueError) as e:
        print(e)
    try:
        transaction_stats = transaction_stream.get_stats()
        print(f"Transaction analysis: {transaction_stats["count"]} "
              f"operations, net flow: {transaction_stats["net"]} units")
    except ValueError as e:
        print(e)

    print("")
    event_dat = ["login", "error", "logout"]
    event_stream = EventStream("EVENT_001")
    try:
        print(event_stream.process_batch(event_dat))
    except (TypeError, KeyError, ValueError) as e:
        print(e)
    try:
        event_stats = event_stream.get_stats()
        print(f"Event analysis: {event_stats["count"]} events, "
              f"{event_stats["error"]} error detected")
    except ValueError as e:
        print(e)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    filters = ["high", "large", "error"]
    try:
        processor.set_streams([sensor_stream, transaction_stream,
                               event_stream])
        all_dat: List[List[Any]] = []
        all_dat.append(sensor_dat)
        all_dat.append(transaction_dat)
        all_dat.append(event_dat)

        print("\nBatch 1 Results:")
        processor.process_all(all_dat)

        print("")
        print("Stream filtering active: High-priority data only")
        processor.filter_all(all_dat, filters)
    except TypeError as e:
        print(e)

    print("")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
