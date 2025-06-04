import time


def stopwatch(duration_seconds=60):
    """Run a simple stopwatch for the given number of seconds."""
    for elapsed in range(1, duration_seconds + 1):
        print(f"{elapsed}\uCD08 \uACBD\uACFC")  # "X초 경과" in Korean
        time.sleep(1)
    print("1\uBD84\uC774 \uACBD\uACFC\uD588\uC2B5\uB2C8\uB2E4!")


if __name__ == "__main__":
    stopwatch()

