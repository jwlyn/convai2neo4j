from py2neo import Node,Relationship,Graph,NodeMatcher,RelationshipMatcher
import pandas as pd
class Dateframe(object):
    def __init__(self):
        self.local = 'http://localhost:7474'
        self.username = 'neo4j'
        self.password = '123456'

exam = Dateframe()
graph = Graph(exam.local, username=exam.username, password=exam.password)

# CreateNode
class Dateframe(object):
    def __init__(self):
        self.local = 'http://localhost:7474'
        self.username = 'neo4j'
        self.password = '123456'

def CreateNode(m_graph,m_label,m_attrs):
    m_n="_.name="+"\'"+m_attrs['name']+"\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    print(re_value)
    if re_value is None:
        m_mode = Node(m_label,**m_attrs)
        n = graph.create(m_mode)
        return n
    return None

# Match Node
def MatchNode(m_graph,m_label,m_attrs):
    m_n="_.name="+"\'"+m_attrs['name']+"\'"
    matcher = NodeMatcher(m_graph)
    re_value = matcher.match(m_label).where(m_n).first()
    return re_value
# Create Relationship
def CreateRelationship(m_graph,m_label1,m_attrs1,m_label2,m_attrs2,m_r_name):
    reValue1 = MatchNode(m_graph,m_label1,m_attrs1)
    reValue2 = MatchNode(m_graph,m_label2,m_attrs2)
    if reValue1 is None or reValue2 is None:
        return False
    m_r = Relationship(reValue1,m_r_name,reValue2)
    n = graph.create(m_r)
    return n

if __name__ == "__main__" :

    data1=[{'subject': 'i', 'relation': 'hate', 'object': 'math class'}, {'subject': 'my brother', 'relation': 'is', 'object': 'older'}, {'subject': 'my brother', 'relation': 'is older than', 'object': 'me'}, {'subject': 'i', 'relation': 'am on', 'object': 'soccer team'}, {'subject': 'i', 'relation': 'am old', 'object': '13 years'}]
    subjects = []
    objects = []
    relations = []

    for i in data1:

        subjects.append(i['subject'])
        objects.append(i['object'])
        relations.append(i['relation'])

    for i in subjects:
        if 'my' in i:
            att1=i.split(' ')[0]
            att2=i.split(' ')[1]
            subjects.append('i')
            objects.append(i)
            relations.append('of')


    data = pd.DataFrame({"subject":subjects,"object":objects,"relation":relations})
    print(subjects)
    print(objects)
    label1 = 'personality1'
    label2 = 'personality1'
    for i,j in data.iterrows():
        # 名称
        attr1 = {"name":j.subject}
        CreateNode(graph,label1,attr1)
        # 产品
        attr2 = {"name":j.object}
        CreateNode(graph,label2,attr2)
        m_r_name = j.relation
        reValue = CreateRelationship(graph,label1,attr1,label2,attr2,m_r_name)
        print(reValue)