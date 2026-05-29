DB_NAME = "dog.db"


def store(key, value):
    with open(DB_NAME, "a") as f:
        f.write(f"{key}:{value}\n")


def retrieve(key):
    result = None
    with open(DB_NAME, "r") as f:
        for line in f:
            k, v = line.strip().split(":", 1)
            if k == key:
                result = v
    return result


def main():
    print("Mini DB. Commands: PUT k,v | GET k | EXIT")
    while True:
        try:
            line = input("🐕> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line:
            continue
        parts = line.split(None, 1)
        cmd = parts[0].upper()
        if cmd == "EXIT":
            break
        elif cmd == "GET":
            if len(parts) < 2:
                print("Usage: GET k")
                continue
            val = retrieve(parts[1])
            print(val if val is not None else "(not found)")
        elif cmd == "PUT":
            if len(parts) < 2 or "," not in parts[1]:
                print("Usage: PUT k,v")
                continue
            k, v = parts[1].split(",", 1)
            store(k.strip(), v.strip())
        else:
            print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
