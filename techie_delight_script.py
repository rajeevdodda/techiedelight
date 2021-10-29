from selenium import webdriver
import xlsxwriter
import os
import time

driver = webdriver.Chrome(r"C:\Users\rdodda\chromedriver.exe")

workbook = xlsxwriter.Workbook(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "techidelight.xlsx"))


# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write("A1", "S No")
worksheet.write("B1", "Problem")
worksheet.write("C1", "Link")
worksheet.write("D1", "Level")
worksheet.write("E1", "Tags")

page = 1
row = 1

while page < 63:
    url = f"https://www.techiedelight.com/page/{page}/"
    time.sleep(2)
    driver.get(url)

    articles = driver.find_elements_by_tag_name("article")

    for article in articles:
        html_id = article.get_attribute("id")

        problem_xpath = f'//*[@id="{html_id}"]/div/header/h2/a'
        problem = driver.find_element_by_xpath(problem_xpath).text
        problem_link = driver.find_element_by_xpath(
            problem_xpath).get_attribute("href")
        try:
            difficulty_xpath = f'//*[@id="{html_id}"]/div/header/div/a/span'
            difficulty = driver.find_element_by_xpath(difficulty_xpath).text
        except Exception as e:
            difficulty = "NA"
        tags_xpath = f'//*[@id="{html_id}"]/div/header/div/span'
        tags = driver.find_element_by_xpath(tags_xpath).text
        worksheet.write(row, 0, row)
        worksheet.write(row, 1, problem)
        worksheet.write(row, 2, problem_link)
        worksheet.write(row, 3, difficulty)
        worksheet.write(row, 4, tags)
        row += 1

    page += 1

workbook.close()
