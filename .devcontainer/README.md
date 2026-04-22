# Hướng dẫn chạy Frappe LMS trên GitHub Codespaces

## Cách mở Codespace (lần đầu)

1. Truy cập repo fork của bạn trên GitHub: `https://github.com/tuanbiofficial-commits/daotaobiluxury`
2. Bấm nút **Code** (xanh lá, góc phải) → tab **Codespaces** → **Create codespace on develop**
3. Chọn máy cấu hình tối thiểu **4-core / 8GB RAM** (mặc định 2-core không đủ).
4. Đợi ~10 phút cho lần đầu (bench init + cài LMS).
5. Khi thấy log `SystemInit... bench start`, trình duyệt tự mở port 8000.
6. Đăng nhập: **Administrator / admin**

## Lần mở sau

- Chỉ mất ~30 giây (đã cache bench + database).
- Vẫn mở từ tab **Codespaces** → chọn codespace cũ → **Resume**.

## Dừng / Xoá

- **Dừng** (giữ nguyên dữ liệu, tiếp tục tính phí storage ~$0.07/GB/ngày): Codespaces → ⋯ → Stop codespace.
- **Xoá hẳn**: Codespaces → ⋯ → Delete (làm lại setup từ đầu nếu cần).

## Lưu ý free tier

- 60 giờ/tháng miễn phí với máy 2-core. Máy 4-core tính ×2 → còn 30 giờ/tháng.
- Tắt codespace khi không dùng để tiết kiệm giờ.
