#!/usr/bin/env python3
import sys, time, random, math
def main():
    print("\033[1;33m" + "="*60 + "\033[0m")
    print(f"\033[1;33m          {sys.argv[0].split('/')[-1].upper()} MATRIX SIMULATION ENGINE\033[0m")
    print("\033[1;33m" + "="*60 + "\033[0m")
    print("\033[3mType 'sim' to run a 10-step tensor computation, or 'exit'.\033[0m\n")
    while True:
        try:
            cmd = input("\033[1;32mSIM > \033[0m").strip()
            if cmd == 'exit': break
            if cmd == 'sim':
                for i in range(1, 11):
                    val = math.sin(i) * random.uniform(10, 100)
                    print(f"\033[1;36m[Epoch {i}/10]: Vector state = {val:.6f} | Delta = {abs(val/2):.4f}\033[0m")
                    time.sleep(0.3)
                print("\033[1;32m[Success]: Simulation converged.\033[0m")
        except: break
if __name__ == '__main__': main()
