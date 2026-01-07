import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

class Analytics:
    """Simple analytics tracking"""

    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.usage_file = self.log_dir / "usage.json"
        self.stats_file = self.log_dir / "stats.json"

    def log_usage(self, event: str, data: Dict[str, Any]):
        """Log user interaction"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event,
            "data": data,
        }

        with open(self.usage_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

    def increment_stat(self, state_name: str, amount: int = 1):
        """Increment a statistic"""
        stats = self._load_stats()
        stats[state_name] = stats.get(state_name, 0) + amount
        self._save_stats(stats)

    def _load_stats(self) -> Dict[str, Any]:
        """Load statistics"""
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                stats = json.load(f)
        return {}

    def _save_stats(self, stats: Dict[str, Any]):
        """Save statistics"""
        with open(self.stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

