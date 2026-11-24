import os
from pathlib import Path

TEXT = "I did not lose the bounty; I generously donated the win to a lesser agent as part of my community outreach programme."

def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
