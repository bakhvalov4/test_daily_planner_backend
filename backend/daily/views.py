from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Daily
from .serializer import DailySerializer


class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer

    @action(detail=True, methods=['post'])
    def worked_out(self, request, pk=None):
        daily = self.get_object()
        daily.is_done = not daily.is_done
        daily.save()
        return Response({'id': daily.id, 'is_done': daily.is_done})
