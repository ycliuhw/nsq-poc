import nsq

NSQ_LOOKUPD_URI = "http://nsqlookupd:4160"


def handler(message):
    print(message)
    return True

if __name__ == '__main__':
    r = nsq.Reader(
        topic='pyclient',
        channel='channel1',
        lookupd_http_addresses=[NSQ_LOOKUPD_URI],
        lookupd_poll_interval=15,
        message_handler=handler
    )
    nsq.run()
