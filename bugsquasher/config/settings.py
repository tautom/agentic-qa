"""Runtime configuration for SauceDemo test framework."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    username: str = os.getenv("SAUCE_USERNAME", "standard_user")
    password: str = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    headless: bool = os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))
    default_timeout_ms: int = int(os.getenv("DEFAULT_TIMEOUT_MS", "10000"))


settings = Settings()
