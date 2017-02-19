#!/usr/bin/python3
import psutil
import dothat.lcd as lcd


class Screen():

    def __init__(self):
        lcd.clear()
        self.content = ""

    def write_temp(self, probe, temp, ip, time):
        cpu = psutil.cpu_percent()
        if len(str(probe)) > 7:
            probe = str(probe)[:6]
        self.content = self.__full_line(str(time) + "     " + str(cpu) + "%")
        self.content += self.__full_line(str(probe) + " : " + str(temp) + "*C")
        self.content += self.__full_line(str(ip))
        lcd.write(self.content)

    def write_humidity(self, probe, hum, ip, time):
        cpu = psutil.cpu_percent()
        if len(str(probe)) > 7:
            probe = str(probe)[:6]
        self.content = self.__full_line(str(time) + "     " + str(cpu) + "%")
        self.content += self.__full_line(str(probe) + " : " + str(hum) + "%")
        self.content += self.__full_line(str(ip))
        lcd.write(self.content)


    def write_message(self, message):
        self.content = message
        lcd.write(self.content)

    def clear_screen(self):
        lcd.clear()

    def __full_line(self, line):
        n = len(line)
        for i in range(16 - n):
            line += " "
        return line
