import speedtest
import csv
from datetime import datetime
from time import sleep


def run_speedtest():
    st = speedtest.Speedtest(secure=True)
    st.get_servers()
    st.get_best_server()
    download_speed = st.download() * (10**-6)
    upload_speed = st.upload() * (10**-6)
    ping = st.results.ping
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return current_time, download_speed, upload_speed, ping


def write_to_csv(csv_filename, current_time, download_speed, upload_speed, ping):
    with open(csv_filename, 'a', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')

        if csv_file.tell() == 0:
            csv_writer.writerow(['Data', 'Taxa de Download (Mbps)', 'Taxa de Upload (Mbps)', 'Ping (ms)'])

        csv_writer.writerow([f"{current_time}", f"{download_speed:.2f}", f"{upload_speed:.2f}", f"{ping:.3f}"])


if __name__ == "__main__":
    num_tests = int(input("Digite o número de vezes que deseja testar: "))
    interval = 20
    csv_fileName = 'speedTestResults.csv'

    for q in range(num_tests):
        currentTime, downloadSpeed, uploadSpeed, pingResult = run_speedtest()
        write_to_csv(csv_fileName, currentTime, downloadSpeed, uploadSpeed, pingResult)
        print('Teste {}/{}: Data: {} Download: {:.2f} Upload: {:.2f} Ping: {}'.format(q+1, num_tests, currentTime, downloadSpeed, uploadSpeed, pingResult))
        if (q+1) < num_tests:
            sleep(interval)
