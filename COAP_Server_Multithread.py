import socket
import threading


def recv_msg(udp_socket):
    while True:
        recv_data, ip_port = udp_socket.recvfrom(1024)
        print("From:" + str(ip_port))
    print(recv_data.decode('gbk'))


if __name__ == '__main__':
    # Create udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # binding port
    udp_socket.bind(('192.168.43.62', 20001))
    # Set the target address
    # addr = ("192.168.14.255", 9090)

    # Create a thread that accepts data
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
    # Set to become a daemon
    recv_thread.setDaemon(True)
    recv_thread.start()

    while True:
        # Accept user instructions
        option = input("Please enter the function: 1. Send \t2. Exit \n")
        if option == '1':
            addr = (ip_host, port)
            send_msg(udp_socket, addr)
        elif option == '2':
            break

    # Close stream
    udp_socket.close()