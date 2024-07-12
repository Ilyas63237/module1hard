#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gread = {'Jhonny': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Steve': [4, 5, 5, 2], 'Khendrik': [4, 4, 3], 'Aaron': [5, 5, 5, 4, 5]}
J = (sum(gread['Jhonny'])/len(gread['Jhonny']))
print(gread)
# Так как, в России школьников оценивают целочисленными оценками, было добавлено округление
# Наверняка есть оператор округления, просто решил заморочится и потренироваться)
if (J>=sum(gread['Jhonny'])//len(gread['Jhonny'])+0.5): J=(sum(gread['Jhonny'])//len(gread['Jhonny'])+1)
else: J = (sum(gread['Jhonny'])//len(gread['Jhonny']))
B = (sum(gread['Bilbo'])/len(gread['Bilbo']))
if (B>=sum(gread['Bilbo'])//len(gread['Bilbo'])+0.5): B=(sum(gread['Bilbo'])//len(gread['Bilbo'])+1)
else: B = (sum(gread['Bilbo'])//len(gread['Bilbo']))
S = (sum(gread['Steve'])/len(gread['Steve']))
if (S>=sum(gread['Steve'])//len(gread['Steve'])+0.5): S=(sum(gread['Steve'])//len(gread['Steve'])+1)
else: S = (sum(gread['Steve'])//len(gread['Steve']))
K = (sum(gread['Khendrik'])/len(gread['Khendrik']))
if (K>=sum(gread['Khendrik'])//len(gread['Khendrik'])+0.5): K=(sum(gread['Khendrik'])//len(gread['Khendrik'])+1)
else: K = (sum(gread['Khendrik'])//len(gread['Khendrik']))
A = (sum(gread['Aaron'])/len(gread['Aaron']))
if (A>=sum(gread['Aaron'])//len(gread['Aaron'])+0.5): A=(sum(gread['Aaron'])//len(gread['Aaron'])+1)
else: A = (sum(gread['Aaron'])//len(gread['Aaron']))
print('Jhonny ',J,', ','Bilbo ',B,',','Steve ',S,', ','Khendrik',K,', ','Aaron',A)
