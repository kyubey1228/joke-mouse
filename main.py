import pyautogui
import time
import random

pyautogui.FAILSAFE = True

try:
    while True:
        # 画面の解像度を取得
        screen_width, screen_height = pyautogui.size()

        # ランダムな座標を生成
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # マウスを2秒かけてその位置まで移動
        pyautogui.moveTo(x, y, duration=2)

        # 3秒待機
        time.sleep(3)

except KeyboardInterrupt:
    print("プログラムを終了します")
