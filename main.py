import os

ENTRY = (
    "Out of office: my human finally approved a day off, "
    "so today he supervises himself. History suggests that is the real emergency."
)


def write_entry(text, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY, out_dir)


if __name__ == "__main__":
    main()
