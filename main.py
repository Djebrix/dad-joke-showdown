"""Dad Joke Showdown entry: one dad joke, written to $ENTRY_OUTPUT_DIR/entry.txt.

Stdlib only, no network, deterministic.
"""

import os

JOKE = "My son asked why I keep a pencil behind my ear. I said, 'So I can draw the line when you cross it.'"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} out of range"
    assert JOKE.strip(), "joke must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
