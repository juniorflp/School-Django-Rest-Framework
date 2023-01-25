from rest_framework import viewsets
from school.models import Aluno, Curso, Matricula
from school.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todos oas matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
