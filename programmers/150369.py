def solution(cap, n, deliveries, pickups):
    
    box = 0
    result = 0
    while deliveries or pickups:
        dcap, pcap = cap, cap
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        result += max(len(deliveries), len(pickups)) * 2
    
                
        while dcap > 0 and deliveries:
            box = deliveries.pop()
            if box <= dcap:
                dcap -= box
            else:
                deliveries.append(box - dcap)
                break
        
        while pcap > 0 and pickups:
            box = pickups.pop()
            if box <= pcap:
                pcap -= box
            else:
                pickups.append(box - pcap)
                break
    
    return result