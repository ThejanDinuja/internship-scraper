from sqlmodel import SQLModel, Field


class JobBase(SQLModel):
    title: str
    company: str
    url: str = Field(unique=True)


class Job(JobBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


    def getTitle(self):
        return self.title

    def getCompany(self):
        return self.company

    def getUrl(self):
        return self.url
