def parse_aging_ranges(aging_ranges_str):
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append("0")
        elif prev == 0:
            bucket_labels.append(f"0-{lim}")
        else:
            bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    return limits, bucket_labels, bucket_of

def test_default_6_buckets():
    limits, labels, bucket_of = parse_aging_ranges("2,30,60,90,120")
    print("Default Labels:", labels)
    assert len(labels) == 6
    assert labels == ["0-2", "3-30", "31-60", "61-90", "91-120", "أكثر من 120"]
    
    # Test advance payment (age = 0)
    assert bucket_of(0) == 0 # Falls into 0-2
    assert bucket_of(2) == 0 # Falls into 0-2
    assert bucket_of(3) == 1 # Falls into 3-30
    assert bucket_of(30) == 1 # Falls into 3-30
    assert bucket_of(31) == 2 # Falls into 31-60
    assert bucket_of(150) == 5 # Falls into >120
    print("SUCCESS: Default 6 buckets test passed!")

def test_custom_5_to_30_buckets():
    limits, labels, bucket_of = parse_aging_ranges("5,30,60,90,120")
    print("Custom Labels:", labels)
    assert labels[0] == "0-5"
    assert labels[1] == "6-30"
    assert bucket_of(0) == 0 # Falls into 0-5
    assert bucket_of(5) == 0 # Falls into 0-5
    assert bucket_of(6) == 1 # Falls into 6-30
    print("SUCCESS: Custom 0-5, 6-30 buckets test passed!")

if __name__ == "__main__":
    test_default_6_buckets()
    test_custom_5_to_30_buckets()
