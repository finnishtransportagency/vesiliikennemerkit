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

def classFactory():
  from .collections.style_script.processing.waterway_sign_stylizer import SignStylizerPNG
  return SignStylizerPNG()

# any other initialisation needed