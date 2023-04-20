from rest_framework import serializers, viewsets, permissions

from api.serializers import PostSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.user != self.request.user:
            raise serializers.ValidationError("You can only update your own posts.")
        serializer.save()


