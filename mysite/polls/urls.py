# 뷰를 호출하려면 연결된 URL이 있어야 하고, 이를위해 URLconf가 사용됨
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# 이 다음 단계는 최상위 URLconf에서 polls.urls 모듈을 바라보게 설정하는 것