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
        if len(data_batch) == 0:
            raise ValueError("ERROR: Sensor data is empty!")

        mandatory_keys = ["temp", "humidity", "pressure"]
        for reading in data_batch:
            # Check if each reading is a dict
            if isinstance(reading, Dict) is False:
                raise TypeError("ERROR: Sensor data not corretly formatted!")
            # Check if dict hass all the mandatory keys
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
                    raise ValueError("ERROR: "
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

    def filter_data(self: DataStream, data_batch: List[Any], criteria: str | None = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self: "DataStream") -> Dict[str, Union[str, int, float]]:
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

    def process_batch(self: DataStream, data_batch: List[Any]) -> str:
        return super().process_batch(data_batch)

    def filter_data(self: DataStream, data_batch: List[Any], criteria: str | None = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self: DataStream) -> Dict[str, str | int | float]:
        return super().get_stats()


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

    print("\nInitializing Event Stream...")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
