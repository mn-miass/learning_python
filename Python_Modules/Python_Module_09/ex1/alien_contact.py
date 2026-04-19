from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    messages_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def Validation_Rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must not start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
           self.witness_count < 3):
            raise ValueError("Telepathic contacts must have at least 5 "
                             "witnesses")
        if self.signal_strength > 7.0 and self.messages_received is None:
            raise ValueError("Strong signals must have messages received")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 6, 1, 12, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            messages_received="'Greetings from Zeta Reticuli'",
            is_verified=True
        )
        print("Valid Contact report")
        print('ID: ', valid_contact.contact_id)
        print("Type:", valid_contact.contact_type)
        print("Location:", valid_contact.location)
        print("Signal :", valid_contact.signal_strength)
        print("Duration:", valid_contact.duration_minutes, "minutes")
        print("Witnesses:", valid_contact.witness_count)
        print('Messages:', valid_contact.messages_received)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        print("\n======================================")
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 6, 1, 12, 0),
            location="Area 52, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
            messages_received=None,
            is_verified=False
        )

        print("Valid Contact report")
        print('ID: ', invalid_contact.contact_id)
        print("Type:", invalid_contact.contact_type)
        print("Location:", invalid_contact.location)
        print("Signal :", invalid_contact.signal_strength)
        print("Duration:", invalid_contact.duration_minutes, "minutes")
        print("Witnesses:", invalid_contact.witness_count)
        print('Messages:', invalid_contact.messages_received)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
