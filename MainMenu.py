# 這個函式是用於創建主選單並處理用戶選擇的程式
def main_menu():
    # 顯示主選單標題
    print("主選單:")
    # 顯示選項一
    print("1. 選項一")
    # 顯示選項二
    print("2. 選項二")
				
    # 要求用戶輸入選擇
    choice = input("請輸入選擇 (1/2): ")

    # 如果選擇為1，顯示相應的訊息
    if choice == '1':
        print("你選擇了選項一。")
    # 如果選擇為2，顯示相應的訊息
    elif choice == '2':
        print("你選擇了選項二。")

# 程式的主入口點，確保只在直接執行這個程式時執行以下代碼
if __name__ == "__main__":
    # 啟動主選單函數
    main_menu()
