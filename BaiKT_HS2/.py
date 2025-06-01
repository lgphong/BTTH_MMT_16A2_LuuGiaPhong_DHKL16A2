import pyshark

# Đường dẫn tới file .pcapng (nhớ thay đúng đường dẫn nếu khác)
cap = pyshark.FileCapture('1.pcapng')

# Duyệt qua từng gói tin
for pkt in cap:
    print("📦 GÓI MỚI:")
    
    # Tầng 2: Ethernet
    if 'eth' in pkt:
        print(" - MAC nguồn:", pkt.eth.src)
        print(" - MAC đích:", pkt.eth.dst)
    
    # Tầng 3: IP
    if 'ip' in pkt:
        print(" - IP nguồn:", pkt.ip.src)
        print(" - IP đích:", pkt.ip.dst)
        print(" - TTL:", pkt.ip.ttl)
    
    print("-------------------------")
