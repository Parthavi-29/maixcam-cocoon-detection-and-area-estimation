from maix import camera, display, image, nn, app, tracker, gpio, touchscreen
import math

# -----------------------------
# LED setup
# -----------------------------
led = gpio.GPIO("A0", gpio.Mode.OUT)
led.value(0)

# -----------------------------
# Model
# -----------------------------
model_path = "/root/cocoon/cocoonp2.maixcam/cocoon.mud"
print("Loading model:", model_path)

detector = nn.YOLOv5(model=model_path)

# -----------------------------
# Camera & Display
# -----------------------------
cam = camera.Camera(
    detector.input_width(),
    detector.input_height(),
    detector.input_format()
)

disp = display.Display()
ts = touchscreen.TouchScreen()

tracker0 = tracker.ByteTracker()

# -----------------------------
# Counter
# -----------------------------
count = 0
counted_ids = []

count_line_y = cam.height() // 2

# -----------------------------
# Calibration
# -----------------------------
CM_PER_PIXEL = 0.05

# -----------------------------
# EXIT BUTTON
# -----------------------------
exit_label = "< EXIT"
exit_btn_pos = [0, 0, 80, 40]

def is_in_button(x, y, btn):
    return x > btn[0] and x < btn[0] + btn[2] and y > btn[1] and y < btn[1] + btn[3]

# -----------------------------
# Store FINAL area only
# -----------------------------
final_area = 0

# -----------------------------
# Main loop
# -----------------------------
while not app.need_exit():

    img = cam.read()

    # TOUCH
    x_t, y_t, pressed = ts.read()

    if pressed:
        if disp.width() != cam.width():
            x_t = int(x_t * cam.width() / disp.width())
            y_t = int(y_t * cam.height() / disp.height())

        if is_in_button(x_t, y_t, exit_btn_pos):
            print("EXIT pressed")
            app.set_exit_flag(True)

    # Detection
    objs = detector.detect(img, conf_th=0.5, iou_th=0.45)

    track_objs = []
    for obj in objs:
        track_objs.append(
            tracker.Object(obj.x, obj.y, obj.w, obj.h, obj.class_id, obj.score)
        )

    tracks = tracker0.update(track_objs)

    img.draw_line(0, count_line_y, cam.width(), count_line_y, image.COLOR_YELLOW, 2)

    for track in tracks:

        if track.lost:
            continue

        obj = track.history[-1]
        cy = obj.y + obj.h // 2

        img.draw_rect(obj.x, obj.y, obj.w, obj.h, image.COLOR_RED)

        x = max(0, obj.x)
        y = max(0, obj.y)
        w = min(obj.w, cam.width() - x)
        h = min(obj.h, cam.height() - y)

        if w <= 0 or h <= 0:
            continue

        roi = img.crop(x, y, w, h)

        blobs = roi.find_blobs([(60,255)], pixels_threshold=50)

        largest = 0
        for b in blobs:
            if b.pixels() > largest:
                largest = b.pixels()

        if largest == 0:
            continue

        pixel_area = largest

        area = pixel_area * (CM_PER_PIXEL ** 2) - 3

        # -----------------------------
        # COUNTING (store FINAL area)
        # -----------------------------
        if cy > count_line_y and track.id not in counted_ids:

            count += 1
            counted_ids.append(track.id)

            final_area = area  # ONLY store when counted

            print("Cocoon:", count, "| Area:", round(area,2), "cm^2")

            if count == 100:
                led.value(1)
                app.sleep_ms(1000)
                led.value(0)

                count = 0
                counted_ids = []

        # keep original display
        img.draw_string(x, y - 10, f"A:{area:.2f}cm2", image.COLOR_GREEN)

    # EXIT button
    img.draw_rect(exit_btn_pos[0], exit_btn_pos[1],
                  exit_btn_pos[2], exit_btn_pos[3],
                  image.COLOR_RED, 2)
    img.draw_string(5, 10, exit_label, image.COLOR_RED)

    # -----------------------------
    # DISPLAY FINAL AREA (TOP RIGHT)
    # -----------------------------
    img.draw_string(
        cam.width() - 120,
        10,
        f"A:{final_area:.2f}",
        image.COLOR_GREEN
    )

    # Count
    img.draw_string(10, 80, f"Count:{count}", image.COLOR_GREEN, scale=2)

    disp.show(img)