import time

import uiautomator2 as u2

no_rob = []
d = u2.connect()
# d.debug = True
d.app_start("com.tencent.mm", stop=True)
time.sleep(5)
print("开始等待红包。。。")
while True:
    home_btn = d(className="android.widget.RelativeLayout", resourceId="com.tencent.mm:id/nvt")
    if home_btn.exists and len(home_btn) == 4:
        home_btn[0].click()
    chat_list = d(className="android.widget.LinearLayout", resourceId="com.tencent.mm:id/cj1")
    if chat_list.exists:
        for chat_item in chat_list:
            sender_div = chat_item.child(className="android.view.View", resourceId="com.tencent.mm:id/kbq")
            sender = sender_div.get_text() if sender_div.exists else ""
            message_div = chat_item.child(className="android.view.View", resourceId="com.tencent.mm:id/ht5")
            if message_div.exists:
                message = message_div.get_text()
                if "[微信红包]" in message and sender not in no_rob:
                    print("发现红包，进入红包页面")
                    chat_item.click()
                    no_rob.append(sender)
                    time.sleep(0.5)
                    # red_btn = d(className="android.widget.LinearLayout", resourceId="com.tencent.mm:id/b4t")
                    red_div = d(className="android.widget.FrameLayout", resourceId="com.tencent.mm:id/bkg")
                    if red_div.exists:
                        red_div = red_div[-1]
                        red_btn = red_div.child(className="android.widget.LinearLayout", resourceId="com.tencent.mm:id/b4t")
                        if red_btn.exists:
                            red_div.click()
                            # d.double_click(red_btn[-1].center()[0], red_btn[-1].center()[1])
                            time.sleep(0.5)
                            # 点击开红包
                            open_btn = d(className="android.widget.ImageButton", resourceId="com.tencent.mm:id/j6h", description="开")
                            if open_btn.exists:
                                open_btn.click()
                                time.sleep(0.8)
                    # 退到首页
                    while True:
                        home_btn = d(className="android.widget.RelativeLayout", resourceId="com.tencent.mm:id/nvt")
                        if home_btn.exists:
                            break
                        d.press("back")
                        time.sleep(0.3)
                elif "[微信红包]" not in message and sender in no_rob:
                    no_rob.remove(sender)
    time.sleep(0.3)
