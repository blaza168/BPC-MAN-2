class Entry(object):

  def __init__(self, name, institution, country, publications_count, citation_count, citations_per_publication):
    self.name = name
    self.country = country
    self.publications_count = publications_count
    self.citation_count = citation_count
    self.citations_per_publication = citations_per_publication
