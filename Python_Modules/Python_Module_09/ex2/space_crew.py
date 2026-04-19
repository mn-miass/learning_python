from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = "Cadet"
    OFFICER = "Officer"
    LIEUTENANT = "Lieutenant"
    CAPITAIN = "Captain"
    COMMANDER = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_of_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="Planned")
    budget_million: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def Mission_Validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        count = 0
        for member in self.crew:
            if member.rank == Rank.CAPITAIN or member.rank == Rank.COMMANDER:
                count += 1
        if count == 0:
            raise ValueError("Mission must have at least one "
                             "Captain or Commander")
        experience_over_5 = 0
        for memeber in self.crew:
            if memeber.years_of_experience > 5:
                experience_over_5 += 1
        if self.duration_days > 365 and experience_over_5 < len(self.crew) / 2:
            raise ValueError("Long missions must have at least half of "
                             "the crew "
                             "with more than 5 years of experience")
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=================================")
    try:
        validated_crew_1 = CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=35,
            specialization="Mission Command",
            years_of_experience=10,
            is_active=True
        )
        validated_crew_2 = CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=28,
            specialization="Navigation",
            years_of_experience=6,
            is_active=True
        )
        validated_crew_3 = CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=30,
            specialization="Engineering",
            years_of_experience=4,
            is_active=True
        )
        valid_crew = [validated_crew_1, validated_crew_2, validated_crew_3]

        valid_mission = SpaceMission(
            mission_id="M2024_Mars",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            launch_date=datetime(2024, 6, 1, 12, 0),
            crew=valid_crew,
            budget_million=2500.0)
        print("Valid Mission Created:")
        print("Mission :", valid_mission.mission_name)
        print("ID:", valid_mission.mission_id)
        print("Destination:", valid_mission.destination)
        print("Duration:", valid_mission.duration_days, "days")
        print("Budget:", valid_mission.budget_million, "million USD")
        print("Crew Members:")
        for member in valid_crew:
            print(f" - {member.name} ({member.rank} - "
                  f"{member.specialization})")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        print("\n=========================================")
        invalidated_crew_1 = CrewMember(
            member_id="CM001",
            name="Alice Johnson",
            rank=Rank.CADET,
            age=35,
            specialization="Pilot",
            years_of_experience=10,
            is_active=True
        )
        invalidated_crew_2 = CrewMember(
            member_id="CM002",
            name="Bob Smith",
            rank=Rank.LIEUTENANT,
            age=28,
            specialization="Engineer",
            years_of_experience=6,
            is_active=True
        )
        invalidated_crew_3 = CrewMember(
            member_id="CM003",
            name="Charlie Davis",
            rank=Rank.LIEUTENANT,
            age=30,
            specialization="Scientist",
            years_of_experience=4,
            is_active=True
        )
        invalid_crew = [invalidated_crew_1, invalidated_crew_2,
                        invalidated_crew_3]
        invalid_mission = SpaceMission(
            mission_id="M2024_Mars",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            launch_date=datetime(2024, 6, 1, 12, 0),
            crew=invalid_crew,
            budget_million=2500.0
        )
        print("Valid Mission Created:")
        print("Mission :", invalid_mission.mission_name)
        print("ID:", invalid_mission.mission_id)
        print("Destination:", invalid_mission.destination)
        print("Duration:", invalid_mission.duration_days, "days")
        print("Budget:", invalid_mission.budget_million, "million USD")
        print("Crew Members:")
        for member in valid_crew:
            print(f" - {member.name} ({member.rank} - "
                  f"{member.specialization})")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
