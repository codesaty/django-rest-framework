from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'

    )

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'image',
                  'url', 'created', 'modified_by')

    def save(self, **kwargs):
        return True
