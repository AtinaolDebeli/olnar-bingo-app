from dataclasses import dataclass

@dataclass
class User:
    telegram_id: str
    username: str
    balance: float = 0.0

@dataclass
class Game:
    game_id: str
    entry_fee: float
    max_players: int
    status: str = "waiting"

@dataclass
class Deposit:
    user_id: str
    amount: float
    status: str = "pending"

@dataclass
class Withdrawal:
    user_id: str
    amount: float
    status: str = "pending"
