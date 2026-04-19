from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        valid_station = SpaceStation(
            station_id="SS01",
            name="Orbital Station Alpha",
            crew_size=10,
            power_level=85.5,
            oxygen_level=92.0,
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=True,
            notes="All systems nominal."
        )

        print("Space Station Data Validation")
        print("=================================")
        print("Valid Station Created Successfully")
        print("ID:", valid_station.station_id)
        print("Name:", valid_station.name)
        print("Crew :", valid_station.crew_size)
        print("Power Level:", valid_station.power_level)
        print("Oxygen Level:", valid_station.oxygen_level)
        print('Status:', "Operational\n" if valid_station.is_operational else
              "Non-operational\n")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        print("=================================")
        invalid_station = SpaceStation(
            station_id="SS02",
            name="Orbital Station Beta",
            crew_size=210,
            power_level=85.5,
            oxygen_level=92.0,
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=True,
            notes="All systems nominal."
        )
        print("Space Station Data Validation")
        print("=================================")
        print("Valid Station Created Successfully")
        print("ID:", invalid_station.station_id)
        print("Name:", invalid_station.name)
        print("Crew :", invalid_station.crew_size)
        print("Power Level:", invalid_station.power_level)
        print("Oxygen Level:", invalid_station.oxygen_level)
        print('Status:', "Operational" if invalid_station.is_operational else
              "Non-operational")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
