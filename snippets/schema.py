import graphene 
from graphene_django.types import DjangoObjectType
from .models import Snippet


class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet

class Query(graphene.ObjectType):
    all_snippetss = graphene.List(SnippetType)

    def resolve_all_snippetss(self, info, **kwargs):
        return Snippet.objects.all()
