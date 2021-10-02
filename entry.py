class Entry(object):

    def __init__(self, name, institution, country, publications_count, citation_count):
        self.name = name
        self.institution = institution
        self.country = country
        self.publications_count = publications_count
        self.citation_count = citation_count

    def __str__(self):
        return "%s,%s,%s,%d,%d,%.2f" % (self.name, self.institution, self.country, self.publications_count, self.citation_count,
                                   self.publications_count / self.citation_count if self.citation_count > 0 else 0)
