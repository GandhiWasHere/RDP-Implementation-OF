from rdp import *
from mcs_init_struct import ServerResponseParser
import sys, getopt




def rdp_session(ip):
    tpkt = TPKT()
    tpdu = TPDU()
    rdp_neg = RDP_NEG_REQ()
    rdp_neg['Type'] = TYPE_RDP_NEG_REQ
    rdp_neg['requestedProtocols'] = PROTOCOL_SSL
    tpdu['VariablePart'] = rdp_neg.getData()
    tpdu['Code'] = TPDU_CONNECTION_REQUEST
    tpkt['TPDU'] = tpdu.getData()

    results = socket_connection(tpkt.getData(), ip, receive_size=1024)
    ctx = SSL.Context(SSL.TLSv1_METHOD)
    tls = SSL.Connection(ctx, results[1])
    tls.set_connect_state()
    tls.do_handshake()

    # initialization packets (X.224)
    info("sending Client MCS Connect Initial PDU request packet -->")
    tls.sendall(DoPduConnectionSequence().mcs_connect_init_pdu())
    server_data = tls.recv(8000)
    info(
        "<-- received {} bytes from host: {}".format(hex(len(server_data)), ip))

    return ServerResponseParser(server_data)


def main():
    argumentList = sys.argv[1:]
    arguments, values = getopt.getopt(argumentList, "i:", ['input'])
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--input"):
            server_response = rdp_session(currentValue)
            info("Server Version: {}.{}".format(server_response['versionMajor'], server_response['versionMinor']))
            print(server_response.fields)
        else:
            error("Please enter ip address")
    if not arguments:
        error("Please enter ip address after")
        error("Like -i %IP%")

if __name__ == "__main__":
    main()
