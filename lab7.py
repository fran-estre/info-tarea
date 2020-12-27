class Element:

    def __init__(self, name=None, value=None, isItemList=False):
        self.elements = []
        self.isItemList = isItemList
        self.name = name
        self.value = value
        self.width = 2

    def addElement(self, element):
        self.elements.append(element)

    def toString(self, indent):
        result = ""
        # la cabecera del elemento
        if not self.isItemList:
            result = " " * indent * self.width + self.name + ":"
            if self.value != None:
                result += " " + self.value
            result += "\n"
        # los elementos del elemento actual
        if len(self.elements) > 0:
            newIndent = indent
            if not self.isItemList:
                newIndent +=1
            for x in self.elements:
                result += x.toString(newIndent)
            if self.isItemList:
                result = result[0:newIndent*self.width-2] + \
                    "-" + result[newIndent*self.width-1:]
        return result


root = Element(name="respons")
root.addElement(Element("week_day", "Вторник"))
disciplines = Element(name="disciplines")

item = Element(isItemList=True)
item.addElement(Element("name", "Программирование(ЛЕК)"))
item.addElement(Element("time", "11:40-13:10"))
item.addElement(Element("number_of_auditorium","302"))
item.addElement(Element("address","Кронверкский пр., д.49, лит.А"))
item.addElement(Element("lecturer","Письмак Алексей Евгеньевич"))
item.addElement(Element("format","Очно - дистанционный"))
disciplines.addElement(item)

item2 = Element(isItemList=True)
item2.addElement(Element("name", "Информатика(ЛАБ)"))
item2.addElement(Element("time", "13:30-15:00"))
item2.addElement(Element("number_of_auditorium","306"))
item2.addElement(Element("address","Кронверкский пр., д.49, лит.А"))
item2.addElement(Element("lecturer","Болдырева Елена Александровна"))
item2.addElement(Element("format","Очно - дистанционный"))

disciplines.addElement(item2)

root.addElement(disciplines)
print(root.toString(0))
