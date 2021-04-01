from openie import StanfordOpenIE
from py2neo import Node,Relationship,Graph,NodeMatcher
import pandas as pd
from neo4j import CreateNode,MatchNode,CreateRelationship

class Dateframe(object):
    def __init__(self):
        self.local = 'http://localhost:7474'
        self.username = 'neo4j'
        self.password = '123456'


if __name__ == "__main__" :
    exam = Dateframe()
    graph = Graph(exam.local, username=exam.username, password=exam.password)
    with open('valid.txt', 'r', encoding='utf-8') as r:
        lines = r.read().splitlines()

    spo_list = []

    with StanfordOpenIE() as client:
        for line in lines:
            spo_list.append(client.annotate(line))

    num=54
    for spo in spo_list:
        subjects = []
        objects = []
        relations = []
        num += 1

        for i in spo:
            subjects.append(i['subject'])
            objects.append(i['object'])
            relations.append(i['relation'])
        for i in subjects:
            if 'my' in i:
                att1 = i.split(' ')[0]
                att2 = i.split(' ')[1]
                subjects.append('i')
                objects.append(i)
                relations.append('of')
        data = pd.DataFrame({"subject":subjects,"object":objects,"relation":relations})
        print(subjects)
        print(objects)
        label1 = 'personality'+str(num)
        label2 = 'personality'+str(num)
        for i,j in data.iterrows():
            attr1 = {"name":j.subject}
            CreateNode(graph,label1,attr1)
            attr2 = {"name":j.object}
            CreateNode(graph,label2,attr2)
            m_r_name = j.relation
            reValue = CreateRelationship(graph,label1,attr1,label2,attr2,m_r_name)
            print(reValue)
