

browser.get(url)
    time.sleep(5)

    items = browser.find_elements(By.XPATH, '//div[@data-marker="item"]') #находим все элементы с карточками товара
    for i in range(5):
        items[i].click() #кликаем по карточке номер которой вышел в цикле
        browser.switch_to.window(browser.window_handles[-1]) #Переключаемся на последнюю открытую вкладку(-1 = последняя)
        print(browser.current_url) #выводим ссылку на влкадку
        #собираем и выводим информацию с открытой вкладки
        title = browser.find_element(By.CLASS_NAME, 'title-info-title-text')
        print(title.text)
        seller_geo = browser.find_element(By.CLASS_NAME, "style-item-address__string-wt61A")
        print(f'Локация: {seller_geo.text}')
        print()
        browser.close() #закрываем открытую вкладку

        browser.switch_to.window(browser.window_handles[0]) #переключаемся обратно на начальную вкладку
        time.sleep(2)