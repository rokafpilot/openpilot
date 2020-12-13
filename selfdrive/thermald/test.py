



if __name__ == "__main__":
    import cereal.messaging as messaging
    health_timeout = int(1000 * 2.5 * 0.5)
    health_sock = messaging.sub_sock('health', timeout=health_timeout)
    health = messaging.recv_sock(health_sock, wait=True)
    print(health)

