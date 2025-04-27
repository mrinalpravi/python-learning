import csv
from packaging import version


def load_server_data(file_path):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def find_outdated_servers(server_data, thresholds):
    outdated_servers = []
    for server in server_data:
        outdated_libs = {}
        for lib, threshold_version in thresholds.items():
            if lib in server and version.parse(server[lib]) < version.parse(threshold_version):
                outdated_libs[lib] = server[lib]
        if outdated_libs:
            outdated_servers.append((server["server"], outdated_libs))
    return outdated_servers


def main():
    file_path = "server.csv"
    thresholds = {"nginx": "1.20.0", "python": "3.8.0", "openssl": "1.1.1"}

    server_data = load_server_data(file_path)
    # print(server_data)
    for i in server_data:
        print(i)
    outdated_servers = find_outdated_servers(server_data, thresholds)

    writer(outdated_servers,"hello.csv")
    for server, outdated_libs in outdated_servers:
        print(f"{server}: {outdated_libs}")


def writer(names,path):
    with open(path, "w", newline="") as f:
        fieldname = ["name"]
        writer = csv.DictWriter(f, fieldnames=fieldname)

        writer.writeheader()

        for name in names:
            writer.writerow({"name":name})


if __name__ == "__main__":
    # main()
    writer(["mrinal","ivin","jinu"],"names.csv")
