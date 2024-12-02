import graphene
from graphene_django.types import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info):
        return Task.objects.all()

class CreateTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        task = Task.objects.create(title=title)
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        id = graphene.ID()
        completed = graphene.Boolean()

    def mutate(self, info, id, completed):
        task = Task.objects.get(pk=id)
        task.completed = completed
        task.save()
        return UpdateTask(task=task)

class DeleteTask(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        try:
            task = Task.objects.get(pk=id)
            task.delete()
            return DeleteTask(success=True)
        except Task.DoesNotExist:
            return DeleteTask(success=False)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)