from selenium.webdriver.common.by import By


def get_table_fields(element, selectors):
    return {
        "id": element.find_element(By.CLASS_NAME, "id").get_attribute("innerHTML"),
        **{
            name: element.find_element(By.CSS_SELECTOR, selector)
            for name, selector in selectors.items()
        },
    }
