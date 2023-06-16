#!/usr/bin/env python
# coding: utf-8

# In[2]:


gp = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Denis"),('Houda','Bob'),('Alice','Denis')]


# In[ ]:


Question1:


# In[3]:


def create_network(gp):
    """ 
      Cette fonction retourne un dictionnaire dont les clés 
      sont les prénoms des membres du réseau et les valeurs 
      le tableau de leurs amis.

    """
    d={}
    i=0
    while i<len(gp):
        if gp[i][0] not in d:
            d[gp[i][0]]=list()
            d[gp[i][0]].append(gp[i][1])
        else:
            d[gp[i][0]].append(gp[i][1])
        if gp[i][1] not in d:
            d[gp[i][1]]=list()
            d[gp[i][1]].append(gp[i][0])
        else:
            d[gp[i][1]].append(gp[i][0])
        i+=1
    return d


# In[4]:


def Test_create_network():
    assert create_network(gp) == {'Alice': ['Bob', 'Charlie', 'Denis'],
                                  'Bob': ['Alice', 'Denis', 'Houda'], 'Charlie': ['Alice'],
                                  'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert create_network ([]) == {}
    print('ok')
Test_create_network()


# In[ ]:


Question2:


# In[ ]:


Théoriquement:
la complexité de la première fonction est quadratique et la deuxième est linéaire. 


# In[ ]:


Question3:


# In[5]:


def get_people(d):
    """ 
      Cette fonction retourne la liste
      des personnes de ce réseau dans un tableau.

    """
    Lp=list(d.keys())
    return Lp


# In[7]:


def test_get_people():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert get_people(d) == ['Alice' , 'Bob' , 'Charlie', 'Denis' ,'Houda']
    assert get_people({'Charlie':[]}) == ['Charlie']
    print('ok')
test_get_people()    


# In[ ]:


Question4:


# In[8]:


def are_friends(d,p1,p2):
    """ 
      Cette fonction retourne True si les deux
      personnes sont amies, et False sinon.

    """

    if p2 in d[p1]:
        return True
    else:
        return False


# In[11]:


def test_are_friends():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert are_friends(d,'Houda','Bob') == True
    assert are_friends(d,'Alice','Charlie') == True
    assert are_friends(d,'Houda','Denis') == False
    print("ok")
test_are_friends()    


# In[ ]:


Question5:


# In[12]:


def all_his_friends(d,p,lp):
    """ 
      Cette fonction prend en paramètre
      réseau, une personne et un groupe de
      personnes et retourne True si la 
      personne est amie avec toutes les personnes
      du groupe, et False sinon.

    """
    i=0
    while i<len(lp):
        if not are_friends(d,p,lp[i]):
            return False
        i+=1
    return True
        


# In[14]:


def Test_all_his_friends():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert all_his_friends(d,'Charlie',['Bob','Houda']) == False
    assert all_his_friends(d,'Bob',['Alice','Houda']) == True
    print('ok')
Test_all_his_friends()


# In[ ]:


Question6:


# In[15]:


def is_a_community(d,gp):
    """ 
      Cette fonction prend en paramètre 
      un dictionnaire modélisant le réseau 
      et un groupe de personnes (tableau de personnes) 
      et retourne True si ce groupe est une communauté,
      et False sinon.

    """
    
    i=0
    while i<len(gp):
        L=[]
        j=0
        while j<len(gp):
            if j!=i:
                L.append(gp[j])
            j+=1
        #print(L)
        if not all_his_friends(d,gp[i],L):
            return False
            
        else:
            i+=1
    return True  
        


# In[17]:


def Test_is_a_community():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert is_a_community(d,['Alice','Bob','Denis']) == True
    assert is_a_community(d,['Alice','Bob','Houda']) == False
    print('ok')
Test_is_a_community()


# In[ ]:


Question7:


# In[18]:


def find_community(d,gp):
    """ 
      Cette fonction prend en paramètre un réseau
      et un groupe de personnes et retourne 
      une communauté 

    """
    cm=[]
    for p in range(len(gp)):
        i=0
        while i<len(gp):
            bol=1
            if i!=p:
                if  not is_a_community(d,[gp[p],gp[i]]):
                    bol=0
            i+=1
        if bol==1:
            cm.append(gp[p])
    return cm               


# In[21]:


def Test_find_community():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert find_community(d,['Houda','Denis','Bob','Alice']) == ['Denis', 'Bob', 'Alice']
    assert find_community(d,['Alice','Bob','Charlie']) == ['Alice', 'Charlie']
    print('ok')
Test_find_community()


# In[ ]:


Question8:


# In[22]:


def order_by_decreasing_popularity(d,gp):
    """ 
      Cette fonction prend en paramètre
      un réseau et un groupe de personnes
      et trie le groupe de personnes selon
      la popularité (nombre d'amis) décroissante.

    """
    dgp={}
    gpt=[]
    i=0
    while i<len(gp):
        dgp[gp[i]]=len(d[gp[i]])
        i+=1
    for k,v in sorted(dgp.items(),key=lambda x: x[1]):
        gpt.append(k)
    return gpt[::-1]
      


# In[23]:


def Test_order_by_decreasing_popularity():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert order_by_decreasing_popularity(d,['Bob','Alice','Charlie']) == ['Alice', 'Bob', 'Charlie']
    assert order_by_decreasing_popularity(d,['Denis','Alice','Houda','Charlie']) == ['Alice', 'Denis', 'Charlie', 'Houda']
    print('ok')
Test_order_by_decreasing_popularity()


# In[ ]:


Question9:


# In[24]:


def find_community_by_decreasing_popularity(d):
    """
      Cette fonction prend en paramètre un réseau.
      La fonction doit trier l'ensemble des personnes 
      du réseau selon l'ordre décroissant de popularité 
      puis retourner la communauté trouvée en appliquant 
      l'heuristique de construction de communauté maximale
      utilisée dans la fonction précédente.

    """
    pd=get_people(d)
    pdo=order_by_decreasing_popularity(d,pd)
    pdc=find_community(d,pdo)
    return pdc
    


# In[26]:


def Test_find_community_by_decreasing_popularity():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert find_community_by_decreasing_popularity(d) == ['Alice','Charlie']
    assert find_community_by_decreasing_popularity({'Nour':['Lina','David'],'Lina':['Moha']}) == ['Lina']
    print('ok')
Test_find_community_by_decreasing_popularity()


# In[ ]:


Question10:


# In[37]:


def find_community_from_person(d,p):
    """
      prenant en paramètre un réseau et une personne,
      et retournant une communauté maximale contenant 
      cette personne selon l'heuristique décrite ci-dessus.
    
    """
    com=[p]
    com+=find_community(d,(order_by_decreasing_popularity(d, d[p])))
    return com


# In[55]:


def Test_find_community_from_person():
    assert find_community_from_person(d,'Bob')==['Bob', 'Houda']
    assert find_community_from_person({'Nour':['Lina'],'Lina':['Nour','Alice'],'Alice':['Nour']},'Nour')==['Nour', 'Lina']
    print('ok')
Test_find_community_from_person()


# In[ ]:


Question11:


# In[ ]:


la complexité de la première fonction est quadratique et la deuxième est linéaire.


# In[ ]:


Question12:


# In[41]:


def find_max_community(d):
    """
      Cette fonction prend en paramètre
      un réseau et applique l'heuristique 
      de recherche de communauté maximale 
      donnée par find_community_from_person 
      pour toutes les personnes du réseau. 
      La fonction doit retourner la plus grande 
      communauté trouvée.
    
    """
    
    max_com=[]
    for p in d:
        person_com=find_community_from_person(d,p)
        if len(max_com)<len(person_com):
            max_com=person_com
    return max_com
    


# In[50]:


def Test_find_max_community():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'Houda'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'Houda': ['Bob']}
    assert find_max_community(d)==['Denis', 'Alice', 'Bob']
    assert find_max_community({'Nour':['Lina'],'Lina':['Nour','Alice'],'Alice':['Nour']})==['Nour', 'Lina']
    print('ok')
Test_find_max_community()

