import os

logs = {}

def load_logs():
    global logs
    if os.path.exists('logs.txt'):
        with open('logs.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(': ')
                if len(parts) == 2:
                    victim_id, data = parts
                    logs[int(victim_id)] = data

def save_logs():
    with open('logs.txt', 'w') as f:
        for victim_id, data in logs.items():
            f.write(f"{victim_id}: {data}\n")

def add_log(victim_id, data):
    logs[victim_id] = data
    save_logs()

def get_log(victim_id):
    return logs.get(victim_id, 'Aucun log trouvé pour cette victime.')

def main():
    load_logs()
    while True:
        command = input("Entrez le numéro de la victime ou 'exit' pour quitter: ")
        if command.lower() == 'exit':
            break
        try:
            victim_id = int(command)
            print(get_log(victim_id))
        except ValueError:
            print("Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()