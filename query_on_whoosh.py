import sys
import json

#term --> object
#"home and child" --> searches for document that contains
#both home and child (but not necessarily only in that order)
#***"and"*** is a stop word, wont query

from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir


def query(query_str, page_Number, items_per_page):
    ix = open_dir("indexdir")
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("description", ix.schema).parse(query_str)
        results = searcher.search(query, limit=None)
        num_query_results = len(results)
        query_results = []
        

        for i in range(start_index, min(len(results), end_index)):
            d = {}
            d['url'] = "https://www.youtube.com/watch?v=%s" % results[i]['id']
            d['title'] = results[i]['title']
            d['description'] = results[i]['description']
            d['score'] = results[i].score
            query_results.append(d)
    
    return query_results, num_query_results

if __name__ == "__main__":
    query_str = sys.argv[1]
    page_Number = int(sys.argv[2])
    items_per_page = int(sys.argv[3])
    query(query_str, page_Number, items_per_page)