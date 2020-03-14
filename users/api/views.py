from rest_framework import generics, mixins
from users.api.serializers import UserSerializer
from users.models import CustomUser


class UserListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #only Authentication user can creat profile

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)