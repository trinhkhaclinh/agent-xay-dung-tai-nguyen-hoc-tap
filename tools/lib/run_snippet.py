# -*- coding: utf-8 -*-
"""Chạy thử một snippet đã ghi ra file tạm. Dùng bởi verify_code.py (--run).

Quy trình: import file như một module → nếu có biến `app` (ứng dụng FastAPI/ASGI) thì
dựng TestClient và gọi thử GET "/" (chấp nhận mọi status < 500, kể cả 404).

Mã thoát:
  0  OK (import được; nếu có app thì server phản hồi < 500)
  3  Thiếu thư viện bên thứ ba (môi trường) → caller coi là SKIP, không phải lỗi nội dung
  2  Lỗi thực thi thật (import/runtime/HTTP 5xx) → caller coi là BLOCKER
"""
import importlib.util
import sys
import traceback


def main():
    path = sys.argv[1]
    spec = importlib.util.spec_from_file_location("snippet_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except ModuleNotFoundError as e:
        print("SKIP_MODULE:%s" % e.name)
        sys.exit(3)
    except SyntaxError:
        traceback.print_exc()
        sys.exit(2)
    except Exception:
        traceback.print_exc()
        sys.exit(2)

    app = getattr(mod, "app", None)
    if app is None:
        print("RUN_OK_NOAPP")
        sys.exit(0)

    try:
        from starlette.testclient import TestClient
    except ModuleNotFoundError as e:
        print("SKIP_MODULE:%s" % e.name)
        sys.exit(3)

    try:
        client = TestClient(app)
        r = client.get("/")
        if r.status_code >= 500:
            print("HTTP_5XX:%d" % r.status_code)
            sys.exit(2)
        print("RUN_OK:%d" % r.status_code)
        sys.exit(0)
    except ModuleNotFoundError as e:
        print("SKIP_MODULE:%s" % e.name)
        sys.exit(3)
    except Exception:
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()
