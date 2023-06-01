names = ['tarteel','asmaa','ahmed']
names.insert(0,'sabrin')
print(names)
names.remove('ahmed')
print(names)
names.insert(3,'hamda')
print(names)
names.remove('asmaa')
print(names)
friends = ['adel','ahmed']              #2
employees = ['samah','amjed']
school = ['ali','basma']
my_list = []
my_list.extend(friends)
my_list.extend(employees)
my_list.extend(school)
print(my_list)
dict1 ={1:10,2:20}              #3
dict2 ={3:30,4:40}
dict3 ={5:50,6:60}
dict4 ={}
for d in (dict1,dict2,dict3):    dict4.update(d)
print(dict4)
my_num = dict()
for i in range(1,16):
    my_num[i] = i **2
print(my_num)
d1 = {'a':100,'d':200,'c':300}
d2 = {'a':150,'d':200,'c':400}
d3 = {}
for i in d1.keys():
    if i in d2.keys():
        d1[i] = d1[i] + d2[i]
print(d3)
keys = ['ten','twenty','thirty']                #6
values =[10,20,30]
my_dict = {}
for i in range (len(keys)):    my_dict[keys[i]] = values[i]
print(my_dict)
sampleDict = {                      #7
    'class':{        'student':{
            'name':'mike',            'marks':{
                'physics':70 ,                'history':80
            }

        }

    }

}
print(sampleDict.get('class').get('student').get('marks').get('history'))
my_dict1 = {1:'alaa',5:'hadeel',7:'hanin',13:'malak'}
for k,v in my_dict1.items():
    if k <10:
        print(v,end='->')

