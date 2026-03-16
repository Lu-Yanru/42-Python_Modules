#!/usr/bin/env python3


from datetime import datetime
from enum import Enum


try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("Missing module pydantic.")
    print("Install with: pip install pydantic")
    print("Exiting...")
    exit()


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate(self: "SpaceMission") -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        needed_crew = False
        for member in self.crew:
            if member.rank == (Rank.COMMANDER or Rank.CAPTAIN):
                needed_crew = True
        if not needed_crew:
            raise ValueError("Must have at least one Commander or Captain")

        experienced = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced crew")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self

    def print_info(self: "SpaceMission") -> None:
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        sarah = CrewMember(
            member_id="SC01",
            name="Sarah Connor",
            rank="commander",
            age=35,
            specialization="Mission Command",
            years_experience=10
        )
        john = CrewMember(
            member_id="JS01",
            name="John Smith",
            rank="lieutenant",
            age=30,
            specialization="Navigation",
            years_experience=8
        )
        alice = CrewMember(
            member_id="AJ01",
            name="Alice Johnson",
            rank="officer",
            age=32,
            specialization="Engineering",
            years_experience=6
        )
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-01-01T10:00:00",
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0
        )
        valid_mission.print_info()
    except ValidationError as e:
        print(e)
        exit(1)

    print("\n=========================================")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-01-01T10:00:00",
            duration_days=900,
            crew=[alice],
            budget_millions=2500.0
        )
        invalid_mission.print_info()
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
        exit(1)


if __name__ == "__main__":
    main()
