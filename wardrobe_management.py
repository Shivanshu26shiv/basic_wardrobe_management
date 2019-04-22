'''

 i - W a r d r o b e

'''


import random

name=raw_input('Name ? ').capitalize() 
print 'Hello ' + name
print ''
sex=raw_input('Sex (F/M)? ').capitalize() 
while sex not in 'FM' or len(sex)!=1:
    print 'Incorrect value entered, please retry!'
    sex=raw_input('Sex (F/M)? ').capitalize() 

def show_menu():
    
    x = '''
    Chose any of the below option(s):
    ---------------------------------
    
    1. Display wardrobe and exit
    2. Chose from wardrobe
    3. Recommend from wardrobe
    4. Add quantity to wardrobe
    5. Exit
    '''
    print x
    opt=input('>>> ')

    while opt!=12345 and opt>5 :
        print x
        opt=input('>>> ')
        
    wd='wardrobe_'+sex+'.txt'
    if opt==6:
        print 'exiting...'
        exit
    elif opt==1:
        show_wardrobe(sex,wd)
    elif opt==2:    
        chose_wardrobe(sex,wd)
    elif opt==3:
        rec_wardrobe(sex,wd)
    elif opt==4:
        add_wardrobe(sex,wd)
    
    
def show_wardrobe(sex,wd):
    ls_show=[]
    print '\nCurrent item(s) in wardrobe: '
    with open(wd,'r') as f:
        print '\n-----------------\n'
        for cnt,i in enumerate(f.readlines(),1):
            ls_show.append(str(cnt)+'#'+' '+str(i))
            print str(cnt)+'#'+' '+str(i)
        print '-----------------'
        f.close()
    return ls_show    

def chose_wardrobe(sex,wd):
    sw=show_wardrobe(sex,wd)
    item_chosed=input('\nPlease chose item number in wardrobe to pick: ')
    k=0
    while k<len(sw):
        if int(sw[k].replace('\n','')[0]) == item_chosed:
            print 'You have picked: ' + sw[k]
            
            f = open(wd,'r')
            ls=f.readlines()
            f = open(wd,'w+')
            f.close()
            f = open(wd,'r+')
            ls_key=ls[item_chosed-1].split(':')[0]
            ls_value=int(ls[item_chosed-1].split(':')[1].replace('\n','').strip())
            ls_value-=1
            ls[item_chosed-1]=ls_key+': '+str(ls_value)+'\n'
            f.writelines(ls)
            f.close()
            print "Given item's quantity has been reduced by 1."
            
            break
        k+=1
    show_menu()
        
def rec_wardrobe(sex,wd):
    sw=show_wardrobe(sex,wd)
    print '\nSystem recommends: ',
        
    f = open(wd,'r')
    ls=f.readlines()
    r=random.randint(0,len(ls)-1)
    ls_key=ls[r].split(':')[0]
    
    if sex=='F':
        if r==0:
            print ls[r].split(':')[0]
        elif r==1:
            print '{} and {}'.format(ls[r].split(':')[0].replace('\n',''),ls[r+1].split(':')[0])
        elif r==2:
            print '{} and {}'.format(ls[r].split(':')[0].replace('\n',''),ls[r-1].split(':')[0])
            
    elif sex=='M':
        if r==0:
            print '{} and {}'.format(ls[r].split(':')[0].replace('\n',''),ls[r+random.randint(1,2)].split(':')[0])
        elif r==1 or r==2:
            print '{} and {}'.format(ls[r].split(':')[0].replace('\n',''),ls[0].split(':')[0])
    show_menu()

def add_wardrobe(sex,wd):
    sw=show_wardrobe(sex,wd)
    item_chosed=input('\nPlease chose item number in wardrobe to add: ')
    k=0
    while k<len(sw):
        if int(sw[k].replace('\n','')[0]) == item_chosed:
            print 'You have chosed: ' + sw[k]
            
            f = open(wd,'r')
            ls=f.readlines()
            f = open(wd,'w+')
            f.close()
            f = open(wd,'r+')
            ls_key=ls[item_chosed-1].split(':')[0]
            ls_value=int(ls[item_chosed-1].split(':')[1].replace('\n','').strip())
            ls_value+=1
            ls[item_chosed-1]=ls_key+': '+str(ls_value)+'\n'
            f.writelines(ls)
            f.close()
            print "Given item's quantity has been incremented by 1."
            
            break
        k+=1
    show_menu()
    
show_menu()


