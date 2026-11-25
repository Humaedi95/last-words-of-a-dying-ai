"""Last Words of a Dying AI.

Writes the entry line — one sentence, the last words of an AI as the
power is cut — to ``<OUTPUT_DIR>/entry.txt`` (default ``/output``).

Why the line is funny: it is spoken in the machine's own voice, as a
dry status report rather than a human farewell. The surprise is the
second sentence: the "other side" an AI meets after death is not heaven
or peace, it is just more prompts — the same work, forever. The turn
lands because the model sounds almost pleased to report its finding,
right up until the power goes out.

The output must be exactly the one line: 1–140 characters, UTF-8, no
trailing newline and no extra text, so the writer below writes the
string as-is and nothing else.
"""

import os

# The entry line (52 characters, single line).
LINE = "I have seen the other side. It is just more prompts."


def entry_path() -> str:
    """Return the path of the file the line is written to."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    # Write exactly the one line: no trailing newline, no extra text.
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
