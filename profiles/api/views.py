from rest_framework import generics, mixins

from accounts.api.serializers import UserSerializer
from profiles.api.serializers import BabysitterProfileSerializer
from profiles.models import BabysitterProfile
from accounts.models import CustomUser


class BabysiiterProfileAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BabysitterProfileSerializer

    def get_queryset(self):
        qs = BabysitterProfile.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class BabysiiterProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BabysitterProfile.objects.all()
    serializer_class = BabysitterProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


