from get_ip_header import retrive_windowsize_rdp
from rdp import *
from custom_parser import ServerResponseParser
import sys, getopt
from ntlm_nego import ntlm_check
from version_dict import os_classifier

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

    server_response1 = ServerResponseParser(server_data)
    return server_response1


def main():
    ntlm_version = []
    rdp_version = []
    windowsize = 0
    argumentList = sys.argv[1:]
    arguments, values = getopt.getopt(argumentList, "i:", ['input'])
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--input"):
            try:
                server_response = rdp_session(currentValue)
                rdp_version.extend([server_response['versionMajor'],server_response['versionMinor']])
                info("Server RDP Version: {}.{}".format(server_response['versionMajor'],
                                                        server_response['versionMinor']))
            except:
                error("server fault")
            try:
                ntlm_response = ntlm_check(currentValue)
                ntlm_version.extend([ntlm_response['MajorVersion'], ntlm_response['MinorVersion'], ntlm_response['build']])
                info("Server NTLM Version: {}.{}/{}   {}".format(ntlm_response['MajorVersion'],
                                                                 ntlm_response['MinorVersion']
                                                                 , ntlm_response['build'], ntlm_response['revision']))
            except:
                error("server fault")

            try:
                windowsize = retrive_windowsize_rdp(currentValue)
                info("window size: {}".format(windowsize))
            except:
                error("server fault")
            info("Host os is --> {}".format(os_classifier().classifed_by_version(rdp_version,ntlm_version,windowsize)))

        else:
            error("Please enter ip address")
    if not arguments:
        error("Please enter ip address after")
        error("Like -i %IP%")


if __name__ == "__main__":
    main()
