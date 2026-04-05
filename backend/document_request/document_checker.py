def get_required_documents(classification):

    if classification == "PRODUCT":
        return [
            "Purchase Order",
            "Supply Contract",
            "Payment Order"
        ]

    elif classification == "SERVICE":
        return [
            "Service Proposal",
            "Service Contract",
            "Payment Order",
            "Service Completion Certificate"
        ]

    return ["General Document"]
