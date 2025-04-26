from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CandidateProfile:
    name: str = None
    emails: List[str] = field(default_factory=list)
    phone_numbers: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    education: List[str] = field(default_factory=list)
    experience: List[str] = field(default_factory=list)
