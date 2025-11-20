import shutil

def ignore_files(directory,files):
    return [f for f in files if f =='firsttext']

# shutil.copytree('rybau', 'rybau3', ignore=ignore_files) kopiuje dir z plikami ale mozna ignorowac
# rozne case np tutaj mamy cos takiego mozna zrobic split lub shutilignorepatterns
# lub endswith, startswith, special pattern in also works just string operations

# shutil.copy('firsttext','destination') kopiuje tylko plik

# MOVING FILES
# shutil.move('firsttext','rybau2/firsttext')
# shutil.rmtree('rybau2') this removing dir

total, used, free = shutil.disk_usage('/')
# print(total,used,free)

shutil.copystat('fare.txt','place.txt') # meta dane beda kopiowane bez kopiowania
# shutil.chown('fare.txt',user='root') changes user name