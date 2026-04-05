from backend.orchestrator.materiality_flow import MaterialityFlow


def run_test():
    print("🚀 Starting FULL FLOW TEST\n")

    client_id = "test_client"
    file_path = "test_invoice.xml"

    flow = MaterialityFlow(client_id)

    try:
        result = flow.run(file_path)

        print("\n✅ FLOW COMPLETED")
        print(result)

    except Exception as e:
        print("\n❌ FLOW FAILED")
        print(str(e))


if __name__ == "__main__":
    run_test()
