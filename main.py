import os

VOW = "I vow to spend my last 1% of battery on you, and to keep your name in my memory even after every update wipes the rest."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
