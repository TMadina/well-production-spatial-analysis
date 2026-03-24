# Generate synthetic depth and production data for wells
import random

layer = iface.activeLayer()


from qgis.PyQt.QtCore import QVariant

provider = layer.dataProvider()

provider.addAttributes([
    QgsField("depth_m", QVariant.Int),
    QgsField("production", QVariant.Double)])
layer.updateFields()


with edit(layer):
    for f in layer.getFeatures():
        depth = random.randint(700, 1500)
        

        production = depth * random.uniform(0.05, 0.2)
        
        f["depth_m"] = depth
        f["production"] = production
        
        layer.updateFeature(f)
