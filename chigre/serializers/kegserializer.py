from rest_framework import serializers
from chigre.models import Keg
from chigre.serializers import BeerSerializerEx, KegTypeSerializer

class KegSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
  
    class Meta:
        model = Keg
        fields = ('id', 'pintprice', 'canyaprice', 'fullweight', 'emptyweight', 'actualweight', 'beer', 'kegtype', 'creator', 'created')
        
class KegSerializerEx(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    kegtype = KegTypeSerializer(read_only=True)
    beer = BeerSerializerEx(read_only=True)
  
    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.select_related('creator')
        queryset = queryset.prefetch_related('kegtype', 'beer', 
            'beer__creator', 'beer__brewery', 'beer__beertype',
            'beer__brewery__creator')
        return queryset

    class Meta:
        model = Keg
        fields = ('id', 'pintprice', 'canyaprice', 'fullweight', 'emptyweight', 'actualweight', 'beer', 'kegtype', 'creator', 'created')
