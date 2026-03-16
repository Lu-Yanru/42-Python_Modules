#!/usr/bin/env python3


from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Missing module pydantic.")
    print("Install with: pip install pydantic")
    print("Exiting...")
    exit()


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2025-06-16T10:00:00",
            is_operational=True,
            # notes="Main station"
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {"Operational"
                         if valid_station.is_operational
                         else "Not operational"}")
    except ValidationError as e:
        print(e)

    print("\n========================================")
    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=50,  # invalid crew size
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2025-06-16T10:00:00",
            is_operational=True,
            notes=None
        )
        print(f"Crew: {invalid_station.crew_size} people")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
