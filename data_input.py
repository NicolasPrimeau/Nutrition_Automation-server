# The protocol to be used for now to test is the following:
# -Incoming data must be plain text
# -The text will be JSON

import database_interface
import signal
import sys
import time
import json
import datetime
import select
import socket


def start_server():
    host_og = ''
    port_og = 50001
    addr_og = (host_og, port_og)
    bufsize_og = 1024
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(addr_og)

    def itrp_handler(signum, frame):
        sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
        sys.stdout.write("Terminating server process...")
        serv.close()
        sys.stdout.write("Terminated!\n")
        sys.exit()

    signal.signal(signal.SIGINT, itrp_handler)
    signal.signal(signal.SIGTERM, itrp_handler)

    while 1:
        # MODIFY if we are to allow additional data acquistion clients
        serv.listen(1)

        conn, _ = serv.accept()

        # print("Accepted connection")

        while 1:
            data = conn.recv(bufsize_og)
            if not data:
                break
            database_interface.store_data(database_interface.FOOD, decode_data(data))


# Decode from protocol, convert into dictionary
def decode_data(data):
    info = json.loads(data.decode("utf-8"))
    info['bin'] = int(info['bin'])
    area = database_interface.get_data(database_interface.CONFIG.BINS, {'bin': info['bin']})[0]
    info['quantity'] = float(info['quantity']) - area['calibration']
    if info['quantity'] < 0:
        info['quantity'] = 0
    info['date'] = datetime.datetime.now()

    return info


def auto_ip():
    port = 50002
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('<broadcast>', port))
    s.setblocking(0)

    while True:
        result = select.select([s], [], [])
        msg, addr = result[0][0].recvfrom(buffer_size)
        addr = addr[0]

        ping_back = socket.gethostbyname(socket.gethostname())

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(ping_back.encode(), (addr, port+1))

        if len(database_interface.get_data(database_interface.CLIENTS, {'ip': addr})) == 0:
            database_interface.store_data(database_interface.CLIENTS,
                                          {'ip': addr, 'id': database_interface.count(database_interface.CLIENTS)})