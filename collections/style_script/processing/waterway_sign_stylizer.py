"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterBoolean,
                       QgsApplication,
                       QgsSymbolLayer,
                       QgsProperty,
                       QgsRasterMarkerSymbolLayer)


class SignStylizerPNG(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    SIGN_CODE_FIELD = 'sign_code_field'
    SPEED_LIMIT_FIELD = 'speed_limit_field'
    OLD_OR_NEW = "old_or_new"
    MODIFY_SIZE = 'modify_size'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return SignStylizerPNG()

    def name(self):
        return 'sign_stylizer_png'

    def displayName(self):
        return self.tr('Finnish Waterway Sign Stylizer (PNG)')

    def group(self):
        return self.tr('scripts')

    def groupId(self):
        return 'scripts'

    def shortHelpString(self):
        return self.tr("Takes point data layer with Finnish waterway sign codes as input" +
                       " and visualizes each point with the equivalent sign PNG." +
                       " Optionally adjusts image size based on map scale.")

    def initAlgorithm(self, config=None):
        # self.addParameter(
        #     QgsProcessingParameterEnum(
        #         self.OLD_OR_NEW,
        #         self.tr('Visualisoitko vanhoilla vai uusilla liikennemerkeillä?'),
        #         ["Vanhoilla", "Uusilla"]
        #     )
        # )

        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Valitse liikennemerkkitaso'),
                [QgsProcessing.TypeVectorPoint]
            )
        )

        self.addParameter(
            QgsProcessingParameterField(
                self.SIGN_CODE_FIELD,
                'Valitse sarake, jossa merkkikoodit ovat. Esimerkiksi: \n-Digiroad (vanhat merkit): VANHAKOODI \n-Digiroad: TYYPPI\n'+
                '-Tierekisteri (Vanhat): S_ASETUSNR\n-Tierekisteri: S_UUSIASNR',
                '',
                self.INPUT))

        speed_parameter = QgsProcessingParameterField(
            self.SPEED_LIMIT_FIELD,
            'Valitse sarake, jossa liikenteen nopeusrajoitusarvot ovat. \n-Digiroad: ARVO \n'+
            '-Tierekisteri: LMTEKSTI',
            '',
            self.INPUT)
        speed_parameter.setFlags(QgsProcessingParameterField.FlagOptional)

        self.addParameter(speed_parameter)

        self.addParameter(
            QgsProcessingParameterBoolean(
                self.MODIFY_SIZE,
                "Muokkaa myös kuvien kokoa, siten että ne skaalautuvat mittakaavan mukaan",
                True))

    def processAlgorithm(self, parameters, context, feedback):
        input_layer = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        value_field = self.parameterAsString(parameters, self.SIGN_CODE_FIELD, context)
        speed_field = self.parameterAsString(parameters, self.SPEED_LIMIT_FIELD, context)
        old_or_new_selection = self.parameterAsString(parameters, self.OLD_OR_NEW, context)
        size_selection = self.parameterAsBool(parameters, self.MODIFY_SIZE, context)

        if old_or_new_selection == "1":
            old_or_new_selection = "new"
        else:
            old_or_new_selection = "old"

        # Assume PNG files are stored similarly to SVGs but under a 'png' folder. NOTE: 'png' folder is the root folder of the installed collection and doesn't need to be included in the path.
        resource_path = (QgsApplication.qgisSettingsDirPath() + "resource_sharing/collections/Väylävirasto " + 
                         "navigation signs (Vesiliikennemerkit 0.1)/png/")
        resource_path = resource_path.replace("\\", "/")

        # The rest of the script would proceed similarly, but we'll use a simple PNG marker symbol layer
        # For simplicity, this example does not include conditional logic based on speed limit
        # You will need to adjust the path expressions to match your PNG file naming and structure

        path_exp = "concat(\'{0}\', \"{1}\", '.png')".format(resource_path, value_field)

        size_exp = ("CASE WHEN @map_scale < 10000 THEN 7 WHEN @map_scale < 50000 THEN 5.5" + 
                    " WHEN @map_scale < 100000 THEN 5 WHEN @map_scale < 150000 THEN 4.5 WHEN @map_scale < 500000"+ 
                    " THEN 3.5 ELSE 2.5 END")

        # Raster layer for using PNG-images as marker symbols
        raster_layer = QgsRasterMarkerSymbolLayer("circle")
        
        rend = input_layer.renderer().clone()
        rend.symbol().changeSymbolLayer(0, raster_layer)
        
        # defining the image path expression
        rend.symbol().symbolLayer(0).setDataDefinedProperty(QgsSymbolLayer.PropertyName, 
        QgsProperty.fromExpression(path_exp))
        
        if size_selection:
            rend.symbol().symbolLayer(0).setDataDefinedProperty(QgsSymbolLayer.PropertySize, QgsProperty.fromExpression(size_exp))
        
        input_layer.setRenderer(rend)
        input_layer.triggerRepaint()

        return {"Styling": "complete"}
