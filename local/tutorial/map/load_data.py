import os
from map.models import Evacuation
from django.contrib.gis.utils import LayerMapping



# ModelとGeojsonファイルのカラムのマッピング
mapping = {

   'evacuation_site': '指定緊急避難場所',
   'location': '所在地',
   'flood': '洪水',
   'landslides': 'がけ崩れ、土石流及び地滑り',
   'storm_surge' : '高潮',
   'earthquake': '地震',
   'tsunami': '津波',
   'massive_fire': '大規模な火事',
   'inland_flooding': '内水氾濫',
   'volcanic_phenomena': '火山現象',
   'geom' : 'POINT',
}

# ファイルパス
geojson_file = os.path.abspath(
  os.path.join(os.path.dirname(__file__), 'data','hinanjo.geojson'))

# 実行
def run(verbose=True):
   lm = LayerMapping(Evacuation, geojson_file,    
        mapping,transform=False, encoding='UTF-8')
   lm.save(strict=True, verbose=verbose)