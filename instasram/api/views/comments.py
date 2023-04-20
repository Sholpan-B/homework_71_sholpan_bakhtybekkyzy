from rest_framework import serializers, viewsets, permissions

from api.serializers import CommentSerializer
from comment.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.user != self.request.user:
            raise serializers.ValidationError("You can update only your own comments.")
        serializer.save()
