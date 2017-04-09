#coding=utf-8

#URI metninin oluşturulması:
#1. CSV dosyasının konumu 
uri="""file:///C:/Users/banbar/Dropbox/GMT_352_GIS/MY_BOOK/Code/Dunya_Veri/rastgeleNoktalar.csv?"""
#2. Dosyanın türünü belirtmemiz gerekiyor:
uri += """type=csv&"""
#3. X-değerleri hangi sütuna karşılık geliyor?
uri += """xField=longitude&"""
#4. Y-değerleri hangi sütuna karşılık geliyor?
uri += """yField=latitude&"""
#5. EPSG'nin belirlenmesi:
uri += """crs=epsg:4326"""

# Katmanın QGIS katman paneline eklenmesi
layer=QgsVectorLayer(uri,"Rastgele Noktalar","delimitedtext")
QgsMapLayerRegistry.instance().addMapLayers([layer])