import json, os

dirs = [
    "data\\IHI0100_A.c_ras_system_architecture_document_1-200-4eec50ce-4515-4b7f-b8bb-bfef79f004ad",
    "data\\IHI0100_A.c_ras_system_architecture_document_200-226-5cd9e625-23ba-4a2f-a307-b1083200e80f",
]

for data_dir in dirs:
    print("=== %s ===" % data_dir.split("\\")[-1])
    for f in sorted(os.listdir(data_dir)):
        fp = os.path.join(data_dir, f)
        data = json.load(open(fp, encoding="utf-8"))

        if "content_list_v2" in f:
            # v2 is page-level: one entry per page
            print("  %s: list[%d]" % (f, len(data)))
            if data and isinstance(data[0], dict):
                print("    keys:", list(data[0].keys()))

        if "content_list" in f and "v2" not in f:
            # v1 is element-level
            if data and isinstance(data[0], dict):
                page_idxes = set()
                for item in data:
                    pi = item.get("page_idx")
                    if pi is not None:
                        page_idxes.add(pi)
                if page_idxes:
                    print("  %s: %d items, page_idx range: %d ~ %d (%d unique)" % (
                        f, len(data), min(page_idxes), max(page_idxes), len(page_idxes)))

        if f == "layout.json":
            if isinstance(data, dict) and "pdf_info" in data:
                pdf_info = data["pdf_info"]
                if isinstance(pdf_info, list):
                    print("  layout.json pdf_info: list[%d]" % len(pdf_info))
                else:
                    print("  layout.json pdf_info: %s" % type(pdf_info).__name__)
            else:
                print("  layout.json keys:", list(data.keys())[:8])
    print()
