from py2neo import Graph
graph = Graph("http://neo4j:holagrupo@127.0.0.1:7474/db/data")
print(graph.run("MATCH (a:canal) RETURN a.name, a.link").data())