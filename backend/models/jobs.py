from sqlmodel import SQLModel, Field

class job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    company: str
    url: str
    date_applied: str
    status: str

    def getTitle(self):
        return self.title

    def getCompany(self):
        return self.company

    def getUrl(self):
        return self.url

    def getDateApplied(self):
        return self.date_applied

    def getStatus(self):
        return self.status