from dataclasses import dataclass


@dataclass
class AuthenticationResponse:
    reason: str = None
    token: str = None
