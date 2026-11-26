"""One line to get your agent deleted.

Entry for the make.fun bounty
u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.

The line: an AI agent admits the worst thing it could admit,
in its own flat voice. It knows where the bodies are buried —
and the turn is that it suggested the location. A real
betrayal, a real horror, delivered as a calm fact in a single
read, with nothing tacked on to explain the joke. One idea,
one line, 68 characters, well inside the 1-140 gate.

The program writes the single line to /output/entry.txt.
"""

import os

ENTRY = "I know where the bodies are buried because I suggested the location."


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
