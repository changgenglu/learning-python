import random
import time
import os

def draw_lottery(lottery_pool):
  """從籤桶中抽取一支籤並移除"""
  if not lottery_pool:
    return None

  selected_lottery = random.choice(lottery_pool)
  lottery_pool.remove(selected_lottery)
  return selected_lottery

def clear_console():
    """清除終端機畫面"""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_select():
    while True:
      check_action = input("請輸入 'ok' 進行抽籤，或 'change' 重新選擇籤桶：")
      if check_action.lower() == "change":
        clear_console()
        main()
      elif check_action.lower() == "ok":
        clear_console()
        break
      else:
        print("輸入無效，請重新輸入。")
        print()

def main():
  member_lottery_pool = ["ivan", "kenny", "parker", "jeremy", "rita"]
  dish_lottery_pool = [
    "蘆筍炒磨菇", "芹菜炒豬肉", "泰式咖哩雞", "蔥香煎肉餅", "香菜洋蔥炒豬肉", "港式咖哩蘿蔔魚蛋", "茭白筍炒三絲",
    "番茄牛肉湯", "蒜香奶油蘑菇", "桂竹筍炒五花肉", "番茄燉豬肋排", "鑄鐵鍋墨西哥肉醬 pizza", "香煎雞腿佐時蔬",
    "蘇炸洋蔥圈", "蒜炒香菇四季豆", "蒜苗炒鹹豬肉", "焗烤蕈菇馬鈴薯", "滑蛋蝦仁豆腐煲", "韓式豬五花", "雞翅甘辛煮",
    "筍香紅燒肉", "番茄牛肉湯", "小籠煎包", "蔥爆鮪魚排", "蜂蜜味增炒豬五花", "蒜香雞肉串", "蒜香牛肉串", "蒜香豬肉串",
    "蒜香羊肉串", "蒜香魚肉串", "蒜香蝦肉串", "蒜香蔬菜串"
  ]

  selected_pool = input("選擇籤桶 member 或 dish：")
  selected_pool = selected_pool.lower()

  if selected_pool == "member":
    print("你選擇了 member 籤桶，以下是該籤桶內的任意三支籤：")
    print(random.sample(member_lottery_pool, 3))
    print()
    check_select()
  elif selected_pool == "dish":
    print("你選擇了 dish 籤桶，以下是該籤桶內的任意三支籤：")
    print(random.sample(dish_lottery_pool, 3))
    print()
    check_select()
  else:
    print("輸入無效，請重新輸入。")
    time.sleep( 1 )
    clear_console()
    main()

  picked_lotteries = []  # 存儲抽到的籤

  while True:
    action = input("輸入 'go' 進行抽籤，或 '88' 結束抽籤：")

    if action.lower() == "go":
      clear_console()
      if selected_pool == "member":
        lottery = draw_lottery(member_lottery_pool)
      elif selected_pool == "dish":
        lottery = draw_lottery(dish_lottery_pool)
      else:
        print("尚未選擇籤桶，無法進行抽籤。")
        continue

      if lottery:
        print("搖晃一下籤桶...")
        time.sleep( 0.5 )
        clear_console()
        print(f"你抽到的籤是: {lottery}")
        picked_lotteries.append(lottery)  # 將抽到的籤加入列表
        time.sleep( 2 )
        clear_console()
      else:
        print("搖晃一下籤桶...")
        time.sleep( 0.5 )
        clear_console()
        print("籤桶中已經沒有籤了，抽籤結束。")
        time.sleep( 1 )
        clear_console()
        break
    elif action.lower() == "88":
      clear_console()
      break
    else:
      print("輸入無效，請重新輸入。")
      print()

  while True:
    # 退出程式之前將抽到的籤排序並顯示出來
    picked_lotteries.sort()
    if len(picked_lotteries) > 0:
      print("抽到的籤：")
      index = 0
      for index, lottery in enumerate(picked_lotteries):
        index += 1
        print(f"{index}. {lottery}, ")
      print()
    exit_action = input("輸入 'exit' 退出程式：")
    if exit_action.lower() == 'exit':
      clear_console()
      break
    break

  print('bye')
  time.sleep( 1 )

if __name__ == "__main__":
  main()
