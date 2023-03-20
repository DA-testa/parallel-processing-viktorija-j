# python3

from typing import List, Tuple

def parallel_processing(n: int, m: int, data: List[int]) -> List[Tuple[int, int]]:
    output = []
    threads = [0] * n
    time = 0
    jobs = data
    
    while jobs:
        for idt, t in enumerate(threads):
            threads[idt] -= 1
            if threads[idt] <= 0 and jobs:
                threads[idt] = jobs.pop(0)
                output.append((idt, time))
        time += 1

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    
    for job in result:
        print(f"{job[0]} {job[1]}")

if __name__ == "__main__":
    main()
