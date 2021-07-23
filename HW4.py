##EX1
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    #print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value

        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls

### class MyDate
# The Point class is created through a make_MyDate_class function,
# which has structure similar to a class statement in Python,
# but concludes with a call to make_class.
def make_mydate_class():

    def __init__(self, d=1, m=1,y=2000):
        self['set']('day', d)
        self['set']('month', m)
        self['set']('year', y)

    def __str__(self):
        string = '%d.%d.%d' % (self['get']('day'), self['get']('month'), self['get']('year'))
        return string

    def __repr__(self):
        repDay = repr(self['get']('day'))
        repMonth = repr(self['get']('month'))
        repYear = repr(self['get']('year'))
        return 'Date({0},{1},{2})'.format(repDay, repMonth, repYear)

    def get_year(self):
        return self['get']('year')
    def get_month(self):
        return self['get']('month')
    def get_day(self):
        return self['get']('day')
    def set_year(self,y):
        if y in range(1900,2100):
            self['set']('year', y)
        else:
            self['set']('year', 2000)
    def set_month(self,m):
        if y in range(1,12):
            self['set']('month', m)
        else:
            self['set']('year', 1)
    def set_day(self,d):
        if y in range(1,30):
            self['set']('day', d)
        else:
            self['set']('day', 1)
    return make_class(locals())

### class Person
# The Point class is created through a make_Person_class function,
# which has structure similar to a class statement in Python,
# but concludes with a call to make_class.
def make_Person_class():

    def __init__(self, f_name, l_name,dob,id):
        self['set']('f_name', f_name)
        self['set']('l_name', l_name)
        self['set']('dob', dob)
        self['set']('id', id)

    def __str__(self):
        return "Name:{} {} \niD:{} \nDOB:{}".format(self['get']('f_name'), self['get']('l_name'), self['get']('id'), self['get']('dob')['get']('__str__')())

    def __repr__(self):
        return "Person:{}{}{}{}".format(self['get']('f_name'), self['get']('l_name'), self['get']('id'), self['get']('dob')['get']('__str__')())

    def get_f_name(self):
        return self['get']('f_name')
    def get_l_name(self):
        return self['get']('l_name')
    def get_dob(self):
        return self['get']('dob')
    def get_id(self):
        return self['get']('id')
    def set_f_name(self,name):
        self['set']('f_name', name)
    def set_l_name(self,name):
        self['set']('l_name', name)
    def set_dob(self,dob):
        self['set']('dob', dob)
    def set_id(self,id):
        if id>0: self['set']('id', id)
        else : self['set']('id', 'defualt')
    return make_class(locals())

## take from make_Person_class
def make_Student_class():
    def __init__(self, f_name, l_name, dob, id, Learning, Avg, Seniority):
        make_Person_class()['get']('__init__')(self, f_name, l_name, dob, id)
        self['set']('Learning', Learning)
        self['set']('Avg', Avg)
        self['set']('Seniority', Seniority)

    def __str__(self):
        return make_Person_class()['get']('__str__')(self) + "\nLearning:{} \nAvg:{} \nSeniority:{}".format(
            self['get']('Learning'), self['get']('Avg'), self['get']('Seniority'))
    def __repr__(self):
        return "Student:{},{},{},{},{},{},{}".format(repr(self['get']('f_name')),
                    (self['get']('l_name')),
                    (self['get']('dob')['get']('__repr__')()),
                    (self['get']('id')),
                    (self['get']('Learning')),
                    (self['get']('Avg')),
                    (self['get']('Seniority')))


    def get_learning(self):
        return self['get']('Learning')
    def get_avg(self):
        return self['get']('Avg')
    def get_seniority(self):
        return self['get']('Seniority')
    def set_learning(self,Learning):
        self['set']('Learning',Learning)
    def set_avg(self,Avg):
        self['set']('Avg',Avg)
    def set_seniority(self,Seniority):
        self['set']('Seniority',Seniority)
    return make_class(locals())
##take from make_Person
def make_Faculty_class():
    def __init__(self, f_name, l_name, dob, id, Teaching, Salary, Seniority):
        make_Person_class()['get']('__init__')(self, f_name, l_name, dob, id)
        self['set']('Teaching', Teaching)
        self['set']('Salary', Salary)
        self['set']('Seniority', Seniority)

    def __str__(self):
        return make_Person_class()['get']('__str__')(self) + "\nTeaching:{} \nSalary:{} \nSeniority:{}".format(
            self['get']('Teaching'), self['get']('Salary'), self['get']('Seniority'))

    def __repr__(self):
        return "Faculty:({},{},{},{},{},{},{})"\
            .format((self['get']('f_name')),
                    (self['get']('l_name')),
                    (self['get']('dob')['get']('__repr__')()),
                    (self['get']('id')),
                    (self['get']('Teaching')),
                    (self['get']('Salary')),
                    (self['get']('Seniority')))

    def get_teaching(self):
        return self['get']('Teaching')
    def get_salary(self):
        return self['get']('Salary')
    def get_seniority(self):
        return self['get']('Seniority')
    def set_teaching(self,Teaching):
        self['set']('Learning',Teaching)
    def set_salary(self,Salary):
        self['set']('Salary',Salary)
    def set_seniority(self,Seniority):
        self['set']('Seniority',Seniority)

    return make_class(locals())
##take from make_Student_class and make_Faculty_class
def make_TA_class():
    def __init__(self, f_name, l_name, dob, id,Learning,Avg,Seniority, Teaching, Salary,):
        make_Student_class()['get']('__init__')(self, f_name, l_name, dob, id,Learning,Avg,Seniority)
        make_Faculty_class()['get']('__init__')(self, f_name, l_name, dob, id, Teaching, Salary, Seniority)
    def __str__(self):
        return make_Faculty_class()['get']('__str__')(self) + '\n' + make_Student_class()['get']('__str__')(self)
    def __repr__(self):
        return 'TA({},{},{},{},{},{},{},{},{},{})'\
            .format((self['get']('name')),
                    (self['get']('f_name')),
                    (self['get']('dob')['get']('__repr__')()),
                    (self['get']('id')),
                    (self['get']('Teaching')),
                    (self['get']('Salary')),
                    (self['get']('Seniority')),
                    (self['get']('Learning')),
                    (self['get']('Avg')),
                    (self['get']('Seniority')))
    return make_class(locals())

def program():
    d = date['new'](18, 1, 2021)
    print("********person********")
    p = person['new']('alex', 'serdukov', d, '323274787')
    print(p['get']('__str__')())
    print("********student with person*****:")
    s = student['new']('alex', 'serdukov', d, '323274787', 'Software Engineering',98.0,3)
    print(s['get']('__str__')())
    print("******faculty***********")
    f=faculty['new']('alex','serdukov',d,323274787,'Software Engineering',1000.0,3)
    print(f['get']('__str__')())

print('********************************************EX1***********************************************')
date=make_mydate_class()
person=make_Person_class()
student=make_Student_class()
faculty=make_Faculty_class()
ta=make_TA_class()
program()


##EX3
class Shekel(object):
    def __init__(self,money):
        self.Shekel=money
    def __str__(self):
        return '{}'.format(self.Shekel)
    def __repr__(self):
        return Shekel({}).__format__(self.Shekel)

class Dollar(object):

    def __init__(self,money):
        self.Dollar=money
    def __str__(self):
        return '{}'.format(self.Dollar)
    def __repr__(self):
        return Dollar({}).__format__(self.Dollar)
    def convert_to_nis(self):
        return self.Dollar*3.2
    def convert_to_euro(self):
        return self.Dollar*1.2

class Euro(object):
    def __init__(self,money):
        self.Euro=money
    def __str__(self):
        return '{}'.format(self.Euro)
    def __repr__(self):
        return Euro({}).__format__(self.Euro)
    def convert(self):
        return self.Euro*3.7

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {Shekel: 'shekel', Dollar: 'dolar', Euro: 'euro'}

def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)



def add_shekel_with_shekel(a,b):
    return a.Shekel+b.Shekel

def add_shekel_with_dolar(a,b):
    return a.Shekel+b.convert_to_nis()

def add_shekel_with_euro(a,b):
    return a.Shekel+b.convert()

def add_dolar_with_shekel(a,b):
    return a.convert_to_nis()+b.Shekel

def add_dolar_with_dolar(a,b):
    return a.Dollar+b.Dollar

def add_dolar_with_euro(a,b):
    return a.convert_to_euro()+b.Euro

def add_euro_with_shekel(a,b):
    return a.convert()+b.Shekel

def add_euro_with_dolar(a,b):
    return a.Euro+b.convert_to_euro()

def add_euro_with_euro(a,b):
    return a.Euro+b.Euro


def mul_shekel_with_shekel(a,b):
    return a.Shekel*b.Shekel

def mul_shekel_with_dolar(a,b):
    return a.Shekel*b.convert_to_nis()

def mul_shekel_with_euro(a,b):
    return a.Shekel*b.convert()

def mul_dolar_with_shekel(a,b):
    return a.convert_to_nis()*b.Shekel

def mul_dolar_with_dolar(a,b):
    return a.Dollar*b.Dollar

def mul_dolar_with_euro(a,b):
    return a.convert_to_euro()*b.Euro

def mul_euro_with_shekel(a,b):
    return a.convert()*b.Shekel

def mul_euro_with_dolar(a,b):
    return a.Euro*b.convert_to_euro()

def mul_euro_with_euro(a,b):
    return a.Euro*b.Euro

apply.implementations = {
            ('add', ('shekel', 'shekel')): add_shekel_with_shekel,
			('add', ('shekel', 'dolar')): add_shekel_with_dolar,
			('add', ('shekel', 'euro')): add_shekel_with_euro,
			('add', ('dolar', 'shekel')): add_dolar_with_shekel,
            ('add', ('dolar', 'dolar')): add_dolar_with_dolar,
            ('add', ('dolar', 'euro')): add_dolar_with_euro,
            ('add', ('euro', 'shekel')): add_euro_with_shekel,
            ('add', ('euro', 'dolar')): add_euro_with_dolar,
            ('add', ('euro', 'euro')): add_euro_with_euro,
            ('mul', ('shekel', 'shekel')): mul_shekel_with_shekel,
			('mul', ('shekel', 'dolar')): mul_shekel_with_dolar,
			('mul', ('shekel', 'euro')): mul_shekel_with_euro,
			('mul', ('dolar', 'shekel')): mul_dolar_with_shekel,
            ('mul', ('dolar', 'dolar')): mul_dolar_with_dolar,
            ('mul', ('dolar', 'euro')): mul_dolar_with_euro,
            ('mul', ('euro', 'shekel')): mul_euro_with_shekel,
            ('mul', ('euro', 'dolar')): mul_euro_with_dolar,
            ('mul', ('euro', 'euro')): mul_euro_with_euro }


x=Shekel(100)
y=Dollar(50)
z=Euro(20)
print('********************************************EX3***********************************************')

print('add Shekel with Shekel:',apply('add', x, x))
print('add Shekel with Dollar:',apply('add', x, y))
print('add Shekel with Euro:',apply('add', x, z))

print('add Dollar with Shekel:',apply('add', y, x))
print('add Dollar with Dollar:',apply('add', y, y))
print('add Dollar with Euro:',apply('add', y, z))

print('add Euro with shekel:',apply('add', z, x))
print('add Euro with Dollar:',apply('add', z, y))
print('add Euro with Euro:',apply('add', z, z))

print('mul Shekel with Shekel:',apply('mul', x, x))
print('mul Shekel with Dollar:',apply('mul', x, y))
print('mul Shekel with Euro:',apply('mul', x, z))

print('mul Dollar with Shekel:',apply('mul', y, x))
print('mul Dollar with Dollar:',apply('mul', y, y))
print('mul Dollar with Euro:',apply('mul', y, z))

print('mul Euro with shekel:',apply('mul', z, x))
print('mul Euro with Dollar:',apply('mul', z, y))
print('mul Euro with Euro:',apply('mul', z, z))



