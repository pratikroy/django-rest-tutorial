from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    """
    The create() and update() methods define how fully fledged instances are
    created or modified when calling serializer.save()
    """
    def create(self, validated_data):
        """Create and return a new snippet instance, given the validated data"""
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return existing snippet instance"""
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
