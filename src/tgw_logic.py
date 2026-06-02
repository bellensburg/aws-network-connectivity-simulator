from find_by_id import find_by

def same_tgw(attachments, vpc_a, vpc_b):
    """
    Check if two VPCs share the same Transit Gateway.
    """
    att_a = find_by(attachments, "vpc_id", vpc_a)
    att_b = find_by(attachments, "vpc_id", vpc_b)

    if not att_a or not att_b:
        return False

    return att_a["tgw_id"] == att_b["tgw_id"]


if __name__ == "__main__":
    attachments = [
        {"tgw_id": "tgw-1", "vpc_id": "vpc-a"},
        {"tgw_id": "tgw-1", "vpc_id": "vpc-b"}
    ]

    print(same_tgw(attachments, "vpc-a", "vpc-b"))
