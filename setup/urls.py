
from django.contrib import admin
from django.urls import path, include, re_path
from school.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Ecola teste",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("Alunos", AlunosViewSet, basename="Alunos")
router.register("Cursos", CursosViewSet, basename="Cursos")
router.register("Matriculas", MatriculasViewSet, basename="Matriculas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    re_path(r'^doc/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
