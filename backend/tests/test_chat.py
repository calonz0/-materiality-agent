from interface.chat_handler import handle_request


def run_chat_test():
    client_id = "test_client"

    print("\n💬 STEP 1 (no invoice):")
    print(handle_request(client_id))

    print("\n💬 STEP 2 (send invoice):")
    invoice = {
        "description": "Industrial painting service",
        "amount": 10000
    }
    print(handle_request(client_id, invoice))

    print("\n💬 STEP 3 (repeat call, should remember state):")
    print(handle_request(client_id))


if __name__ == "__main__":
    run_chat_test()
