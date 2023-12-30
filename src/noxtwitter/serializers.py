from rest_framework import serializers

from noxtwitter import models


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)

    def get_likes_count(self):
        return self.instance.get_likes_count()

    class Meta:
        model = models.Post
        fields = ['id', 'content', 'creator', 'created_at', 'likes_count']
        extra_kwargs = {
            'creator': {'read_only': True}
        }
