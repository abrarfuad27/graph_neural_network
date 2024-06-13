import re
import matplotlib.pyplot as plt

def get_power_usage_from_logs(log_file):
    power_usage = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'(\d+\.\d+) kWh of electricity used since the beginning', line)
            if match:
                power_usage.append(float(match.group(1)))
    return power_usage

if __name__ == '__main__':
    log_file = 'log_file.txt'
    power_usage = get_power_usage_from_logs(log_file)
    print(power_usage)

    plt.figure()
    plt.plot(power_usage)
    plt.xlabel('Epoch')
    plt.ylabel('Power Usage (kWh)')
    plt.title('Graph Neural Network Power Usage vs Epoch')
    plt.savefig('power_usage.png')

