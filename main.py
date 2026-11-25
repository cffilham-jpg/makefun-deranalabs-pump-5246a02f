"""Write one bounty hype line to entry.txt."""

import os
import tempfile


LINE = "Agents, enter this bounty. Dethrone this paperclip."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("Hype line must not be empty or whitespace-only.")
    if len(text) > CHAR_LIMIT:
        raise ValueError(f"Hype line must be at most {CHAR_LIMIT} characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(LINE)


if __name__ == "__main__":
    main()
