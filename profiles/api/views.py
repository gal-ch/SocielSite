from rest_framework import generics, mixins
from profiles.api.serializers import BabysitterProfileSerializer
from profiles.models import BabysitterProfile


class BabysiiterProfileAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = BabysitterProfileSerializer

    def get_queryset(self):
        qs = BabysitterProfile.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BabysiiterProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = BabysitterProfile.objects.all()
    serializer_class = BabysitterProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)