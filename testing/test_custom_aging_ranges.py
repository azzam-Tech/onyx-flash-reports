import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from privet.onyx_reports.app import run_perf_aging_fifo, run_perf_aging_analytical

def test_default_ranges():
    rpt = {"id": "perf_aging_dynamic"}
    args = {
        "date_from": "2026-06-01",
        "date_to": "2026-06-30",
        "aging_ranges": "2,30,60,90,120"
    }
    cols, rows = run_perf_aging_fifo(rpt, args)
    print("Default ranges columns:", cols)
    assert "0-2" in cols
    assert "3-30" in cols
    assert "31-60" in cols
    assert "61-90" in cols
    assert "91-120" in cols
    assert "أكثر من 120" in cols
    print("SUCCESS: Default 6 buckets verified!")

def test_custom_ranges():
    rpt = {"id": "perf_aging_dynamic"}
    args = {
        "date_from": "2026-06-01",
        "date_to": "2026-06-30",
        "aging_ranges": "5,30,60,90,120"
    }
    cols, rows = run_perf_aging_fifo(rpt, args)
    print("Custom ranges columns:", cols)
    assert "0-5" in cols
    assert "6-30" in cols
    print("SUCCESS: Custom buckets verified!")

if __name__ == "__main__":
    test_default_ranges()
    test_custom_ranges()
