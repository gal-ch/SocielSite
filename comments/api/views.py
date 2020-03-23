from rest_framework import generics
from comments.api.serializers import CommentSerializer
from comments.models import Comment


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    # authentication_classes = []
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        url = self.request.GET.get("url")
        if url:
            return Comment.objects.filter(url=url)
        return Comment.objects.none()


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
