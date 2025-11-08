input = [s for s in open("input.txt").read().split('\n') if s][0]

test =["bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg"]

def findStartOfPacket(ds_buffer, len_packet):
    for count, value in enumerate(ds_buffer):
        if len(set(ds_buffer[count:count+len_packet])) == len_packet:
            return count + len_packet

print(findStartOfPacket(input,14))