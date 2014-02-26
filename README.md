SNA101
======

Quick start for social network analysis with Python and NetworkX.    
    
`mkvirtualenv -i networkx SNA101`**    
**[uses venv wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)    

or

`venv SNA101`    
`pip install networkx`**     
**[uses venv](http://www.virtualenv.org)

Optional:
`pip install Matplotlib` for graph drawing...    

Use *utils/nxGraphtoNodeEdgeList.py* to create csvs easily exportable to Gephi
    
run `utils/community.py` from this directory to deconstruct karate club graph