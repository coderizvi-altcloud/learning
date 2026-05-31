from pydantic import BaseModel,ConfigDict,Field
from datetime import datetime

class PostBase(BaseModel):
    title: str = Field(min_length = 1, max_lenght = 100)
    content : str = Field(min_length= 1)
    author : str = Field(min_length=1,max_length=50)

#this defines what we accpet when creating a new post
class PostCreate(PostBase):   #this will inherit from postbase
    pass

#this defines what we return from our api
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id : int
    date_posted : str