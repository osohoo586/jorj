import math
import random
import time
import turtle


def heart_x(t):
    return 15 * math.sin(t) ** 3


def heart_y(t):
    return (
        12 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    )


def draw_heart_5s(scale=18, steps=500, color="red", delay=0.01):
    """
    Draw heart from center in ~5 seconds
    """
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("❤️ Heart Animation ~5s")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(1)
    t.color(color)

    # Compute points
    points = [
        (
            heart_x((i / steps) * 2 * math.pi) * scale,
            heart_y((i / steps) * 2 * math.pi) * scale,
        )
        for i in range(steps + 1)
    ]

    # Random order for center lines
    indices = list(range(len(points)))
    random.shuffle(indices)

    print("Зүрх зурж эхэлж байна...")
    for i, idx in enumerate(indices):
        x, y = points[idx]
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.goto(x, y)
        time.sleep(delay)  # adjust for total duration

        if i % 50 == 0:
            print(f"⏳ Зурж байна... {i}/{steps} ({i * 100 // steps}%)")

    print("✅ Зүрх зурагдлаа!")

    # Романтик мессежүүд харуулах
    time.sleep(1)
    show_romantic_message(screen, t)

    screen.exitonclick()


def show_romantic_message(screen, t):
    """
    Романтик мессежүүдийг анимэйшнтэй харуулах
    """
    # Зүрхийг арилгах
    t.clear()

    # Screen setup for better text rendering
    screen.tracer(0)

    # Эхний мессеж: "Би зүгээр л 10 минутад"
    message1 = "Би зүгээр л 10 минутад"

    # Үсэг бүрийг анимэйшнтэй гаргах
    for i in range(len(message1) + 1):
        t.clear()
        t.penup()
        t.goto(0, 50)
        t.color("#FF69B4")
        t.write(message1[:i], align="center", font=("MS Gothic", 32, "bold"))
        screen.update()
        time.sleep(0.1)

    # Жаахан хүлээх
    time.sleep(1.5)

    # Fade out эффект
    for _ in range(3):
        t.clear()
        screen.update()
        time.sleep(0.2)
        t.penup()
        t.goto(0, 50)
        t.color("#FF69B4")
        t.write(message1, align="center", font=("MS Gothic", 32, "bold"))
        screen.update()
        time.sleep(0.2)

    t.clear()
    screen.update()
    time.sleep(0.5)

    # Хоёр дахь мессеж: "Чамд дурлачихсан" - Романтик анимэйшнтэй
    romantic_animation(screen, t)


def romantic_animation(screen, t):
    """
    "Чамд дурлачихсан" гэсэн романтик анимэйшн
    """
    message2 = "Чамд дурлачихсан 💖"

    # Үсэг бүрийг том болгож гаргах
    for i in range(len(message2) + 1):
        t.clear()

        # Жижиг зүрхнүүд эргэн тойронд зурах
        draw_small_hearts_around(t)

        # Пульс эффект
        size = 28 + (i % 3) * 4  # 28-36 хооронд хэлбэлзэх
        t.penup()
        t.goto(0, 0)
        t.color("#FF1493")
        t.write(message2[:i], align="center", font=("MS Gothic", size, "bold"))
        screen.update()
        time.sleep(0.15)

    # Финал: Пульс эффектээр харуулах
    for pulse in range(8):
        t.clear()
        draw_small_hearts_around(t)

        if pulse % 2 == 0:
            size = 36
            t.color("#FF1493")
        else:
            size = 32
            t.color("#FF69B4")

        t.penup()
        t.goto(0, 0)
        t.write(message2, align="center", font=("MS Gothic", size, "bold"))
        screen.update()
        time.sleep(0.3)

    # Эцсийн харагдац
    t.clear()
    draw_small_hearts_around(t)

    # Сүүлийн sparkle эффект
    for _ in range(3):
        draw_sparkles(t)
        screen.update()
        time.sleep(0.3)

    t.color("#FF1493")
    t.penup()
    t.goto(0, 0)
    t.write(message2, align="center", font=("MS Gothic", 36, "bold"))
    screen.update()


def draw_small_hearts_around(t):
    """
    Жижиг зүрхнүүдийг эргэн тойронд зурах
    """
    positions = [
        (-250, 200), (-200, 220), (-150, 230),
        (150, 230), (200, 220), (250, 200),
        (-250, -200), (-200, -220), (-150, -230),
        (150, -230), (200, -220), (250, -200),
    ]

    t.pensize(1)
    for x, y in positions:
        # Жижиг зүрх зурах
        draw_mini_heart(t, x, y, scale=1.5, color="#FFB6C1")


def draw_mini_heart(t, x, y, scale=1, color="pink"):
    """
    Жижиг зүрх зурах
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()

    # Зүрхний хэлбэр
    for i in range(20):
        angle = (i / 20) * 2 * math.pi
        hx = heart_x(angle) * scale
        hy = heart_y(angle) * scale
        t.goto(x + hx, y + hy)

    t.end_fill()
    t.penup()


def draw_sparkles(t):
    """
    Гялалзах од зурах
    """
    sparkle_positions = [
        (-280, 0), (-240, 100), (-200, -100),
        (280, 0), (240, 100), (200, -100),
        (0, 250), (0, -250)
    ]

    t.color("#FFFF00")  # Шар өнгө
    for x, y in sparkle_positions:
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Одны хэлбэр
        for _ in range(4):
            t.forward(10)
            t.backward(10)
            t.right(45)

        # Жижиг тойрог
        t.penup()
        t.goto(x, y - 3)
        t.pendown()
        t.circle(3)

    t.penup()


if __name__ == "__main__":
    # delay утгыг багасгах = илүү хурдан
    # 0.001 = маш хурдан
    # 0.005 = хурдан
    # 0.01 = дунд хурд
    draw_heart_5s(scale=18, steps=500, color="red", delay=0.001)
