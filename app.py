from http.server import BaseHTTPRequestHandler, HTTPServer
import os


HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8001))

PINTEREST_PIN_URL = "https://www.pinterest.com/pin/6685099435977519/"

PRODUCTS = [
    {
        "id": "purple-blue-drip",
        "name": "Purple Blue Drip Cake",
        "price": 420000,
        "badge": "Bán chạy",
        "image": "https://i.pinimg.com/736x/90/47/47/904747e3be82b47fb1c2a28585f81d39.jpg",
        "description": "Bánh ombre tím xanh, phủ drip trắng và kem bắt bông nổi bật.",
    },
    {
        "id": "strawberry-cloud",
        "name": "Strawberry Cloud",
        "price": 390000,
        "badge": "Mới",
        "image": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?auto=format&fit=crop&w=900&q=80",
        "description": "Kem vanilla mềm, dâu tươi và lớp phủ hồng nhẹ cho tiệc sinh nhật.",
    },
    {
        "id": "matcha-garden",
        "name": "Matcha Garden",
        "price": 360000,
        "badge": "Ít ngọt",
        "image": "https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?auto=format&fit=crop&w=900&q=80",
        "description": "Vị trà xanh thanh, trang trí kem trắng và vụn bánh giòn.",
    },
    {
        "id": "choco-midnight",
        "name": "Choco Midnight",
        "price": 450000,
        "badge": "Đậm vị",
        "image": "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?auto=format&fit=crop&w=900&q=80",
        "description": "Socola nhiều tầng, ganache bóng và nhân cacao đậm.",
    },
    {
        "id": "mango-sunrise",
        "name": "Mango Sunrise",
        "price": 410000,
        "badge": "Trái cây",
        "image": "https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=900&q=80",
        "description": "Kem xoài, sponge cake mềm và lớp trái cây nhiệt đới tươi.",
    },
    {
        "id": "red-velvet-rose",
        "name": "Red Velvet Rose",
        "price": 430000,
        "badge": "Quà tặng",
        "image": "https://images.unsplash.com/photo-1586985289906-406988974504?auto=format&fit=crop&w=900&q=80",
        "description": "Cốt red velvet, cream cheese và trang trí hoa kem tinh tế.",
    },
]


def money(value):
    return f"{value:,}".replace(",", ".") + "đ"


def product_cards():
    cards = []
    for product in PRODUCTS:
        cards.append(
            f"""
            <article class="product-card">
                <div class="product-media">
                    <img src="{product["image"]}" alt="{product["name"]}" loading="lazy">
                    <span>{product["badge"]}</span>
                </div>
                <div class="product-info">
                    <h3>{product["name"]}</h3>
                    <p>{product["description"]}</p>
                    <div class="product-purchase">
                        <strong>{money(product["price"])}</strong>
                        <button
                            class="cart-button"
                            type="button"
                            data-id="{product["id"]}"
                            data-name="{product["name"]}"
                            data-price="{product["price"]}"
                        >
                            Thêm vào giỏ
                        </button>
                    </div>
                </div>
            </article>
            """
        )
    return "\n".join(cards)


HTML = f"""<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sweet Galaxy Cake</title>
    <style>
        :root {{
            --berry: #b91c5c;
            --plum: #5b2a86;
            --leaf: #15803d;
            --sun: #f59e0b;
            --cream: #fff8ef;
            --paper: #ffffff;
            --ink: #172033;
            --muted: #63708a;
            --line: #eadfda;
            --shadow: 0 18px 48px rgba(31, 24, 39, 0.16);
        }}

        * {{
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            margin: 0;
            min-height: 100vh;
            color: var(--ink);
            font-family: "Segoe UI", Arial, sans-serif;
            background: var(--cream);
        }}

        button, a {{
            font: inherit;
        }}

        .site-header {{
            position: sticky;
            top: 0;
            z-index: 20;
            border-bottom: 1px solid rgba(234, 223, 218, 0.9);
            background: rgba(255, 248, 239, 0.94);
            backdrop-filter: blur(14px);
        }}

        .nav {{
            width: min(1180px, calc(100% - 32px));
            height: 72px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
        }}

        .brand {{
            color: var(--ink);
            text-decoration: none;
            font-size: 19px;
            font-weight: 900;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .nav-links a {{
            color: var(--muted);
            text-decoration: none;
            font-size: 14px;
            font-weight: 700;
        }}

        .cart-toggle {{
            position: relative;
            min-height: 42px;
            border: 0;
            border-radius: 8px;
            padding: 0 16px;
            color: white;
            background: var(--berry);
            font-weight: 800;
            cursor: pointer;
        }}

        .cart-toggle span {{
            display: inline-grid;
            min-width: 22px;
            height: 22px;
            margin-left: 8px;
            place-items: center;
            border-radius: 999px;
            color: var(--berry);
            background: white;
            font-size: 12px;
        }}

        .hero-band {{
            background:
                linear-gradient(90deg, rgba(91, 42, 134, 0.92), rgba(185, 28, 92, 0.78)),
                url("https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1800&q=80") center / cover;
            color: white;
        }}

        .hero {{
            width: min(1180px, calc(100% - 32px));
            min-height: calc(100vh - 72px);
            margin: 0 auto;
            display: grid;
            grid-template-columns: minmax(0, 1fr) 420px;
            align-items: center;
            gap: 46px;
            padding: 58px 0 72px;
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            margin: 0 0 18px;
            padding: 8px 14px;
            border: 1px solid rgba(255, 255, 255, 0.34);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.14);
            font-size: 14px;
            font-weight: 800;
        }}

        h1 {{
            max-width: 760px;
            margin: 0;
            font-size: clamp(42px, 7vw, 78px);
            line-height: 0.98;
            letter-spacing: 0;
        }}

        .lead {{
            max-width: 620px;
            margin: 24px 0 0;
            color: rgba(255, 255, 255, 0.9);
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
            border-radius: 8px;
            padding: 0 22px;
            color: var(--ink);
            background: white;
            text-decoration: none;
            font-weight: 900;
            box-shadow: 0 18px 40px rgba(23, 32, 51, 0.18);
        }}

        .button.secondary {{
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.38);
            background: rgba(255, 255, 255, 0.12);
            box-shadow: none;
        }}

        .hero-card {{
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.42);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.86);
            box-shadow: var(--shadow);
        }}

        .hero-card img {{
            display: block;
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
        }}

        .hero-card div {{
            padding: 22px;
            color: var(--ink);
        }}

        .hero-card h2 {{
            margin: 0 0 8px;
            font-size: 24px;
        }}

        .hero-card p {{
            margin: 0;
            color: var(--muted);
            line-height: 1.55;
        }}

        .section {{
            width: min(1180px, calc(100% - 32px));
            margin: 0 auto;
            padding: 70px 0;
        }}

        .section-title {{
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 24px;
            margin-bottom: 26px;
        }}

        .section-title h2 {{
            margin: 0;
            font-size: clamp(30px, 4vw, 44px);
            line-height: 1.08;
        }}

        .section-title p {{
            max-width: 500px;
            margin: 0;
            color: var(--muted);
            line-height: 1.6;
        }}

        .products {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 20px;
        }}

        .product-card {{
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--paper);
            box-shadow: 0 10px 28px rgba(31, 24, 39, 0.08);
        }}

        .product-media {{
            position: relative;
            background: #f4ede8;
        }}

        .product-media img {{
            display: block;
            width: 100%;
            aspect-ratio: 4 / 3;
            object-fit: cover;
        }}

        .product-media span {{
            position: absolute;
            top: 12px;
            left: 12px;
            border-radius: 999px;
            padding: 6px 10px;
            color: white;
            background: rgba(23, 32, 51, 0.78);
            font-size: 12px;
            font-weight: 800;
        }}

        .product-info {{
            padding: 18px;
        }}

        .product-info h3 {{
            margin: 0 0 8px;
            font-size: 20px;
        }}

        .product-info p {{
            min-height: 70px;
            margin: 0;
            color: var(--muted);
            line-height: 1.55;
        }}

        .product-purchase {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-top: 18px;
        }}

        .product-purchase strong {{
            color: var(--plum);
            font-size: 19px;
            white-space: nowrap;
        }}

        .cart-button {{
            min-height: 42px;
            border: 0;
            border-radius: 8px;
            padding: 0 14px;
            color: white;
            background: var(--leaf);
            font-weight: 800;
            cursor: pointer;
            white-space: nowrap;
        }}

        .benefits-band {{
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
            background: white;
        }}

        .benefits {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }}

        .benefit {{
            border-left: 4px solid var(--sun);
            padding: 10px 0 10px 16px;
        }}

        .benefit strong {{
            display: block;
            margin-bottom: 6px;
        }}

        .benefit span {{
            color: var(--muted);
            line-height: 1.55;
        }}

        .cart-panel {{
            position: fixed;
            inset: 0 0 0 auto;
            z-index: 40;
            width: min(420px, 100%);
            display: grid;
            grid-template-rows: auto 1fr auto;
            background: white;
            box-shadow: -22px 0 60px rgba(23, 32, 51, 0.22);
            transform: translateX(104%);
            transition: transform 180ms ease;
        }}

        .cart-panel.open {{
            transform: translateX(0);
        }}

        .cart-head {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--line);
            padding: 20px;
        }}

        .cart-head h2 {{
            margin: 0;
            font-size: 24px;
        }}

        .close-cart {{
            width: 40px;
            height: 40px;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: white;
            cursor: pointer;
            font-size: 22px;
            line-height: 1;
        }}

        .cart-items {{
            overflow: auto;
            padding: 14px 20px;
        }}

        .empty-cart {{
            margin: 18px 0;
            color: var(--muted);
            line-height: 1.6;
        }}

        .cart-item {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 12px;
            border-bottom: 1px solid var(--line);
            padding: 14px 0;
        }}

        .cart-item h3 {{
            margin: 0 0 5px;
            font-size: 16px;
        }}

        .cart-item p {{
            margin: 0;
            color: var(--muted);
            font-size: 14px;
        }}

        .quantity {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .quantity button {{
            width: 32px;
            height: 32px;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--cream);
            cursor: pointer;
            font-weight: 900;
        }}

        .cart-foot {{
            border-top: 1px solid var(--line);
            padding: 20px;
        }}

        .total-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 14px;
            font-size: 20px;
            font-weight: 900;
        }}

        .checkout {{
            width: 100%;
            min-height: 48px;
            border: 0;
            border-radius: 8px;
            color: white;
            background: var(--berry);
            font-weight: 900;
            cursor: pointer;
        }}

        .checkout-note {{
            margin: 10px 0 0;
            color: var(--muted);
            font-size: 13px;
            line-height: 1.5;
        }}

        .toast {{
            position: fixed;
            right: 20px;
            bottom: 20px;
            z-index: 50;
            max-width: min(340px, calc(100% - 40px));
            border-radius: 8px;
            padding: 14px 16px;
            color: white;
            background: rgba(23, 32, 51, 0.94);
            opacity: 0;
            transform: translateY(12px);
            transition: opacity 160ms ease, transform 160ms ease;
            pointer-events: none;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        @media (max-width: 980px) {{
            .hero {{
                grid-template-columns: 1fr;
                min-height: auto;
            }}

            .hero-card {{
                max-width: 520px;
            }}

            .products {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}

            .section-title {{
                align-items: start;
                flex-direction: column;
            }}
        }}

        @media (max-width: 680px) {{
            .nav {{
                width: min(100% - 24px, 1180px);
                height: auto;
                padding: 14px 0;
                align-items: start;
                flex-direction: column;
            }}

            .nav-links {{
                width: 100%;
                justify-content: space-between;
            }}

            .hero, .section {{
                width: min(100% - 24px, 1180px);
            }}

            .hero {{
                padding: 42px 0 54px;
            }}

            .lead {{
                font-size: 17px;
            }}

            .products, .benefits {{
                grid-template-columns: 1fr;
            }}

            .product-purchase {{
                align-items: stretch;
                flex-direction: column;
            }}

            .cart-button {{
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <header class="site-header">
        <nav class="nav" aria-label="Điều hướng chính">
            <a class="brand" href="#">Sweet Galaxy Cake</a>
            <div class="nav-links">
                <a href="#products">Sản phẩm</a>
                <a href="{PINTEREST_PIN_URL}" target="_blank" rel="noreferrer">Nguồn mẫu</a>
                <button class="cart-toggle" type="button" id="openCart">Giỏ hàng <span id="cartCount">0</span></button>
            </div>
        </nav>
    </header>

    <main>
        <section class="hero-band">
            <div class="hero">
                <div>
                    <p class="eyebrow">Tiệm bánh thiết kế theo yêu cầu</p>
                    <h1>Bánh kem ngọt ngào cho buổi tiệc lung linh.</h1>
                    <p class="lead">
                        Chọn mẫu bánh yêu thích, thêm vào giỏ hàng và đặt nhanh cho sinh nhật,
                        kỷ niệm hoặc những bữa tiệc cần một điểm nhấn thật nổi bật.
                    </p>

                    <div class="actions">
                        <a class="button" href="#products">Xem sản phẩm</a>
                        <button class="button secondary" type="button" id="heroCartButton">Mở giỏ hàng</button>
                    </div>
                </div>

                <article class="hero-card">
                    <img src="{PRODUCTS[0]["image"]}" alt="{PRODUCTS[0]["name"]}">
                    <div>
                        <h2>{PRODUCTS[0]["name"]}</h2>
                        <p>{PRODUCTS[0]["description"]}</p>
                    </div>
                </article>
            </div>
        </section>

        <section class="section" id="products">
            <div class="section-title">
                <h2>Sản phẩm nổi bật</h2>
                <p>
                    Nhiều lựa chọn hơn cho tiệc nhỏ, tiệc gia đình và quà tặng.
                    Mỗi mẫu đều có thể điều chỉnh màu sắc, chữ viết và kích thước.
                </p>
            </div>

            <div class="products">
                {product_cards()}
            </div>
        </section>

        <section class="benefits-band">
            <div class="section benefits">
                <div class="benefit">
                    <strong>Làm mới trong ngày</strong>
                    <span>Bánh được chuẩn bị theo đơn, giữ kem mềm và cốt bánh ẩm.</span>
                </div>
                <div class="benefit">
                    <strong>Tùy chỉnh lời chúc</strong>
                    <span>Thêm tên, tuổi, ngày kỷ niệm hoặc màu chủ đề của buổi tiệc.</span>
                </div>
                <div class="benefit">
                    <strong>Gợi ý kích thước</strong>
                    <span>Hỗ trợ chọn size phù hợp số người dùng trước khi xác nhận đơn.</span>
                </div>
            </div>
        </section>
    </main>

    <aside class="cart-panel" id="cartPanel" aria-label="Giỏ hàng" aria-hidden="true">
        <div class="cart-head">
            <h2>Giỏ hàng</h2>
            <button class="close-cart" type="button" id="closeCart" aria-label="Đóng giỏ hàng">x</button>
        </div>
        <div class="cart-items" id="cartItems">
            <p class="empty-cart">Giỏ hàng đang trống. Hãy chọn một mẫu bánh bạn thích.</p>
        </div>
        <div class="cart-foot">
            <div class="total-row">
                <span>Tổng cộng</span>
                <span id="cartTotal">0đ</span>
            </div>
            <button class="checkout" type="button" id="checkoutButton">Đặt bánh</button>
            <p class="checkout-note">Nút đặt bánh hiện hiển thị thông báo xác nhận trên trang demo.</p>
        </div>
    </aside>

    <div class="toast" id="toast" role="status" aria-live="polite"></div>

    <script>
        const cart = new Map();
        const cartPanel = document.getElementById("cartPanel");
        const cartItems = document.getElementById("cartItems");
        const cartCount = document.getElementById("cartCount");
        const cartTotal = document.getElementById("cartTotal");
        const toast = document.getElementById("toast");
        let toastTimer;

        const formatMoney = (value) => new Intl.NumberFormat("vi-VN").format(value) + "đ";

        function showToast(message) {{
            toast.textContent = message;
            toast.classList.add("show");
            clearTimeout(toastTimer);
            toastTimer = setTimeout(() => toast.classList.remove("show"), 1800);
        }}

        function openCart() {{
            cartPanel.classList.add("open");
            cartPanel.setAttribute("aria-hidden", "false");
        }}

        function closeCart() {{
            cartPanel.classList.remove("open");
            cartPanel.setAttribute("aria-hidden", "true");
        }}

        function updateCart() {{
            const items = Array.from(cart.values());
            const count = items.reduce((sum, item) => sum + item.quantity, 0);
            const total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);

            cartCount.textContent = count;
            cartTotal.textContent = formatMoney(total);

            if (!items.length) {{
                cartItems.innerHTML = '<p class="empty-cart">Giỏ hàng đang trống. Hãy chọn một mẫu bánh bạn thích.</p>';
                return;
            }}

            cartItems.innerHTML = items.map((item) => `
                <div class="cart-item">
                    <div>
                        <h3>${{item.name}}</h3>
                        <p>${{formatMoney(item.price)}} x ${{item.quantity}}</p>
                    </div>
                    <div class="quantity" aria-label="Số lượng ${{item.name}}">
                        <button type="button" data-action="decrease" data-id="${{item.id}}">-</button>
                        <strong>${{item.quantity}}</strong>
                        <button type="button" data-action="increase" data-id="${{item.id}}">+</button>
                    </div>
                </div>
            `).join("");
        }}

        function addToCart(product) {{
            const current = cart.get(product.id);
            if (current) {{
                current.quantity += 1;
            }} else {{
                cart.set(product.id, {{ ...product, quantity: 1 }});
            }}
            updateCart();
            showToast(`Đã thêm "${{product.name}}" vào giỏ hàng.`);
        }}

        document.querySelectorAll(".cart-button").forEach((button) => {{
            button.addEventListener("click", () => {{
                addToCart({{
                    id: button.dataset.id,
                    name: button.dataset.name,
                    price: Number(button.dataset.price),
                }});
            }});
        }});

        cartItems.addEventListener("click", (event) => {{
            const button = event.target.closest("button[data-action]");
            if (!button) return;

            const item = cart.get(button.dataset.id);
            if (!item) return;

            if (button.dataset.action === "increase") {{
                item.quantity += 1;
            }} else {{
                item.quantity -= 1;
                if (item.quantity <= 0) {{
                    cart.delete(item.id);
                }}
            }}
            updateCart();
        }});

        document.getElementById("openCart").addEventListener("click", openCart);
        document.getElementById("heroCartButton").addEventListener("click", openCart);
        document.getElementById("closeCart").addEventListener("click", closeCart);

        document.getElementById("checkoutButton").addEventListener("click", () => {{
            const count = Array.from(cart.values()).reduce((sum, item) => sum + item.quantity, 0);
            if (!count) {{
                showToast("Giỏ hàng đang trống.");
                return;
            }}
            showToast("Đã ghi nhận đơn bánh. Tiệm sẽ liên hệ để xác nhận chi tiết.");
        }});

        document.addEventListener("keydown", (event) => {{
            if (event.key === "Escape") closeCart();
        }});

        updateCart();
    </script>
</body>
</html>
"""


class CakePageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request:", self.path)

        content = HTML.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()

        self.wfile.write(content)
        self.wfile.flush()


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), CakePageHandler)
    print(f"Sweet Galaxy Cake is running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
