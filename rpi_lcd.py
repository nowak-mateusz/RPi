from hd44780 import HD44780
from time import sleep, strftime
from datetime import datetime


if __name__ == '__main__':
    lcd = HD44780()
    lcd.message("  MalinowePi.pl\n  @MalinowePi")
    sleep(2)
    while 1:
        lcd.clear()
        lcd.message(datetime.now().strftime('%b %d %H:%M:%S\n'))
        sleep(1)
