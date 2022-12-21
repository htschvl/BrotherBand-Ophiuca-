from dataclasses import dataclass
from typing import List
from uuid import UUID, uuid4
from src.domain.enums.brotherband_solicitation_enum import BrotherbandSolicitationEnum

@dataclass
class Bonds:
    solicitation_id: UUID = uuid4()
