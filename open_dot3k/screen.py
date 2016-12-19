#!/usr/bin/python3
import psutil
import dothat.lcd as lcd


class Screen():

    def __init__(self):
        lcd.clear()
        self.content = ""

    def writeTemp(self, temp, ip, time):
        cpu = psutil.cpu_percent()
        self.content = self.__fullLine(str(time) + "     " + str(cpu) + "%")
        self.content += self.__fullLine("il fait " + str(temp) + "*C")
        self.content += self.__fullLine(str(ip))
        lcd.write(self.content)

    def writeMessage(self, message):
        self.content = message
        lcd.write(self.content)

    def clearScreen(self):
        lcd.clear()

    def __fullLine(self, line):
        n = len(line)
        for i in range(16 - n):
            line += " "
        return line
