from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
  #  image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'url', 'user', 'content', 'timestamp', 'updated')

    # def get_image(self, obj):
    #     img_  = static("comments/img/user.png")
    #     # if obj.user.profile.image:
    #         # img_ = obj.user.profile.image
    #     return img_