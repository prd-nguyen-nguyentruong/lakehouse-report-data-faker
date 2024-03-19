import psutil
import time


def get_process_info(process_id):
    process = psutil.Process(process_id)
    cpu_percent = process.cpu_percent(interval=0.5)
    mem_percent = process.memory_percent()
    cpu_time = process.cpu_times()
    command = process.cmdline()

    return cpu_percent, mem_percent, cpu_time, command


def main():
    process_id = int(input("Enter process ID: "))

    highest_cpu_load = 0
    lowest_cpu_load = float("inf")
    total_cpu_load = 0

    highest_mem_load = 0
    lowest_mem_load = float("inf")
    total_mem_load = 0

    num_samples = 0

    try:
        while True:
            cpu_percent, mem_percent, _, _ = get_process_info(process_id)

            highest_cpu_load = max(highest_cpu_load, cpu_percent)
            lowest_cpu_load = min(lowest_cpu_load, cpu_percent)
            total_cpu_load += cpu_percent

            highest_mem_load = max(highest_mem_load, mem_percent)
            lowest_mem_load = min(lowest_mem_load, mem_percent)
            total_mem_load += mem_percent

            num_samples += 1

            print("Current CPU load:", cpu_percent)
            print("Highest CPU load:", highest_cpu_load)
            print("Lowest CPU load:", lowest_cpu_load)
            print("Average CPU load:", total_cpu_load / num_samples)
            print("----------------------------------------")

            print("Current Memory load:", mem_percent)
            print("Highest Memory load:", highest_mem_load)
            print("Lowest Memory load:", lowest_mem_load)
            print("Average Memory load:", total_mem_load / num_samples)
            print("----------------------------------------")

            time.sleep(1)  # Adjust the frequency of sampling here
    except Exception:
        print("Monitor interupt. Stopped!")
    finally:
        print("\nMonitoring stopped.")
        if num_samples > 0:
            print("Last recorded CPU load statistics:")
            print("Highest CPU load:", highest_cpu_load)
            print("Lowest CPU load:", lowest_cpu_load)
            print("Average CPU load:", total_cpu_load / num_samples)

            print("Last recorded Memory load statistics:")
            print("Highest Memory load:", highest_mem_load)
            print("Lowest Memory load:", lowest_mem_load)
            print("Average Memory load:", total_mem_load / num_samples)


if __name__ == "__main__":
    main()
