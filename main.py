from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from PIL import Image

if __name__ == '__main__':
    im = Image.open('photo_2022-10-05_15-08-25.jpg')

    calculate_salary()
    get_employees()
    print(datetime.today())
    im.show()
    print(im.format, im.size, im.mode)

