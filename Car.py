import cv2

# Thiết lập chiều rộng và chiều cao khung hình
frameWidth = 640
frameHeight = 480

# Tải bộ phân loại Haar Cascade cho việc phát hiện biển số xe
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

# Thiết lập ngưỡng diện tích nhỏ nhất và màu cho khung chữ nhật
minArea = 200
color = (255, 0, 255)

# Mở video từ tệp
cap = cv2.VideoCapture("Resource/video12.mp4")
cap.set(3, frameWidth)  # Đặt chiều rộng của khung hình
cap.set(4, frameHeight)  # Đặt chiều cao của khung hình
cap.set(10, 150)  # Đặt độ sáng của khung hình

count = 0

while True:
    success, img = cap.read()  # Đọc khung hình từ video
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Chuyển đổi khung hình sang màu xám
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)  # Phát hiện biển số xe

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)  # Vẽ hình chữ nhật quanh biển số
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)  # Thêm chữ "Number Plate"
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)  # Hiển thị khung hình kết quả

    if cv2.waitKey(1) & 0xFF == ord('s'):  # Nhấn phím 's' để lưu hình ảnh
        cv2.imwrite("Resources/NoPlate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

cap.release()  # Giải phóng video
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ hiển thị
