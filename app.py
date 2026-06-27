from http.server import BaseHTTPRequestHandler, HTTPServer


import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8001))

CAKE_IMAGE_URL = "https://i.pinimg.com/736x/90/47/47/904747e3be82b47fb1c2a28585f81d39.jpg"
PINTEREST_PIN_URL = "https://www.pinterest.com/pin/6685099435977519/"


HTML = f"""<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sweet Galaxy Cake</title>
    <style>
        :root {{
            --violet: #7c3aed;
            --purple: #a855f7;
            --blue: #2563eb;
            --cyan: #06b6d4;
            --cream: #fff7ed;
            --ink: #172033;
            --muted: #63708a;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            min-height: 100vh;
            color: var(--ink);
            font-family: "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(circle at 12% 18%, rgba(255, 255, 255, 0.45), transparent 24rem),
                linear-gradient(135deg, #5b21b6 0%, #7c3aed 36%, #2563eb 70%, #06b6d4 100%);
        }}

        .page {{
            width: min(1120px, calc(100% - 32px));
            min-height: 100vh;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 460px;
            align-items: center;
            gap: 48px;
            padding: 48px 0;
        }}

        .hero {{
            color: white;
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin: 0 0 18px;
            padding: 8px 14px;
            border: 1px solid rgba(255, 255, 255, 0.32);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.14);
            backdrop-filter: blur(12px);
            font-size: 14px;
            font-weight: 700;
        }}

        h1 {{
            max-width: 720px;
            margin: 0;
            font-size: clamp(42px, 7vw, 82px);
            line-height: 0.96;
            letter-spacing: 0;
        }}

        .lead {{
            max-width: 590px;
            margin: 24px 0 0;
            color: rgba(255, 255, 255, 0.88);
            font-size: 19px;
            line-height: 1.7;
        }}

        .actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-top: 34px;
        }}

        .button {{
            display: inline-flex;
            min-height: 48px;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            padding: 0 22px;
            color: var(--ink);
            background: var(--cream);
            text-decoration: none;
            font-weight: 800;
            box-shadow: 0 18px 40px rgba(23, 32, 51, 0.18);
        }}

        .button.secondary {{
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.36);
            background: rgba(255, 255, 255, 0.14);
            box-shadow: none;
        }}

        .cake-card {{
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.42);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.78);
            box-shadow: 0 28px 80px rgba(23, 32, 51, 0.28);
            backdrop-filter: blur(18px);
        }}

        .cake-card img {{
            display: block;
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
        }}

        .cake-info {{
            padding: 24px;
        }}

        .cake-info h2 {{
            margin: 0 0 10px;
            font-size: 25px;
        }}

        .cake-info p {{
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }}

        .features {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-top: 34px;
        }}

        .feature {{
            min-height: 94px;
            border: 1px solid rgba(255, 255, 255, 0.28);
            border-radius: 8px;
            padding: 16px;
            color: white;
            background: rgba(255, 255, 255, 0.12);
        }}

        .feature strong {{
            display: block;
            margin-bottom: 6px;
            font-size: 15px;
        }}

        .feature span {{
            color: rgba(255, 255, 255, 0.78);
            font-size: 13px;
            line-height: 1.5;
        }}

        @media (max-width: 900px) {{
            .page {{
                grid-template-columns: 1fr;
                gap: 34px;
            }}

            .cake-card {{
                max-width: 520px;
            }}
        }}

        @media (max-width: 620px) {{
            .page {{
                width: min(100% - 24px, 1120px);
                padding: 28px 0;
            }}

            .features {{
                grid-template-columns: 1fr;
            }}

            .lead {{
                font-size: 17px;
            }}
        }}
    </style>
</head>
<body>
    <main class="page">
        <section class="hero">
            <p class="eyebrow">Tiệm bánh gradient tím xanh</p>
            <h1>Bánh kem ngọt ngào cho buổi tiệc lung linh.</h1>
            <p class="lead">
                Thiết kế lấy cảm hứng từ sắc tím lavender, xanh biển và lớp kem ombre mềm mại.
                Phù hợp cho sinh nhật, kỷ niệm hoặc những bữa tiệc cần một điểm nhấn thật nổi bật.
            </p>

            <div class="actions">
                <a class="button" href="#cake">Xem mẫu bánh</a>
                <a class="button secondary" href="{PINTEREST_PIN_URL}" target="_blank" rel="noreferrer">Nguồn Pinterest</a>
            </div>

            <div class="features" aria-label="Điểm nổi bật">
                <div class="feature">
                    <strong>Ombre kem mịn</strong>
                    <span>Lớp màu chuyển nhẹ từ tím sang xanh tạo cảm giác hiện đại.</span>
                </div>
                <div class="feature">
                    <strong>Trang trí nổi bật</strong>
                    <span>Rosette, drip trắng và hạt đường giúp chiếc bánh sáng sân khấu.</span>
                </div>
                <div class="feature">
                    <strong>Tông tiệc mơ màng</strong>
                    <span>Bảng màu dịu nhưng đủ rực rỡ cho ảnh check-in.</span>
                </div>
            </div>
        </section>

        <article class="cake-card" id="cake">
            <img src="{CAKE_IMAGE_URL}" alt="Bánh kem tím xanh từ Pinterest">
            <div class="cake-info">
                <h2>Purple Blue Drip Cake</h2>
                <p>
                    Một mẫu bánh kem ombre tím xanh với lớp drip trắng, kem bắt bông phía trên
                    và phần rắc trang trí ở chân bánh.
                </p>
            </div>
        </article>
    </main>
</body>
</html>
"""


class CakePageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404, "Not found")
            return

        content = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), CakePageHandler)
    print(f"Sweet Galaxy Cake is running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
