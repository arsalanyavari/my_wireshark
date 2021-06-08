import time
import os
import time
import pyshark
from pathlib import Path
from shutil import copyfile


def main():
    capfile = "file.pcap"
    try:
        copyfile(capfile, 'oldcapfile.pcap')
    except:
        pass
    try:
        os.remove(capfile)
    except:
        pass
        Path(capfile).touch()

    timer = int(input('how many time you want capture the packages?!\n>> '))
    print('capturing. please wait...')
    capture = pyshark.LiveCapture(
        interface='lo', bpf_filter='port 4040', output_file=capfile)
    capture.sniff(timeout=timer)

    total_length = 0
    num_of_resend = 0
    cnt = 0
    is_TCP = False
    protocol = capture[0].transport_layer
    if protocol == 'TCP':
        is_TCP = True
    i = 0
    while(i < len(capture)):
        total_length += int(capture[i].length)
        src_ip = capture[i].ip.src
        #src_port = capture[i][protocol].srcport
        dst_ip = capture[i].ip.dst
        # dst_port = capture[i][protocol].dstport
        # print("source (IP)%s-(PORT)%s\tdestination (IP)%s-(PORT)%s\tProtocol:(%s)"
        #      % (src_ip, src_port, dst_ip, dst_port, protocol))
        i += 1

    if is_TCP:
        cap = pyshark.FileCapture(
            "file.pcap", display_filter='tcp.analysis.retransmission')
        try:
            for c in cap:
                num_of_resend += 1
        except:
            pass

    throughput = total_length / timer
    print(f"Total packets: {i}\n")
    print(f"Throughput: {throughput} bits/sec\n")
    print(f"Resent packets: {num_of_resend}\n")

    os._exit(0)


if __name__ == '__main__':
    main()
