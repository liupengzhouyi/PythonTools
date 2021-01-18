from createUML.classModel.FuncModel.FuncModel import FuncModel
from createUML.classModel.MethodModel.MethodModel import MethodModel


class GetInformation:

    s: str

    def getClassName(self, s: str) -> {int, str}:
        value: int
        className: str
        if s[0:6] == 'class ' and s[len(s) - 1] == ':':
            className = s[s.find('class ') + 6:s.index(':')]
            value = 1
        else:
            className = ''
            value = -1
        return {value, className}


    def getClassFunction(self, line: str) -> {int, FuncModel()}:
        value: int
        funcmodel: FuncModel()
        if 'def ' in line and '(' in line and ')' in line:
            value = 1
            funcmodel.funcName = line[line.index('def ') + 4:line.index('(')]
            strMethodList = line[line.find('(self, ') + 7:line.index(')')]
            methodlist: list
            if ',' in strMethodList:
                s = strMethodList.split(', ')
                for item in s:
                    value, m = GetInformation().getClassMethod(item)
                    methodlist.append(m)
            else:
                value, m = GetInformation().getClassMethod(strMethodList[0])
                methodlist.append(m)
            funcmodel.parameterList = methodlist
            if '->' in line:
                funcmodel.returnValueType = line[line.find('-> ') + 3:len(line) - 1]
        else:
            value = -1
        return {value, funcmodel}

    def getClassMethod(self, line: str) -> {int, MethodModel}:
        value: int
        methodModel: MethodModel
        methodModel = MethodModel()
        if ':' in line and line.find(':') != len(line) - 1 and line.find(':', line.find(':') + 1) == -1 and '[' not in line:
            tempList = line.split(':')
            methodModel.name = tempList[0].strip()
            methodModel.type = tempList[1].strip()
            value = 1
        else:
            value = -1
        return {value, methodModel}
