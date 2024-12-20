import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QPushButton, QLabel, QSlider, QFileDialog)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from PIL import Image, ImageFilter
import io

class ImageBlurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图像模糊调节")

        # 初始控件
        self.open_button = QPushButton("打开图像")
        self.open_button.clicked.connect(self.open_image)

        self.image_label = QLabel("请先打开一张图片")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.blur_slider = QSlider(Qt.Horizontal)
        self.blur_slider.setMinimum(0)
        self.blur_slider.setMaximum(20)
        self.blur_slider.setValue(0)
        self.blur_slider.setTickPosition(QSlider.TicksBelow)
        self.blur_slider.setTickInterval(1)
        self.blur_slider.setEnabled(False)  # 未载入图像前不启用
        self.blur_slider.valueChanged.connect(self.update_image)

        # 布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.open_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.blur_slider)

        self.setCentralWidget(central_widget)

        # 保存图像数据的变量
        self.original_image = None

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图像文件", "", "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            self.original_image = Image.open(file_name)
            self.display_image(self.original_image)
            self.blur_slider.setEnabled(True)
            self.blur_slider.setValue(0)

    def update_image(self, value):
        if self.original_image is not None:
            # 使用PIL进行模糊滤镜处理
            blurred_image = self.original_image.filter(ImageFilter.GaussianBlur(radius=value))
            self.display_image(blurred_image)

    def display_image(self, pil_image):
        # 将PIL图像转换为Qt可显示的QPixmap
        # 首先将PIL图像转换为字节数据
        buf = io.BytesIO()
        pil_image.save(buf, format="PNG")
        qimage = QImage.fromData(buf.getvalue(), "PNG")
        pixmap = QPixmap.fromImage(qimage)

        # 调整显示区域大小（可选）
        # 比如固定大小，也可以自动缩放
        pixmap = pixmap.scaled(QSize(400, 400), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageBlurWindow()
    window.resize(600, 500)
    window.show()
    sys.exit(app.exec())
