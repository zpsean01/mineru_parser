import requests, json, time, sys, zipfile
from pathlib import Path

token = json.load(open("config.json"))["token"]
header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
local_path = Path("D:\\协议与规范\\arm\\IHI0100_A.c_ras_system_architecture_document.pdf")

print("[1] 申请上传链接 (page_ranges=1-200, pipeline)", flush=True)
resp = requests.post("https://mineru.net/api/v4/file-urls/batch", headers=header, json={
    "files": [{"name": local_path.name, "page_ranges": "1-200"}],
    "model_version": "pipeline",
})
data = resp.json()["data"]
batch_id = data["batch_id"]
upload_url = data["file_urls"][0]
print("  batch_id: %s" % batch_id, flush=True)

print("[2] 上传文件…", flush=True)
with open(local_path, "rb") as f:
    r = requests.put(upload_url, data=f, timeout=600)
print("  status: %s" % r.status_code, flush=True)

print("[3] 轮询结果…", flush=True)
for i in range(600):
    resp = requests.get("https://mineru.net/api/v4/extract-results/batch/%s" % batch_id, headers=header)
    result = resp.json()
    if result.get("code") != 0:
        print("  code=%s msg=%s" % (result.get("code"), result.get("msg")), flush=True)
        time.sleep(5)
        continue

    entries = result["data"].get("extract_result", [])
    if not entries:
        print("  等待系统提交…", flush=True)
        time.sleep(5)
        continue

    entry = entries[0]
    state = entry.get("state")
    fn = entry.get("file_name", "?")
    print("  %s: %s" % (fn, state), flush=True)

    if state == "done":
        zip_url = entry["full_zip_url"]
        print("完成! ZIP: %s" % zip_url, flush=True)
        r2 = requests.get(zip_url, stream=True, timeout=300)
        out = Path("./data/ras_arm_doc_pipeline")
        out.mkdir(parents=True, exist_ok=True)
        zip_path = out / "result.zip"
        with open(zip_path, "wb") as f:
            for chunk in r2.iter_content(8192):
                if chunk: f.write(chunk)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(out)
        print("已解压到 %s/" % out, flush=True)
        for f in sorted(out.iterdir()):
            if f.is_file() and "result.zip" not in f.name:
                print("  - %s (%d KB)" % (f.name, f.stat().st_size // 1024), flush=True)
        break
    elif state == "failed":
        print("失败: %s" % entry.get("err_msg", ""), flush=True)
        sys.exit(1)
    elif state == "running":
        ep = entry.get("extract_progress", {}).get("extracted_pages", 0)
        tp = entry.get("extract_progress", {}).get("total_pages", 0)
        print("  进度: %s/%s" % (ep, tp), flush=True)

    time.sleep(5)
