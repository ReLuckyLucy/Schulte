from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def setup_driver():
    # 设置Chrome选项
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    return webdriver.Chrome(options=options)

def find_and_click_cells(driver):
    try:
        # 等待表格加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cell"))
        )
        
        # 获取所有单元格
        cells = driver.find_elements(By.CLASS_NAME, "cell")
        
        # 创建一个字典来存储数字和对应的元素
        cell_dict = {}
        for cell in cells:
            try:
                number = int(cell.text)
                cell_dict[number] = cell
            except ValueError:
                continue
        
        # 按顺序点击数字
        for i in range(1, len(cell_dict) + 1):
            if i in cell_dict:
                cell_dict[i].click()
                time.sleep(0.1)  # 短暂延迟以确保点击被注册
                
    except TimeoutException:
        print("页面加载超时")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def main():
    driver = setup_driver()
    try:
        # 打开舒尔特表格网页
        driver.get("http://schulte.luckylucy.live/")
        
        # 等待页面加载
        time.sleep(2)
        
        # 开始挑战
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Test')]"))
        )
        start_button.click()
        
        # 执行点击操作
        find_and_click_cells(driver)
        
        # 等待一段时间以查看结果
        time.sleep(5)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main() 