import requests
from bs4 import BeautifulSoup


def crawler(url : str):
    data = {
        'title' : None,
        'date' : None,
        'location' : None,
        'year' : None,
        'used' : None,
        'kms' : None,
        'import' : None, # nhap khau
        'style' : None,
        'gearBox' : None,
        'fuelEngine' : None,
        'exterior': None,
        'interior': None,
        'seats' : None,
        'doors' : None,
        'motivated' : None,
        'url' : url
    }
    respone = requests.get(url)
    if respone.status_code != 200:
        print(2)
        return data
    soup = BeautifulSoup(respone.text, 'lxml')
    carInfo = soup.find('div', {'id': 'car_detail'})
    if carInfo == None:
        print(1)
        return data
    # 'Xe Toyota Avanza Premio 1.5 MT 2022- 475 Triệu'
    title = carInfo.find('div', {'class': 'title'}).find('h1').text
    data['title'] = title.replace('\n','').replace('\t', '').strip()
    # 'Đăng ngày  9/11/2023. Xem 7 lượt'
    notes = carInfo.find('div', {'class': 'title'}).find('div', {'class': 'notes'}).text
    data['date'] = notes.replace('\n','').replace('\t', '').strip()
    
    detail = carInfo.find('div', {'class': 'box_car_detail'}).find_all('div', {'id': 'mail_parent'})
    # 'Ô Tô Tân Thành  Điện thoại:  0906 906 989   Địa chỉ: 39-41-43 Đường số 7, KDC Conic, Phong Phú, Bình Chánh TP HCM  Website: ototanthanh.bonbanh.com'
    location = carInfo.find('div', {'class': "contact-txt"}).text
    data['location'] = location.replace('\t', '').replace('\n', ' ').strip()

    for element in detail:
        if element.find('div', {'class': 'label'}).text.strip() == 'Năm sản xuất:':
            try:
                data['year'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Tình trạng:':
            try:
                data['used'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}):
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Số Km đã đi:':
            try:
                data['kms'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Xuất xứ:':
            try:
                data['import'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Kiểu dáng:':
            try:
                data['style'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Hộp số:':
            try:
                data['gearBox'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Động cơ:':
            try:
                data['fuelEngine'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Màu ngoại thất:':
            try:
                data['exterior'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Màu nội thất:':
            try:    
                data['interior'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Số chỗ ngồi:':
            try:
                data['seats'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Số cửa:':
            try:
                data['doors'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
        if element.find('div', {'class': 'label'}).text.strip() == 'Dẫn động:':
            try:
                data['motivated'] = element.find('span', {'class': 'inp'}).text.strip()
                continue
            except element.find('span', {'class': 'inp'}) == None:
                continue
    
    return data
    
#print(crawler('https://bonbanh.com/xe-mitsubishi-xpander-premium-1.5-at-2022-5240952'))