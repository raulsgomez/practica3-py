class Database:
    def __init__(self): 
        self.dic=dict()
    def __del__(self):
        del self
        print("Bye")
    def insert(self, col, data):
        s=self.dic
        if col not in s:
            if isinstance(data,int):
                s[col]=list()
                s[col].append(data)
            elif isinstance(data,str):
                s[col]=[]
                s[col].append(data)
            elif isinstance(data,tuple):
                s[col]=list()
                s[col].append(data)
            else: 
                print("Nombralo bien")
        else  :
            l=s[col]
            if (type(l[0])==type(data) ):
                s[col].append(data)
            else: 
                print("Error, no coincide el tipo")
    def remove(self, col, data):
        s=self.dic
        if data in s[col]:
            s[col].remove(data) 
            print("Ok") 
        else:
            print("Error, dato no está en la colección")     
    def search(self,query):
        s=self.dic
        l=query.split()
        col=l[1]
        if(len(l)==2):
           return(s[col]) 
        elif(len(l)==3):
            if(l[2]=="ASC"):
                return s[col].sort()
            else:
                return s[col].sort(reverse=True)
        elif(query.count("WHERE")==1):
            t=list()
            valor=int(l[4])
            if("<="in query):
                if("ASC" in query ):
                    for x in s[col]:
                        if x<=valor:
                            t.append(x)
                    return sorted(t)
                elif("DESC" in query):
                    for x in s[col]:
                        if x<=valor:
                            t.append(x)
                    return sorted(t, reverse=True)
                else:
                    for x in s[col]:
                        if x<=valor:
                            t.append(x)
                    return t
            elif(">="in query):
                if("ASC" in query ):
                    for x in s[col]:
                        if x>=valor:
                            t.append(x)
                    return sorted(t)
                elif("DESC" in query):
                    for x in s[col]:
                        if x>=valor:
                            t.append(x)
                    return sorted(t, reverse=True)
                else:
                    for x in s[col]:
                        if x>=valor:
                            t.append(x)
                    return t
            elif("<"in query):
                if("ASC" in query ):
                    for x in s[col]:
                        if x<valor:
                            t.append(x)
                    return sorted(t)
                elif("DESC" in query):
                    for x in s[col]:
                        if x<valor:
                            t.append(x)
                    return sorted(t, reverse=True)
                else:
                    for x in s[col]:
                        if x<valor:
                            t.append(x)
                    return t
            elif(">"in query):
                if("ASC" in query ):
                    for x in s[col]:
                        if x>valor:
                            t.append(x)
                    return sorted(t)
                elif("DESC" in query):
                    for x in s[col]:
                        if x>valor:
                            t.append(x)
                    return sorted(t, reverse=True)
                else:
                    for x in s[col]:
                        if x>valor:
                            t.append(x)
                    return t  
            else:
                if("ASC" in query ):
                    for x in s[col]:
                        if x==valor:
                            t.append(x)
                    return sorted(t)
                elif("DESC" in query):
                    for x in s[col]:
                        if x==valor:
                            t.append(x)
                    return sorted(t, reverse=True)
                else:
                    for x in s[col]:
                        if x==valor:
                            t.append(x)
                    return t
        else:
            return "Se equivocó en algo wey"


       




        
        
       