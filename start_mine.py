import subprocess

def start_mining_instances(instance_count, batch_file):
    for _ in range(instance_count):
        subprocess.call(['start', 'cmd', '/c', batch_file], shell=True)
        print("Started an instance of ore miner.")

def main():
    try:
        batch_file = r"C:\Users\anwor\OneDrive\OLD FILES\Desktop\Ore_miner.bat"
        num_instances = int(input('Enter the number of ORE CLI miner instances to run: '))
        start_mining_instances(num_instances, batch_file)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
