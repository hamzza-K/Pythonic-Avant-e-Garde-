import os
import random
try:
    os.chdir('path to your directory')
except Exception as e:
    os.mkdir('if the directory is not found, create one')
print(os.getcwd()) #make sure you get the right path

names = ['this sucks', 'lmao', 'omaewashinderu','meh']
my_list = ['wahahhah', 'what are you looking at', 'i am watching you']

class Mi_hacker(object):
    
    def changing_files(self):
        for f in os.listdir():
            f_name, f_ext = os.path.splitext(f)
            nums, names = f_name.split('-')
            nums = nums.zfill(2)
            # names = names.strip()[:-2]
            new_name = '{}-{}{}'.format(names, nums, f_ext)
            os.rename(f, new_name)
            # print(new_name)
    @staticmethod
    def writing_new_files():
        for i in range(10):
            with open('{}-{}.txt'.format(i, random.choice(names)), 'w') as f:
                f.write(random.choice(my_list))

    def deleting_new_files(self):
        new = []
        for f in os.listdir():
            fname, fext = os.path.splitext(f)
            if fname.endswith('eh'):
                new.append(f)

        print(new)
        for f in new:
            if os.path.isfile(f):
                os.remove(f)
    @staticmethod
    def deleting_all_files():
        for f in os.listdir():
            os.remove(f)

if os.listdir():
    pass
else:
    Mi_hacker.writing_new_files()



migood = Mi_hacker()


# migood.writing_new_files()
# migood.changing_files()
migood.deleting_all_files()
