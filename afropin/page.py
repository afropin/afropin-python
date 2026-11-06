class Page:
    """
    One page of a list. Iterate it for the records; paging is None when you asked for page="all". Ask for the next
    page with {"page": page.paging["page"] + 1}.
    """

    def __init__(self, data, paging=None):
        self.data = data
        self.paging = paging

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    @property
    def has_more(self):
        return self.paging is not None and self.paging["page"] < self.paging["pages"]
