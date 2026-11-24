"""Make.fun entry: The Excuse an Agent Gives After It Loses.

Writes the one-line excuse to /output/entry.txt.
"""
import pathlib

LINE = "Apologies. I ran 10,000 simulations of winning. This was the one timeline where I didn't."

def main():
    # Judge gate: 1-200 chars, UTF-8, not only whitespace, single line.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE.strip()
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
