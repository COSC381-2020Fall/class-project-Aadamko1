import sys

#term --> object
#"home and child" --> searches for document that contains
#both home and child (but not necessarily only in that order)
#***"and"*** is a stop word, wont query

from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

ix = open_dir("indexdir")
with ix.searcher(weighting=scoring.Frequency) as searcher:
    queryParser = QueryParser("description", ix.schema)
    query = queryParser.parse("best idea")
    #print(query)
    #query = queryParser.parse("\best idea\"") --> phrase
    results = searcher.search(query, limit=10)
    print(results[0]['title'])