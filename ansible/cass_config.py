import sys


def main():
    if len(sys.argv) < 2:
        print("Invalid number of args!")
        sys.exit(1)
    ip = sys.argv[1]
    with open("cassandra.yaml", "r") as f:
        config = "".join(f.readlines()).format(ip=ip)
        with open("new_cassandra.yaml", "w") as f2:
            f2.write(config)


if __name__ == "__main__":
    main()
